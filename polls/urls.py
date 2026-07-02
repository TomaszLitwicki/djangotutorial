from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name='index'),
    path("<int:question_id>/", views.detail, name='ksywkadetail'),
    path("<int:question_id>/results/", views.results, name='ksywkaresults'),
    path("<int:question_id>/vote/", views.vote, name='ksywkavote'),
]