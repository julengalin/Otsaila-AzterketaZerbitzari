from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    
    path('jantzia/kudeaketa/', TemplateView.as_view(template_name='arropaAriketa/jantzia/jantzia_kudeaketa.html'), name='jantzia-kudeaketa'),
    path('jantzia/list/', views.jantzia_list, name='jantzia-list'),
    path('jantzia/new/', views.new_jantzia, name='new-jantzia'),
    path('jantzia/delete/', views.delete_jantzia, name='delete-jantzia'),
    path('jantzia/edit/', views.edit_jantzia, name='edit-jantzia'),
    path('jantzia/edit-form/<int:jantzia_id>/', views.edit_jantzia_form, name='edit-jantzia-form'),

    path('diseinatzailea/kudeaketa/', TemplateView.as_view(template_name='arropaAriketa/diseinatzailea/diseinatzailea_kudeaketa.html'), name='diseinatzailea-kudeaketa'),
    path('diseinatzailea/list/', views.diseinatzailea_list, name='diseinatzailea-list'),
    path('diseinatzailea/new/', views.new_diseinatzailea, name='new-diseinatzailea'),
    path('diseinatzailea/delete/', views.delete_diseinatzailea, name='delete-diseinatzailea'),
    path('diseinatzailea/edit/', views.edit_diseinatzailea, name='edit-diseinatzailea'),
    path('diseinatzailea/edit-form/<int:diseinatzailea_id>/', views.edit_diseinatzailea_form, name='edit-diseinatzailea-form'),

    path('bilduma/kudeaketa/', TemplateView.as_view(template_name='arropaAriketa/bilduma/bilduma_kudeaketa.html'), name='bilduma-kudeaketa'),
    path('bilduma/list/', views.list_bilduma, name='list-bilduma'),
    path('bilduma/new/', views.new_bilduma, name='new-bilduma'),
    ]
