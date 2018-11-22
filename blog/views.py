from django.shortcuts import render
from .models import Blog
# Create your views here.
def allblogs(request):
    allblogs = Blog.objects
    return render(request,'blog/allblogs.html',{'allblogs':allblogs})