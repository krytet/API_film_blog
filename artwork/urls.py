from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoriesViewSet,
    GenresViewSet,
    TitlesViewSet,
    ReviwsViewSet,
    CommentsViewSet
)

router = DefaultRouter()
router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')
router.register('titles', TitlesViewSet, basename='titles')
router.register('reviews', ReviwsViewSet, basename='reviews')
router.register('comments', CommentsViewSet, basename='comments')



urlpatterns = [
    path('', include(router.urls))

]