# from django.http import JsonResponse
# from django.shortcuts import render
# from watchlist_app.models import Movie

# # Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values())
#     }

#     return JsonResponse(data)
    
# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'active': movie.active,
#         'description': movie.description
#     }
#     return JsonResponse(data)