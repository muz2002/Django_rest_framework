from django.urls import path
from .views import *

urlpatterns = [
    path("homepage/", homepage, name = 'home_page'),
    path("list/", list_posts, name = 'list'),
    path("<int:post_id>", post_detail, name = 'post_detail'),
    path("update/<int:post_id>", update_post, name = 'update'),
    path("delete/<int:post_id>",post_delete, name= 'delete')
]