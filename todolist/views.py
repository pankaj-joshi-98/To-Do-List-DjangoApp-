from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    my_context = {
        'all_items':all_todo_items,
    }
    return render(request, "todo.html", my_context)

def addTodo(request):
    #creating a new todo all_items    
    new_item = TodoItem(content = request.POST['content'])
    #saving the new_item in the database
    new_item.save()
    #redirect the browwser to '/todo/'
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id): 
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()      
    return HttpResponseRedirect('/todo/')

