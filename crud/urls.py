from . import views
from django.urls import path
app_name = 'crud'
urlpatterns = [
    path('create/',views.create,name='create'),
    path('show/',views.show,name='show'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete,name='delete'),
]