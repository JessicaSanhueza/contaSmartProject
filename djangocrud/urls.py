
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),

    path('tasks/create/', views.create_task, name='create_task'),
    path('solicitudes/create/', views.create_solicitud, name='create_solicitud'),

    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('solicitudes_completed/', views.solicitudes_completed, name='solicitudes_completed'),

    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('solicitudes/<int:solicitud_id>/', views.solicitud_detail, name='solicitud_detail'),

    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('solicitudes/<int:solicitud_id>/complete', views.complete_solicitud, name='complete_solicitud'),

    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('tasks/<int:solicitud_id>/delete', views.delete_solicitud, name='delete_solicitud'),

    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
