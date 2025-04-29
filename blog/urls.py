from django.urls import path
from . import views
urlpatterns= [
    path('', views.home, name='home'),
    path('profile/',views.profile_view, name='profile_view'),
    path('crear_articulo/', views.crear_articulo, name='crear_articulo'),
    path('editar/<int:article_id>/',views.editar_articulo,name='editar_articulo'),
    path('eliminar/<int:article_id>/',views.eliminar_articulo, name='eliminar_articulo'),
    path('articulo/<int:article_id>/',views.articulo_view, name='articulo_view'),
    path('like/<int:article_id>', views.likear, name='likes'),
    path('comentar/<int:article_id>', views.comentar, name='comentar'),
    path('crear_description/',views.crearDescription,name='crear_description'),
    path('InfoUser/',views.actualizar_infoUser,name='info_user')
]
