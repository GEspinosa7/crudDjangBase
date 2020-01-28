from django.urls import path
from .views import list_appteste, create_appteste, update_appteste, delete_appteste

urlpatterns = [
    path('', list_appteste, name='list_appteste'),
    path('new/', create_appteste, name='create_appteste'),
    path('update/<int:id>/', update_appteste, name='update_appteste'),
    path('delete/<int:id>/', delete_appteste, name='delete_appteste'),
]