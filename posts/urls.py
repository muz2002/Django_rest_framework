from django.urls import path
from .views import *

urlpatterns = [
    path("homepage/", homepage, name = 'home_page'),
    path("list/", PostListCreateView.as_view(), name = 'list'),
    # path("<int:post_id>", post_detail, name = 'post_detail'),
    path("<pk>", PostRetrieveUpdateDeleteView.as_view(), name = 'post_detail'),
    # path("delete/<int:post_id>",post_delete, name= 'delete')
]