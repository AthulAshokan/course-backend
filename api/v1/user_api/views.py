from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer


class RegisterUserView(APIView):  
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def register_user(request):
#     serializer = UserRegistrationSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         access_token = str(refresh.access_token)

#         return Response(
#             {
#                 'detail': f'{role_name.capitalize()} registered successfully!',
#                 'user_id': user.id,
#                 'access_token': access_token,
#                 'refresh_token': str(refresh),
#             },
#             status=status.HTTP_201_CREATED
#         )
#     else:
#         print(f"Serializer errors: {serializer.errors}")
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response(
                {
                    'detail': f'{role_name.capitalize()} registered successfully!',
                    'user_id': user.id,
                    'access_token': access_token,
                    'refresh_token': str(refresh),
                },
                status=status.HTTP_201_CREATED
            )
        else:
            print(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)