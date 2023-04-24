from django.urls import path
from .views import IndexView, bomView

urlpatterns = [
    path('', IndexView, name='index'),
    path('bomcomparison/', bomView, name="dash_bom_url"),
]
