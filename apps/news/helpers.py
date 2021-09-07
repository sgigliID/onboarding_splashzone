from taxonomy.models import Topic


def parse_search_terms(get_request):
    """Returns a tuple containing
        1. a queryset of Topic instances if 'topics' is in get_request
        2. a string of a text search term if 'text_search' is in get_request

    :param get_request: dictionary of request.GET values
    :type get_request: Dict

    :return: query-able values of search terms
    :rtype: Tuple
    """
    selected_topic_ids = None
    selected_topics = None
    for key, value in get_request.items():
        if key.startswith('topics'):
            if not selected_topic_ids:
                selected_topic_ids = []
            selected_topic_ids.append(int(value))
    text_search = get_request.get('text_search')
    if selected_topic_ids:
        selected_topics = Topic.objects.filter(pk__in=selected_topic_ids)
    return (selected_topics, text_search)
