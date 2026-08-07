from django.shortcuts import render
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
            recipe_description =recipe_description,
            image = image,
        )
    return render(request , "recipe.html") 