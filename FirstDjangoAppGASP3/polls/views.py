# Create your views here.
from django.http import HttpResponse
from .models import Question


#def index(request):
#	return HttpResponse("Hello, world. Yo're at the polls index.")

#def index(request):
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#
#	output = ','.join([k.question_text for k in latest_question_list])
#	return HttpResponse(output)

#from django.template import RequestContext, loader

#def index(request):
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	template = loader.get_template('polls/index.html')
#	context = RequestContext(request, {
#		'latest_question_list': latest_question_list,
#	})
#	return HttpResponse(template.render(context))

# ## o codigo acima pode ser reescrito utilizando o atalho render()

from django.shortcuts import render

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list}
	return render (request, 'polls/index.html', context) # retorna um HttpResponse



#def detail(request, question_id):
#	return HttpResponse("You're looking at question %s." %question_id)

#from django.http import Http404
#def detail(request, question_id):
#	try:
#		question = Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404("Question does not exists")
#
#	return render(request, 'polls/detail.html', {'question':question})
from django.shortcuts import get_object_or_404

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})


def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response %question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." %question_id)

def editar_questao(request, question_id=''):
	try:
		question = Question.objects.get(pk=question_id)
	except:
		question = ''
	return render(request, 'polls/edit_question.html', {'question':question})