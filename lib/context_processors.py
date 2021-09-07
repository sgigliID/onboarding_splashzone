from lib.sitestuff import current_site

from advertising import get_ad


def site_processor(request):
    """Sets up some context variables that will get used by most views.
        Override these values in individual Views' context as needed.

        NOTE: this also sets the current site as a custom variable on the request object itself.
        This is a convience so that we don't need to query the database for the current site all
        over the place. If we have a request object, we have the current site.

        :return: Dictionary of values that base template needs:
            site - Site Object instance that is currently running
            show_topics - Boolean, controls whether to include the topic navbar in the base template
            show_footer_signup - Boolean, controls whether to include the footer signup in the base template
            spoonser - a random Ad defined in the advsertising app
        :rtype: Dict
    """
    this_site = current_site()
    request.site = this_site
    return {
        'site': this_site,
        'show_topics': True,
        'show_footer_signup': True,
        'spoonser': get_ad()
    }
