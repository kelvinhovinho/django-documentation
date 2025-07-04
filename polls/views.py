from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.views import generic


from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    model = Question
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def query_set(self):
        return Question.objects.order_by("-pub_date")[:5]

    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # context = {"latest_question_list":latest_question_list}
    # return render(request, "polls/index.html", context)

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, "polls/detail.html", {"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

    return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))

from django.shortcuts import get_object_or_404, render


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"