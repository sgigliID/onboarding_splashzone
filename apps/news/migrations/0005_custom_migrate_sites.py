# Generated by Django 3.2.4 on 2021-08-30 15:11

from django.db import migrations
from news.models import NewsPost
from django.contrib.sites.models import Site


def forward(apps, schema_editor):
    for np in NewsPost.objects.all():
        np.site = Site.objects.get(name=np.divesite.display_name)
        np.save()


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210830_1511'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]
