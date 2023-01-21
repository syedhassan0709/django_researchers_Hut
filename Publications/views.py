from django.shortcuts import render
from .models import Field
from . models import Year,Publication
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request,'Publications/index.html')


def publications_level(request):
    level = Field.objects.all()
    year = Year.objects.all()
    context = {'level' : level,'year':year}
    return render(request,'Publications/publication_level.html',context)

def publications_all(request,level_id):
    level = Field.objects.get(id=level_id)
    publications = level.publication_set.order_by('year_id')
    year = Year.objects.all()
    context = {'level':level,'publications':publications,'year':year}
    return render(request,'Publications/publication_articles.html',context)

def search(request):
    author1 = request.GET['author']
    title1 = request.GET['title']
    search_result = Publication.objects.filter(author__icontains=author1)
    if title1 == "":
        search_result = Publication.objects.filter(author__icontains=author1)
    if author1 == "":
        search_result = Publication.objects.filter(title__icontains=title1)
    if title1 != "" and author1 != "":
        search_result = Publication.objects.filter(title__icontains=title1).filter(author__icoontains=author1)   
    context= {'search_result':search_result}
    return render(request,'Publications/search_result.html',context)

def aboutus(request):
    return render(request,'Publications/aboutus.html')


