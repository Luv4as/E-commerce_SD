from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('enter/', views.login_user, name='enter'),
    path('logout/', views.logout_user, name='logout'),
    path('cadastro/', views.cadastro_user, name='cadastro'),
]
