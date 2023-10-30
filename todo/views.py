from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Todo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

class IndexView(LoginRequiredMixin, View):
    login_url="login"
    def get(self, request):
        categories = Category.objects.filter(user=request.user)
        return render(request, "index.html", {"categories":categories})
    
class CreateTodoView(LoginRequiredMixin, View):
    def post(self, request):
        body = request.POST.get("body")
        category_id = request.POST.get("id")
        category = Category.objects.filter(id=category_id).first()
        if body and category:
            Todo.objects.create(user=request.user, body=body, category=category)
        return redirect("index")
    

class ActionView(LoginRequiredMixin, View):
    def post(self, request, todo_id, action):
        todo = Todo.object.filter(id=todo_id, user=request.user).first()
        if todo:
            if action == "done":
                todo.done = True
                todo.save()
            elif action == "delete":
                todo.delete()
        return redirect("index")