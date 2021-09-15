from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('categories', views.CategoriesViewSet, basename='categories')
router.register('genres', views.GenresViewSet, basename='genres')
router.register('titles', views.TitlesViewSet, basename='titles')
router.register('titles/(?P<title_id>[^/.]+)/reviews', views.ReviewsViewSet, basename='reviews')
router.register('titles/(?P<title_id>[^/.]+)/reviews/(?P<review_id>[^/.]+)/comments', views.CommentsViewSet, basename='comments')
router.register('users', views.UserViewSet, basename='users')



urlpatterns = [
    path('users/me/', views.Profile.as_view(), name='profile'),
    path('', include(router.urls)),
    

]