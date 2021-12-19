from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect # 라다이렉트 기능 사용
from .models import Question, Choice
from django.template import loader
from django.urls import reverse # URL 처리를 위해 request 객체는 필수 인자, question_id 인자를 받음
                                # path('<int:question_id>/vote/', views.vote, name='vote')
from django.views import generic

# Create your views here.

'''제너릭 뷰로 변환'''
### Generic View (class-based views)

'''generic.ListView : 특정 모델의 리스트를 출력해주는 뷰
    어떤 모델(model)에 대해 어떻게 리스트를 얻어올지 쿼리가 필요하고(queryset), 이것을 어느 템플릿(templates_name)에 어떤 파라미터명으로 전달할지(context_object_name)을 정의해야 함'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' # context_object_name : html에 전달할 파라미터명 지정

    '''Return the last five published questions.'''
    def get_queryset(self): # get_queryset() : 데이터베이스에 query할 객체를 정하는 함수, 템플릿으로넘겨줄 model 리턴
        return Question.objects.order_by('-pub_date')#[:5]

    paginate_by = 5  # 한 페이지에 몇 개의 리스트 출력할 지 결정

'''generic.DetailView :  특정 모델의 특정 오브젝트에 대한 자세한 정보를 출력해주는 뷰
        어떤 모델(model)의 어떤 오브젝트(pk)를 어느 템플릿(template_name)에 어떤 파라미터명(context_object_name)으로 전달할지를 정의해주어야 함'''
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else: # 다음 익셉션이 처리되지 않고 정상 처리하는 경우
        selected_choice.votes += 1 # Choice 객체의 votes 속성, 즉 선택 카운트를 +1 증가시킴
        selected_choice.save() # 변경 사항을 Choice 테이블에 저장
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class AllResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/allresults.html'