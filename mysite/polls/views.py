from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect,HttpResponse
from django.http import Http404
from django.core.urlresolvers import reverse

from .models import Choice,Question
from django.views import generic
from django.utils import timezone

'''
def index(request):
	# return HttpResponse("Hello, world. You're at the polls index")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    # return HttpResponse(template.render(context))
    #此处用render代替
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# Leave the rest of the views (detail, results, vote) unchanged

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
	# try:
	#     question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	#     raise Http404("Question does not exist")
	# return render(request, 'polls/detail.html', {'question': question})
	#引入get_object_or_404快捷方式
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''

# 用Django的通用视图代替
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]
    def get_queryset(self):
     """
     Return the last five published questions (not including those set to be
     published in the future).
     """
     return Question.objects.filter(
         pub_date__lte=timezone.now()
     ).order_by('-pub_date')[:5]
		
		

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
	     """
	     Excludes any questions that aren't published yet.
	     """
	     return Question.objects.filter(pub_date__lte=timezone.now())



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': p,
   			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # reverse函数避免了我们在视图函数中硬编码URL
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))