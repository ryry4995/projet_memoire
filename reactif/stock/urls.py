from django.urls import path # type: ignore
from .views import stock_list, stock_detail, stock_update, stock_delete

app_name = "stock"

urlpatterns = [
    path("liste/", stock_list, name="stock_list"),
    path("<str:code_article>/", stock_detail, name="stock_detail"),
    path("<str:code_article>/update/", stock_update, name="stock_update"),
    path("supprimer/<str:code_article>/", stock_delete, name="stock_delete"),
]
