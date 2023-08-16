from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Word

# Create your views here.


def index(request):
    word_list = Word.objects.order_by('-word_text')
    template = loader.get_template('words/index.html')
    context = {
        'word_list': word_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, word_id):
    word = Word.objects.get(pk=word_id)
    return JsonResponse(word.get_dict())


def random(request, language):
    word_subset = Word.objects.filter(word_lang=language)
    word = word_subset.order_by('?').first()
    return JsonResponse(word.get_dict())
