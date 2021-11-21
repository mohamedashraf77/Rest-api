from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def signup(request):
    data = {}
    serializer = UserSerializer(data= request.data)
    print(request.data)
    if serializer.is_valid():
     serializer.save()
     return Response(data={"message": "done"}, status=status.HTTP_201_CREATED)
    else:
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        request.user.auth_token.delete()
        return Response(data={"message": "done"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(data={"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
