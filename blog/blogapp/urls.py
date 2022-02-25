
from django.urls import path
from .views import Homeview, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AboutSectionView

urlpatterns = [
    path('',Homeview.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('newpost/', AddPostView.as_view(), name="newpost"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(),name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(),name='delete_post'),
    path('about/',AboutSectionView.as_view(), name="about"),

]
