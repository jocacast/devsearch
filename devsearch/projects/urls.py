from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('update-project/<str:pk>', views.updateProject, name='update-project'),
    path('delete-project/<str:pk>', views.deleteProject, name='delete-project'),
    path('create-project/', views.createProject,name="create-project"),
    path('add-to-cart/<str:pk>', views.addToCart, name = 'add-to-cart'),
    path('tag/<str:pk>', views.getTagInfo, name = 'tag')

]
