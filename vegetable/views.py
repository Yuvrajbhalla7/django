from django.shortcuts import render,redirect
from .models import *

# Create your views here.
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