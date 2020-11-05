from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(name):
    """home page learning_logs"""
    return render(name, 'learning_logs/index.html')

@login_required
def topics(name):
    """all pages"""
    topics = Topic.objects.filter(owner=name.user).order_by('date_added')
    context = { 'topics': topics}
    return render(name, 'learning_logs/topics.html', context)

@login_required
def topic(name, topic_id):
    """show topic and all request"""
    topic = Topic.objects.get(id=topic_id)
    #check topic
    if topic.owner != name.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(name, 'learning_logs/topic.html', context)

@login_required
def new_topic(name):
    """ new topic add"""
    if name.method != 'POST':
        #data won send , create empty form
        form = TopicForm()
    else:
        #new data send POST, procesing data
        form = TopicForm(name.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = name.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    
    context = {'form': form}
    return render(name, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(name, topic_id):
    """add new entry"""
    topic = Topic.objects.get(id=topic_id)

    if name.method != 'POST':
        #date wont send new form
        form = EntryForm()
    else:
        #send post procesing date
        form = EntryForm(data=name.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(name, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(name, entry_id):
    """red current entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != name.user:
        raise Http404

    if name.method != 'POST':
        #first req; form fill current entry
        form = EntryForm(instance=entry)
    else:
        #send data post; procesing data
        form = EntryForm(instance= entry, data=name.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(name, 'learning_logs/edit_entry.html', context)