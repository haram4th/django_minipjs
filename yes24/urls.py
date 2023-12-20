from django.urls import path
from . import views

app_name = 'yes24'

urlpatterns = [
    path('', views.yes24index, name='yes24index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]