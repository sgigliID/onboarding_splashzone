from django.template import loader
from django.http import HttpResponse
from django.views import View

from wavepool.onboarding_exercise_defs import prompts


def instructions(request):
    """Displays onboarding instructions
    """
    template = loader.get_template('instructions2.html')

    context = {
        'prompts': prompts,
        'spoonser': None,
        'show_topics': False,
        'show_footer_signup': False,
    }
    return HttpResponse(template.render(context, request))


def prompts_view(request, prompt_id):
    """Displays all onboarding prompts
    """
    template = loader.get_template('prompt.html')
    selected_prompt = prompts[prompt_id - 1]

    if prompt_id < len(prompts):
        next_prompt = prompt_id + 1
    else:
        next_prompt = None

    if prompt_id > 1:
        previous_prompt = prompt_id - 1
    else:
        previous_prompt = None

    context = {
        'prompt': selected_prompt,
        'next_prompt': next_prompt,
        'previous_prompt': previous_prompt,
        'spoonser': None,
        'show_topics': False,
        'show_footer_signup': False,
    }
    return HttpResponse(template.render(context, request))


class Signup(View):
    """Dummy class for signup thank you page
    """
    def setup(self, request, *args, **kwargs):
        super(Signup, self).setup(request, *args, **kwargs)
        self.template = loader.get_template('thankyou.html')
        self.context = {
            'spoonser': None,
            'show_topics': False,
            'show_footer_signup': False,
        }

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.template.render(self.context, request))

    def post(self, request, *args, **kwargs):
        return HttpResponse(self.template.render(self.context, request))
