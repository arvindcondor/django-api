from django.urls import path
from api.views import MyApiView

urlpatterns = [
    path('view/list', MyApiView.as_view()),
    path('view/list/<int:id>/', MyApiView.as_view()),
    # path('view/post/', MyApiView.as_view()),

]
