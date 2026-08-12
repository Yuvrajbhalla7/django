from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login/")
def recipes(request):
    if request.method =="POST":
        data = request.POST
        image = request.FILES.get("image")
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")

        recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            image = image,

        )
    queryset = recipe.objects.all()
    context = {'recipes': queryset}

    return render(request , "recipe.html",context)


def delete_recipe(request ,id):
    queryset = recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes')

def update_recipe(request ,id):
    queryset =recipe.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get("image")
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if image:
            queryset.image = image
        queryset.save()
        return redirect('/recipes/')

    context ={ 'recipe':queryset}
    
    return render(request, 'update.html',context)


def login_page(request ):
        if request.method == "POST":
             username = request.POST.get('username')
             password = request.POST.get('password')

             if not User.objects.filter(username = username).exists():
                 messages.error(request,"invalid username")
                 return redirect('/login/')
             user = authenticate(username =username ,password = password)

             if user is None:
                 messages.error(request ,"invalid password")
                 return redirect('/login/')
             else:
                 login(request ,user)
                 return redirect('/recipes/')
                 
             
        return render(request , "login.html")

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username =  username )
        if user.exists():
            messages.info(request,'username already exist!')
            return redirect('/register/')

        user = User.objects.create(
            first_name = firstname,
            last_name = lastname,
            username =username,
           
        )
        user.set_password(password)
        user.save()
        messages.info(request,' account created sucessfully!')

        

        return redirect( '/register/')
    return render(request , "register.html")