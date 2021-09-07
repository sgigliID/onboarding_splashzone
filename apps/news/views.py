from django.template import loader
from django.http import HttpResponse

from news.models import NewsPost
from news.helpers import parse_search_terms
from taxonomy.models import Topic


def front_page(request):
    """ View for the site's front page
        Returns all available newsposts, formatted like:
            cover_story: the newsposts with is_cover_story = True
            top_stories: the 3 most recent newsposts that are not cover story
            recent_stories: the rest of the newsposts, sorted by most recent
    """
    template = loader.get_template('news/frontpage.html')
    cover_story = NewsPost.objects.filter(is_cover_story=True).first()
    all_stories = NewsPost.objects.filter(is_cover_story=False, active=True).order_by('-publish_date')[:8]

    top_stories = all_stories[:3]
    recent_stories = all_stories[3:]

    context = {
        'cover_story': cover_story,
        'top_stories': top_stories,
        'recent_stories': recent_stories,
    }

    return HttpResponse(template.render(context, request))


def newspost_detail(request, newspost_id):
    """Detail page for a given News Post instance
    """
    template = loader.get_template('news/newspost.html')
    newspost = NewsPost.objects.get(pk=newspost_id)
    context = {
        'newspost': newspost,
    }
    return HttpResponse(template.render(context, request))


def archive(request):
    """List of all News Posts or list of News Posts that match a search query

        Search query examples:
            ?text_search=Autonomous+Vehicles
            Returns stories with "Autonomous Vehicles" in the title or body

            ?text_search=Autonomous+Vehicles&topics_1=4&topics_2=7
            Returns stories with "Autonomous Vehicles" in the title or body AND topics in Topic with PK 4 or 7

    """
    template = loader.get_template('news/archive.html')
    topics = Topic.objects.all().order_by('display_name')
    selected_topics, text_search_value = parse_search_terms(request.GET)
    news_archive = NewsPost.search(topics=selected_topics, text_value=text_search_value)
    context = {
        'news_archive': news_archive,
        'topics': topics,
        'text_search_value': text_search_value,
        'selected_topics': selected_topics,
        'searched': selected_topics or text_search_value,
    }

    return HttpResponse(template.render(context, request))
