from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

import datetime
from .models import Idea


# Create your views here.
def index(request):
    try:
        latest_idea = Idea.objects.latest('idea_date')
        manufactured_idea_text = latest_idea.idea_text
        if len(latest_idea.idea_text) >= 5:
            manufactured_idea_text = latest_idea.idea_text[:5] + "..."

        time_diff = (timezone.now() - latest_idea.idea_date)
        day_diff_from_now = time_diff.days
        hour_diff_from_now = (datetime.datetime.min + (timezone.now() - latest_idea.idea_date)).time().hour + \
                             day_diff_from_now * 24

    except Idea.DoesNotExist:
        raise Http404("Idea does not exit")

    return render(request, 'main/index.html', {'latest_idea': manufactured_idea_text, 'time_diff': hour_diff_from_now})


def write(request):
    try:
        idea = Idea(idea_text=request.POST['idea'], idea_date=timezone.now())
    except KeyError:
        return render(request, 'polls/index.html', {
            'error_message': "You Typed Error."
        })
    else:
        idea.save()
        return HttpResponseRedirect(reverse('main:index'))
