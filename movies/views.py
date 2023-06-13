# A view is just a function

from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

#movies Function
# def movies (request): #request parameter, first arg call anything you like
#     return HttpResponse('Hey')

# Example 1
# data = {

# 'movies': ['movie1', 'movie2']

# }

# Example 2

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

def movies (request): #request parameter, first arg call anything you like
    
  #OPTION 1 adding movies data directly 
  #return render(request, 'movies/movies.html', {'movies': ['movie1', 'movie2']})

  # FOR DATA VARIABLES VERSIONS 1 AND 2 
  # OPTION 2 Adding movies data by data variable via example 1 list or example 2 list and dictionaries
  #return render(request, 'movies/movies.html', data)

  #OPTION 3 adding movies data by data variable from database model
  data = Movie.objects.all()
  return render(request, 'movies/movies.html', {'movies': data})

        

def home (request):
  return HttpResponse('Home Start')


  