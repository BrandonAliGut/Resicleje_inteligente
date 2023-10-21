from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.template import loader
from Api_Reciclaje_I.models import Category
# Create your views here.
from django.utils import timezone

def home(request):
    template = loader.get_template('Index.html')
    context= {
        
    }
    return HttpResponse(template.render(context, request))
    




def categoryView(request):
    template = loader.get_template('HomeIndex.html')
   
    context = {
        
    }
    return HttpResponse(template.render(context, request))


"""   
class CategoryView(ListView):
    model = Category
     # su propio nombre para la lista como variable de plantilla
    
    template_name = 'Index.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["category"] = Category.objects.all()
        return context
        """ 
