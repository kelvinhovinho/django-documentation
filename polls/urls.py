from django.urls import path
from . import views

app_name = 'polls'

urlpatterns =[
    path("", views.index, name="Home"),
    path("<int:question_id>/", views.details, name="Detail"),
    path("<int:question_id>/results/", views.results, name="result"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]