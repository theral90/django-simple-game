"""phaser_game URL Configuration

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

from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.contrib import admin
from game.views import GameView, FirstView, MenuView, RankingView, signup, home
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^first/$', FirstView.as_view()),
    url(r'^home/$', home, name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^game_view/', GameView.as_view(), name='game'),
    url(r'^menu_view/', MenuView.as_view(), name='menu'),
    url(r'^rankings/', RankingView.as_view(), name='rankings'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
