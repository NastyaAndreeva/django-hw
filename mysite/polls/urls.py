from django.urls import path

from . import views

urlpatterns = [
    path("", views.note_list, name="notes"),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('note/new/', views.create_or_edit_note, name='create_note'),
    path('note/edit/<int:note_id>/', views.create_or_edit_note, name='edit_note'),
    path('note/delete/<int:note_id>/', views.delete_note, name='delete_note'),
]