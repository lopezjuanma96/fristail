from django.shortcuts import render
from django.urls import reverse

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader

from .models import Word

# Create your views here.


def index(request):
    query_params = dict(request.GET)
    language = query_params['lang'][0] if 'lang' in query_params else 'en'
    word_list = Word.objects.filter(
        word_lang=language
        ).order_by('-word_text')
    template = loader.get_template('words/index.html')
    context = {
        'word_list': word_list,
        'language': language
    }
    return HttpResponse(template.render(context, request))


def detail(request, word_id):
    word = Word.objects.get(pk=word_id)
    return JsonResponse(word.get_dict())


def add(request):
    word_text = request.POST['word_text']
    word_lang = request.POST['word_lang']
    try:
        word_exists = Word.objects.get(
            word_text=word_text,
            word_lang=word_lang
            )
        word_exists.word_freq += 1.0
        word_exists.save()
    except Word.DoesNotExist:
        new_word = Word(
            word_text=word_text,
            word_lang=word_lang
            )
        new_word.save()
    return HttpResponseRedirect(
        reverse('words:index') + "?lang={}".format(
            request.POST['word_lang']
            )
        )


def random(request, language):
    word_subset = Word.objects.filter(word_lang=language)
    word = word_subset.order_by('?').first()
    return JsonResponse(word.get_dict())
