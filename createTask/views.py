from django.http import HttpResponse, JsonResponse
from myapp.models import Project
# Create your views here.
def index(request):
    return HttpResponse("index page")

def hello(request, username):
    return HttpResponse("<h2>hello %s</h2>" % username)

def about(request):
    return HttpResponse("<p> acerca de </p>")

def MyTask(request):
    return HttpResponse('My tasks')

def MyProject(request):
    project = list(Project.objects.values())
    return JsonResponse(project, safe=False)
