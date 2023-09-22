from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('service-list/', views.service_list, name='service-list'),
    path('contact/', views.contact, name='contact'),
    path('contact-list/', views.contact_list, name='contact-list'),
    path('contact-edit/<int:pk>/', views.contact_edit, name='contact-edit'),
    path('contact-delete/<int:pk>/', views.contact_delete, name='contact-delete'),
    path('feedback/', views.feedback, name='feedback'),



    ########################################################################
    #url for task management system
    path('create-task/', views.task, name="task"),
    path('task-list/', views.task_list, name="task-list"),
    path('edit-task/<int:id>/', views.edit_task, name="edit-task"),
    path('delete-task/<int:pk>/', views.delete_task, name="delete-task"),
    path('completed-task/', views.completed_task, name="completed-task"),
]
