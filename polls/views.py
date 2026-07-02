from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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

#METODA PRZEZ django.http import Http404
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#         contex = {"questions" : question}
#     except Question.DoesNotExist:
#         raise Http404("bla bla bla!!!")
#     return render(request, "polls/detail.html", contex)

#METODA PRZEZ django.shortcuts import get_object_or_404
def detail (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"questions": question})


def results(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)