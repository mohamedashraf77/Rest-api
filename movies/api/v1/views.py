from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer
from movies.models import Movie


class UserCanDelete(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="can-delete").exists()

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def movies_index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def movie_index(request, id):
    movies = Movie.objects.filter(pk=id)
    if movies.exists():
        movie = movies.first()
        serializer = MovieSerializer(instance=movie)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(data={"message":"Movie dosn't exist"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_movie(request):
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message":"done"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([UserCanDelete])
def delete_movie(request, id):
    try:
        movie = Movie.objects.get(pk=id)
        movie = movie.delete()
        return Response(data={"message": "done"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','PATCH'])
def update_movie(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except Exception as e:
        return Response(data={"message": e}, status=status.HTTP_400_BAD_REQUEST)
    serializer = None
    if request.method == 'PUT':
        serializer = MovieSerializer(instance=movie, data= request.data)
    elif request.method == 'PATCH':
        serializer = MovieSerializer(instance=movie, data= request.data, partial= True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
