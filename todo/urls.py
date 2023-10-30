from django.urls import path
from .views import IndexView, CreateTodoView, ActionView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create/", CreateTodoView.as_view(), name="create"),
    path("<int:todo_id>/<str:action>/action/", ActionView.as_view(), name="action")
]