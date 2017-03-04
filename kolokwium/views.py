from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    return render(request, 'kolokwium/index.html', {'kolokwium_list': Kolokwium.objects.all()})

def kolokwium(request, kolokwium_id):
    kolokwium = get_object_or_404(Kolokwium, pk=kolokwium_id)
    questions_and_answers = None
    if request.user.is_authenticated:
        questions_and_answers = []
        questions = Question.objects.filter(kolokwium=kolokwium)
        for q in questions:
            answer = UserAnswer.objects.filter(user=request.user, choice__question=q)
            if len(answer) == 0:
                questions_and_answers.append((q, None))
            else:
                answer = answer[0]
                valid = ValidChoice.objects.filter(question=q, choice=answer.choice)
                if len(valid) == 0:
                    questions_and_answers.append((q, False))
                else:
                    questions_and_answers.append((q, True))
    return render(request, 'kolokwium/kolokwium.html', {'kolokwium': kolokwium, 'questions_and_answers': questions_and_answers})

def question(request, kolokwium_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = UserAnswer.objects.filter(choice__question=question)
    answer = None
    good = None
    if request.user.is_authenticated and len(answers) > 0:
        answer = answers[0]
        good = ValidChoice.objects.filter(question=question)[0].choice
    return render(request, 'kolokwium/question.html', {'question': question, "answer": answer, "good": good})


@login_required
def answer(request, kolokwium_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'kolokwium/question.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        answer = UserAnswer()
        answer.choice = selected_choice
        answer.user = request.user
        answer.save()
        return HttpResponseRedirect(reverse('kolokwium:question', args=(kolokwium_id, question.id)))
