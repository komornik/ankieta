from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.core.urlresolvers import reverse
from mysite.polls.models import Choice, Poll
from django.views.decorators.csrf import csrf_protect
from django.http import Http404
from django.shortcuts import render_to_response
from mysite.polls.models import Poll

from django import forms
from forms import PollForm

def index(request, template='polls/index.html'):
    return render(request, template, {
        'latest_poll_list': Poll.objects.all().order_by('-pub_date',)[:10]
    })


def vote(request, poll_id, template='polls/detail.html'):
    poll = get_object_or_404(Poll, pk=poll_id)
    pollform = PollForm(request.POST or None, instance=poll)

    if pollform.is_valid():
        instance = pollform.save(commit=False,)
        choice = instance.choice_set.get(id=pollform.cleaned_data['votes'])
        choice.votes += 1
        choice.save()
        return redirect(reverse('results', args=(instance.id,)))

    return render(request, template,{
        'form': pollform,
        'latest_poll_list': Poll.objects.all().order_by('-pub_date',)[:10]
    },)

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': poll})

