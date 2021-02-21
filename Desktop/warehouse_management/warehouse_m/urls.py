from django.urls import path
from . import views


app_name = 'warehouse_m'


urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
    path('results/', views.search_index, name='search_index'),
    path('update/<pk>', views.UpdateProduct.as_view(), name='update'),
    path('create', views.CreateProduct.as_view(), name='create'),
    path('delete/<pk>', views.DeleteProduct.as_view(), name='delete'),
]

