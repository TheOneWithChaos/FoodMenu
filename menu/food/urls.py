from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [path('', views.IndexClassView.as_view(), name='index'),
            path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
            path('add/', views.add_item, name='add_item'),
            path('update/<int:item_id>/', views.update_item, name='update_item'),
            path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]