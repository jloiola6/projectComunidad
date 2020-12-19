"""teste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import  admin
from django.urls import  include, path
from django.conf import settings
from django.conf.urls.static import static
from site_joao import views

urlpatterns = [
    path('', views.main, name='main'),
    path('conteudo', views.conteudo, name='login'),
    # path('admin/', admin.site.urls),
    path('cadastro/', views.register, name='cadastro'),
    path('entrar/', views.login, name='entrar'),
    path('adicionar/', views.adicionar, name = 'adicionar'),
    path('logout/', views.logout, name='logout'),
    path('aprovar/', views.aprovar, name='aprovar'),
    path('deletar/', views.deletarConteudo, name='deletar'),
    path('aprovarConteudo/', views.aprovarConteudo, name='aprovar'),
    path('moderadores/', views.moderadores, name='moderadores'),
    path('tornarAdm/', views.tornarAdm, name='tornarAdm'),
    path('retirarAdm/', views.retirarAdm, name='retirarAdm'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


