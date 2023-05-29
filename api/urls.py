from django.urls import path
from api.views import MyApiView

urlpatterns = [
    path('view/list', MyApiView.as_view()),
    path('view/list/<int:postId>', MyApiView.as_view()),
]
