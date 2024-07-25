from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import TodoItems

def TodoLists(request):
    if request.method == 'POST' :
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TodoForm()
    
    todo_items = TodoItems.objects.all()
    return render(request, 'index.html', {'form' : form, 'todo_items' : todo_items} )

def success(request):
    return render(request, 'success.html')

def EditTodoItem(request, pk):
    todo_item = get_object_or_404(TodoItems, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('todolist')
    else:
        form = TodoForm(instance=todo_item)
    return render(request, 'edit.html', {'form': form, 'todo_item' : todo_item})

def DeleteTodoItem(request, pk):
    todo_item = get_object_or_404(TodoItems, pk=pk)
    if request.method == 'POST':
        todo_item.delete()
        return redirect('todolist')
    return render(request, 'delete.html', {'todo_item': todo_item})