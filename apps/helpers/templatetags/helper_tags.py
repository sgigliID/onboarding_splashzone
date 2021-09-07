import os.path
from django import template

register = template.Library()


@register.filter(name='pdb')
def pdb(item, item2=None):
    """Allows you to drop a PDB in a template
        Examples:
        {{variable_in_template|pdb}}
        variable_in_template will be passed to this function as 'item'

        {{variable_in_template|pdb:other_variable_in_template}}
        variable_in_template will be passed to this function as 'item',
        other_variable_in_template will be passed to this function as item2

        :return: N/A
    """
    import pdb  # noqa
    pdb.set_trace()  # noqa


@register.filter(name='story_image')
def story_image(story):
    """Returns the static path to a story's image, if it exists in the file system
        based on the story's PK

        :param story: technically any object that has a 'pk' property, but a News Post is expected
        :type story: Object

        :return: Path to image file matching the objet's pk OR a default image path if matching image doesn't exist
        :rtype: String
    """
    if story:
        image_path = 'static/image/news/{}.jpg'.format(story.pk)
        if os.path.exists(image_path):
            return 'image/news/{}.jpg'.format(story.pk)
    return 'image/placeholder-img.jpg'


@register.filter(name='gherkinize_step')
def gherkinize_step(step):
    """Returns HTML that pretifies a string if it looks like a Gherkin step or a table

        :param step: a string meant to be a step in a prompt scenatrio
        :type step: String

        :return: A formatted HTML string if the provided 'step' string starts with a
            Gherkin keyword or contains a table tag
        :rtype: String
    """
    gherkin_starters = [
        'Given', 'When', 'Then', 'And'
    ]
    split_str = step.split(' ')
    if split_str[0] in gherkin_starters:
        split_str[0] = '<strong>{}</strong>'.format(split_str[0])
        return ' '.join(split_str)
    if '<table>' in step:
        return '<code>{}</code>'.format(step)
    return step
