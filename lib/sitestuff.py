from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.urls import reverse
from django.utils.html import format_html


def current_site():
    return Site.objects.get(pk=settings.SITE_ID)

def getSiteManager():  # noqa
    # note first object manager is the default
    if not settings.SITE_ID or settings.SITE_ID == 999:
        objects = models.Manager()
    elif not settings.SITEMODEL_ENABLED:
        # Don't warn if we deliberately turned off the site model
        objects = models.Manager()
    else:

        objects = CurrentSiteManager()
        # logger.info("Using SITE %d for model %s" % (settings.SITE_ID,self.__class__.__name__,))
    return objects


class MyManager(models.Manager):
    use_in_migrations = True


class SiteModel(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    objects = getSiteManager()

    all_sites = MyManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.site_id and settings.SITE_ID and settings.SITE_ID != 999:
            self.site_id = settings.SITE_ID
            # import pdb; pdb.set_trace()
        # is SITE_ID is 999, allow it to fall through to normal logic (i.e. integrity fail)
        super(SiteModel, self).save(*args, **kwargs)

    def get_full_url(self):
        """ constructs full absolute url based on site associated with this object even if that isn't
            the get_current_site value. (i.e. will use https://www.utilitydive.com/... no matter what, even
            on QA or from a different site settings file) """
        full_url = ''.join(['https://', self.site.domain, self.get_absolute_url()])
        return full_url

    def get_absolute_admin_url(self):
        return reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=(self.pk,))

    def get_full_admin_url(self):

        info = (self._meta.app_label, self._meta.model_name)
        return format_html(
            ''.join(
                [
                    'https://',
                    self.site.domain,
                    reverse('admin:%s_%s_change' % info, args=(self.pk,))
                ]
            )
        )
