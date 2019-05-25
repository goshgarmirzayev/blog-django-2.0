from django.urls import path
from post.views import *

app_name = 'post'
urlpatterns = [

    path('/index', post_index, name="index"),
    path('/create', post_create, name="create"),
    path('/<slug:slug>/detail', post_detail, name="detail"),
    path('/<slug:slug>/update', post_update, name="update"),
    path('/<slug:slug>/delete', post_delete, name="delete"),

]
