# A view is just a function

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movie

#movies Function
# def movies (request): #request parameter, first arg call anything you like
#     return HttpResponse('Hey')

# EXAMPLE 1

# data = {

# 'movies': ['movie3', 'movie4']

# }

# EXAMPLE 2 - Dictionaty (OBJ) with 'movies' key and list (ARRAY) value which contains 3 dictionaries (OBJS) of data. 

# data = {

# 'movies': [
#     {
#         'id': 4,
#          'title': 'Matrix',
#          'yeear': 1999

#     },
#     {
#         'id': 6,
#          'title': 'The Old Gaurd',
#          'yeear': 2022

#     },
#     {
#         'id': 8,
#          'title': 'Termintor',
#          'yeear': 1995

#     }
# ]

# }

# EXAMPLE 3 - in models.py see 'class Movie(models.Model):'




def movies (request): #request parameter, first arg call anything you like
  data = Movie.objects.all()
    
  #OPTION 1 

  # - Accessing movies data directly with '{'movies': ['movie1', 'movie2']}'. This is a dictionary (OBJ) with 'movies' key and a list (array) value.
   #return render(request, 'movies/movies.html', {'movies': ['movie1', 'movie2']})

  # OPTION 2

  # - Accessing data via the 'data' variable in EXAMPLE 1.
  #return render(request, 'movies/movies.html',  data)

  # OPTION 3 

  # - Accessing data via the 'data' variable, in EXAMPLE 2. 
   #return render(request, 'movies/movies.html', data)

  #OPTION 4 
  # - Accessing data via data variable from database 'Movie' model in EXAMPLE 3
  return render(request, 'movies/movies.html', {'movies': data})

      
def home(request):
  return HttpResponse('Home Start')

def detail(request, id):
  data = Movie.objects.get(pk=id)
  return render(request, 'movies/detail.html', {'movie': data})

def add(request):
  title = request.POST.get('title')
  year = request.POST.get('year')

  if title and year:
    movie = Movie(title=title, year=year)
    movie.save()
    return HttpResponseRedirect('/movies')

  return render(request, 'movies/add.html')

def delete(request,id): 
  try:
    movie = Movie.objects.get(pk=id)
  except:
    raise Http404('Movie does not exist')
  movie.delete()
  return HttpResponseRedirect('/movies') #return to page