from django.urls import path, include
from . import views
app_name = "main"

urlpatterns = [
	path('', views.homepage, name="home"),
	path('news/', views.newspage, name="news"),
	path('updates/', views.updatespage, name="updates"),
	path('download/', views.downloadpage, name="download"),
]