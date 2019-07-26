from django.views import View
from django.shortcuts import render, redirect
from .models import Ranking
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from game.forms import SignUpForm


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class FirstView(View):
    def get(self, request):

        return render(request, "first.html")


class GameView(View):
    def get(self, request):
        form = '<input name="score" type="text" /><input name="username" type="text" />'
        username = 'someUser'
        return render(request, "game.html", {'form': form, 'username': username})

    def post(self, request):

        return self.get(request)


class MenuView(View):
    def get(self, request):

        return render(request, "menu.html")


class RankingView(View):

    def get(self, request):

        rankings = Ranking.objects.all()
        ctx = {"rankings": rankings}
        return render(request, "rankings.html", ctx)


class AddRanking(CreateView):

    model = Ranking
    fields = '__all__'
    template_name = 'add_rankings.html'
    success_url = reverse_lazy("rankings")