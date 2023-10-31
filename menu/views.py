from django.http import HttpResponse
from django.template import loader
from .models import Menu

def menu(request):
    menu = Menu.objects.all().values()
    template = loader.get_template('all_menu.html')
    context = {
        'menu': menu,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse(menu)

def details(request, id):
  menu = Menu.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'menu': menu,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))