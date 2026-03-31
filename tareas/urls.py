from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from .forms import LoginForm

urlpatterns = [
    path('proyectos/',views.lista_proyectos,name='proyectos'),
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('proyectos/nuevo/',views.crear_proyecto,name='crear_proyecto'),
    path('proyecto/<int:proyecto_id>/',views.detalle_proyecto,name='detalle_proyecto'),
    path('proyectos/<int:proyecto_id>/tarea/nueva/',views.crear_tarea,name='crear_tarea'),
    path('tarea/<int:tarea_id>/toggle/', views.toggle_tarea, name='toggle_tarea'),
    path('registro/', views.registro, name='registro'),
    path('proyecto/editar/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyecto/eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('tarea/editar/<int:tarea_id>/', views.editar_tarea, name='editar_tarea'),
    path('tarea/eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
]
