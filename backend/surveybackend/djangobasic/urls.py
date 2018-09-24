from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

from rest_framework.routers import DefaultRouter


app_name = 'djangobasic'


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'question', views.QuestionViewSet)
router.register(r'choice', views.ChoiceViewSet)
router.register(r'respond', views.ResponseViewSet)


urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('<int:pk>/', login_required(views.DetailView.as_view()), name='detail'),
    path('<int:pk>/results/', login_required(views.ResultsView.as_view()), name='results'),
    path('<int:question_id>/respond/', views.respond, name='respond'),
    path('api/', include(router.urls)),
]
