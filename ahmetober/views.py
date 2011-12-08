from django.http import  Http404
from django.shortcuts import render_to_response, render
from django.template.base import TemplateDoesNotExist
from django.template.context import RequestContext
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class ArticlesView(TemplateView):
    template_name = "articles.html"

class CVView(TemplateView):
    template_name = "cv.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class SSSView(TemplateView):
    template_name = "sss.html"

def article(request, article_url):
    try:
        resp = render(request, "articles/" + article_url + ".html")
    except TemplateDoesNotExist :
        raise Http404
    return resp