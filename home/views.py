from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples = [
        {'name':'yuvraj bhalla', 'age':12},
        {'name':'mohit thapa', 'age':45},
        {'name':'paras mahajan', 'age':43},
        {'name':'khushal salwan', 'age':11},
        {'name':'ridhima bhatti', 'age':32}
    ]

    for people in peoples:
        print(people)
   
    return render(request ,"index.html", context = {"peoples": peoples})

def yuvi(request):
    return HttpResponse("https://www.youtube.com/watch?v=ZW2FSxb_VEo&list=PLVBKjEIdL9bvCdI4l1Emvbezv10GjUaLk&index=4")

def about(request):
    return HttpResponse("this is our about page")