from django.shortcuts import render ,redirect,get_object_or_404,reverse
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def index(req):
    todos=Todo.objects.all()
    print(todos)
    return render(req,template_name="todos/base.html",context={"todos":todos})
    # return HttpResponse("<h1>Hello World</h1>")
def createTodo(req):
    if req.method=="GET":
        return render(req,template_name="todos/form.html")
    if req.method=="POST":
        todo=req.POST["todo"]
        Todo.objects.create(todo=todo)
        print(todo)
        return redirect("/")
def updateTodo(req,id):
    todo=get_object_or_404(Todo,ok=id)
    if req.method=="GET":
        return render(req,template_name="todos/update")
    if req.method=="POST":
        
    
        
    
        return HttpResponse("Hello"+str(id))
    