from django.urls import path
from . import views

app_name="service_center"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('question/', views.question, name="question"),
    path('<int:service_pk>/', views.detail, name="detail"),
    path('<int:service_pk>/comments/',views.comment_create, name="comment_create"),
    path('<int:service_pk>/update', views.update, name="update"),
    path('admin_page/', views.admin_page, name="admin_page"),
    path('<int:service_pk>/<int:question_pk>/delete_comment/', views.delete_comment, name="delete_comment"),
]
