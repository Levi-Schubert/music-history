from django.urls import path
from . import views

app_name = "history"
urlpatterns = [
	path("", views.index, name="artists"),
	path("<int:artist_id>/", views.details, name="details")
]