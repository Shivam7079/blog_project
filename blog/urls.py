from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    home,
    register,
    create_post,
    edit_post,
    delete_post,
    add_comment,
    like_post,
    profile,
    edit_profile
)

from .api_views import (
    PostViewSet,
    CommentViewSet,
    ProfileViewSet
)


# REST API Router
router = DefaultRouter()

router.register(
    'posts',
    PostViewSet
)

router.register(
    'comments',
    CommentViewSet
)

router.register(
    'profiles',
    ProfileViewSet
)


urlpatterns = [

    # Website URLs
    path('', home, name='home'),

    path('register/', register, name='register'),

    path('create/', create_post, name='create_post'),

    path('edit/<int:id>/', edit_post, name='edit_post'),

    path('delete/<int:id>/', delete_post, name='delete_post'),

    path('comment/<int:id>/', add_comment, name='add_comment'),

    path('like/<int:id>/', like_post, name='like_post'),

    path('profile/', profile, name='profile'),

    path('profile/edit/', edit_profile, name='edit_profile'),

    # REST API URLs
    path('api/', include(router.urls)),

]