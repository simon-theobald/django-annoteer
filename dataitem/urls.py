from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataitem_list, name='dataitem_list'),
    path('dataitem/new', views.dataitem_create, name='dataitem_create'),
    path('dataitem/<int:pk>/edit/', views.dataitem_update, name='dataitem_update'),
    path('dataitem/<int:pk>/delete/', views.dataitem_delete, name='dataitem_delete'),
]


from django.contrib import admin
from django.urls import path, include  # include importieren

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dataitems/', include('dataitems.urls')),  # Pfad zu den URLs Ihrer App
]