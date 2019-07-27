from django.views import View
from django.shortcuts import render, redirect
from .models import Ranking
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from game.forms import SignUpForm, ScoreForm


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
        return render(request, "game.html")

    def post(self, request):
        my_rank = Ranking()
        my_rank.name = request.user.profile
        my_rank.score = request.POST['score']
        my_rank.save()

        return redirect('rankings')


class MenuView(View):
    def get(self, request):
        return render(request, "menu.html")


class RankingView(View):
    def get(self, request):
        rankings = Ranking.objects.order_by('-score')[:5]
        ctx = {"rankings": rankings}
        return render(request, "rankings.html", ctx)
