from django.urls import path # type: ignore
from . import views
from .views import search_view
app_name = 'article'
urlpatterns = [
    path('home/', views.home_view, name='home_view'),
    path('search/', search_view, name='search'),
    path('article/', views.article_list, name='article_list'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('create/', views.article_create, name='article_create'),
    path('<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('<int:pk>/delete/', views.article_delete, name='article_delete'),
      # Ajouter la route pour la suppression
    path('low_stock/', views.low_stock, name='low_stock'),
]
