from django.http import  Http404, HttpResponseRedirect
from django.shortcuts import  render
from django.template.base import TemplateDoesNotExist
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class CVView(TemplateView):
    template_name = "cv.html"

class ContactView(TemplateView):
    template_name = "iletisim.html"

class TodoView(TemplateView):
    template_name = "todo.html"

class SorularView(TemplateView):
    template_name = "sorular.html"

def article(request, article_url):
    try:
        if article_url:
            resp = render(request, "konular/" + article_url + ".html")
        else:
            resp = HttpResponseRedirect('/konular/kanser_genel_bilgi')

    except TemplateDoesNotExist :
        raise Http404
    return resp
