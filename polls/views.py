from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import Question, Choice

# Create your views here.
# METODA PRZEZ LOADERa
# def index(request):
#     questions = Question.objects.all()
#     template = loader.get_template("polls/index.html")
#     contex = {"question_list" : questions }
#     return HttpResponse(template.render(contex, request))

# METODA PRZEZ RENDERa
def index(request):
    questions = Question.objects.all()
    contex = {"question_list": questions}
    return render(request, "polls/index.html", contex)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)