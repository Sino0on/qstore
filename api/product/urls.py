from django.urls import path
from .views import *


urlpatterns = [
    path('goods/', ProductListView.as_view()),
    path('good/<int:pk>', ProductDetailView.as_view()),
    path('like/<int:pk>', LikeUserView.as_view()),
    path('goodlistcreate/', ProductListCreateView.as_view()),
]