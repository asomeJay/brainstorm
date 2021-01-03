from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Idea

# Create your views here.
def index(request):
    try:
        idea_list = Idea.objects.all()
    except Idea.DoesNotExist:
        raise Http404("Idea does not exit")
    return render(request, 'main/index.html', {'idea_list' : idea_list})


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