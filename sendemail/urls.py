from django.urls import path
from . import views
from .views import contact_view


urlpatterns = [
    path('', contact_view, name='contact')
]
