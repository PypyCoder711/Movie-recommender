
from django.contrib import admin
from django.urls import path
from .views import ZScoreGen

urlpatterns = [
    path('gen_z_score/', ZScoreGen.asView()),
]
