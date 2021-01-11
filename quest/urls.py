from django.urls import path

from quest import views

app_name = 'quest'

urlpatterns = [
    path('', views.TodaysQuestionList.as_view(), name='index'),
    path('daily/<int:year>/<int:month>/<int:day>/', views.DailyQuestionList.as_view(), name='daily_questions'),
    path('q/<int:pk>', views.QuestionDetailView.as_view(), name='question_detail'),
    path('ask', views.AskQuestionView.as_view(), name='ask'),
    path('q/<int:pk>/answer', views.CreateAnswerView.as_view(), name='answer_question'),
]
