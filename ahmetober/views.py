from django.http import  Http404
from django.shortcuts import  render
from django.template.base import TemplateDoesNotExist
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class ArticlesView(TemplateView):
    template_name = "articles.html"

class CVView(TemplateView):
    template_name = "cv.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class TodoView(TemplateView):
    template_name = "todo.html"

class SSSView(TemplateView):
    template_name = "sss.html"

def article(request, article_url):
    try:
        if article_url:
            resp = render(request, "articles/" + article_url + ".html")
        else:
            resp = render(request, "articles/kanser_genel_bilgi.html")
    except TemplateDoesNotExist :
        raise Http404
    return resp