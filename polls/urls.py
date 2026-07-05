from django.urls import path
from . import views

app_name = "pollsapp"
urlpatterns =[
    path("", views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.QuestionDetailView.as_view(), name='ksywkadetail'),
    path("<int:pk>/results/", views.QuestionResultsView.as_view(), name='ksywkaresults'),
    path("<int:question_id>/vote/", views.vote, name='ksywkavote'),
]