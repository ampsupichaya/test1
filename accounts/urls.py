from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.indexView, name="home"),
    path('main/', views.mainView, name="main"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='main'), name="logout"),
    path('insertvocab/', views.vocabView, name="insertvocab"),
    path('showvocab/', views.showvocabView, name="showvocab"),
    path('deletevocab/<int:i>/', views.deletevocabView, name="deletevocab"),
    path('editvocab/<int:i>/', views.editvocabView, name="editvocab"),
]