from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    item_list = Todo.objects.order_by("-date")
    page = {
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/home.html', page)

class PostCreateView(CreateView):
    model = Todo
    fields = ['title', 'details']  
    success_url = reverse_lazy('todo')
    
    def form_valid(self, form):
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'details']  
    template_name = 'todo/edit_todo.html'
    success_url = reverse_lazy('todo')
    
    def form_valid(self, form):
        return super().form_valid(form)
  
    
### function to remove item, it receive todo item_id as primary key from url ##
class PostDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo')
    
def favorites(request):
    todos = Todo.objects.all()  # Fetch all todos (filtering happens in JS)
    return render(request, 'todo/favorite.html', {'todos': todos})