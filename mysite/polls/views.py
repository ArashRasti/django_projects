from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404

def index(request):
    question_list = Question.objects.order_by("-pub_date")[0:5]
    # str = " ,".join(q.question_text for q in question_list)
    context = {"question_list" : question_list}
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

# Create your views here.  
def detail(request, question_id):
    try:
        Question.objects.get(pk=question_id)
    except Question.DoesNotExist as ex :
        raise Http404("Question does not exists.")
    return HttpResponse(f"You are looking at quetion detail {question_id}.")

def results(request, question_id):
    response = f"You are looking at the result of the question id={question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    response = f"You are voting a question, id={question_id}"
    return HttpResponse(response)

