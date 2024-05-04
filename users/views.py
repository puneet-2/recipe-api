from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from recipe.models import Recipe
from .models import Profile
from recipe.serializers import RecipeSerializer
from . import serializers
# recipe/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_notification_email  # Importing the Celery task

def my_view(request):
    # Your view logic here
    subject = 'Notification Subject'
    message = 'Notification Message'
    recipient_list = ['recipient@example.com']

    # Call the Celery task
    send_notification_email.delay(subject, message, recipient_list)

    return HttpResponse('Email notification sent asynchronously.')


User = get_user_model()


class UserRegisterationAPIView(GenericAPIView):
    """
    An endpoint for the client to create a new User. 
    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserRegisterationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['tokens'] = {
            'refresh': str(token),
            'access': str(token.access_token)
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = serializers.CustomUserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['tokens'] = {
            'refresh': str(token),
            'access': str(token.access_token)
        }
        return Response(data, status=status.HTTP_200_OK)


class UserLogoutAPIView(GenericAPIView):
    """
    An endpoint to logout users.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user information
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CustomUserSerializer

    def get_object(self):
        return self.request.user


class UserProfileAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user profile
    """
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile


class UserAvatarAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user avatar
    """
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileAvatarSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile


class UserBookmarkAPIView(ListCreateAPIView):
    """
    Get, Create, Delete favorite recipe
    """
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)
    profile = Profile.objects.all()

    def get_queryset(self):
        user = User.objects.get(id=self.kwargs['pk'])
        user_profile = get_object_or_404(self.profile, user=user)
        return user_profile.bookmarks.all()

    def post(self, request, pk):
        user = User.objects.get(id=pk)
        user_profile = get_object_or_404(self.profile, user=user)
        recipe = Recipe.objects.get(id=request.data['id'])
        if user_profile:
            user_profile.bookmarks.add(recipe)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user_profile = get_object_or_404(self.profile, user=user)
        recipe = Recipe.objects.get(id=request.data['id'])
        if user_profile:
            user_profile.bookmarks.remove(recipe)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeAPIView(UpdateAPIView):
    """
    Change password view for authenticated user
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PasswordChangeSerializer

    def get_object(self):
        return self.request.user
# recipe/views.py

import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def my_view(request):
    logger.info('This is an info message.')
    logger.error('This is an error message.')
    # Your view logic here
    return HttpResponse('View response')
from rest_framework import viewsets, pagination
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    pagination_class = YourModelPagination

