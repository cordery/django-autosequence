from django.urls import path

from . import views

urlpatterns = [
    path('locked', views.TestLockedTableRaceView.as_view(), name='test_race_locked'),
    path('not_locked', views.TestNoLockRaceView.as_view(), name='test_race_no_lock')
]
