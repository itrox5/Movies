# A view is just a function

from django.http import HttpResponse
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

data = Movie.objects.all()


def movies (request): #request parameter, first arg call anything you like
    
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


  