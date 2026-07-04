from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect #, Http404
# from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.db.models import F

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"questions": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["wybory"])
    except (KeyError, Choice.DoesNotExist):
        return render (
            request, 
                "polls/detail.html", 
                {
                    'questions': question,
                    'error_message': "No i dupa, mówiłem, że nie przesłałeś formularza!"
                },
            )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("pollsapp:ksywkaresults", args=(question.id,)))