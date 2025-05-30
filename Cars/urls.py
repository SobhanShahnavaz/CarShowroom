from tokenize import Name
from django.urls import path
from . import views


urlpatterns = [
    path('panel', views.Panel, name='Panel'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>',
         views.updaterecord, name='updaterecord'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('Logout/', views.logout, name='logout'),
    path('About/', views.About, name='About'),
    path('Contact/', views.Contact, name='Contact'),
    path('', views.mainPage, name='mainPage'),
]
