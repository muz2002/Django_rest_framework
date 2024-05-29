from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", PostViewSet,basename='posts')


urlpatterns = [
    path("",include(router.urls))
]
    # path("homepage/", homepage, name = 'home_page'),
    # path("list/", PostListCreateView.as_view(), name = 'list'),
    # path("<int:post_id>", post_detail, name = 'post_detail'),
    # path("<int:post_id>", PostRetrieveUpdateDeleteView.as_view(), name = 'post_detail'),
    # path("delete/<int:post_id>",post_delete, name= 'delete')

