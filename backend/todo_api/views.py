from rest_framework import generics, permissions, status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import (
    UserRegistrationSerializer, 
    UserSerializer, 
    TaskSerializer,
    TaskCreateUpdateSerializer
)


class RegisterView(generics.CreateAPIView):
    """
    User registration endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Пользователь успешно зарегистрирован'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    User login endpoint
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({
            'error': 'Необходимо указать имя пользователя и пароль'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': 'Успешный вход в систему'
        })
    else:
        return Response({
            'error': 'Неправильное имя пользователя или пароль'
        }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def user_profile(request):
    """
    Get current user profile
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class TaskListCreateView(generics.ListCreateAPIView):
    """
    List all tasks or create a new task
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['completed', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'updated_at', 'priority']
    ordering = ['-created_at']

    def get_queryset(self):
        """
        Filter tasks by current user
        """
        return Task.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateUpdateSerializer
        return TaskSerializer

    def perform_create(self, serializer):
        """
        Set the user when creating a task
        """
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a task
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filter tasks by current user
        """
        return Task.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return TaskCreateUpdateSerializer
        return TaskSerializer


@api_view(['GET'])
def task_stats(request):
    """
    Get task statistics for current user
    """
    user_tasks = Task.objects.filter(user=request.user)
    
    stats = {
        'total': user_tasks.count(),
        'completed': user_tasks.filter(completed=True).count(),
        'pending': user_tasks.filter(completed=False).count(),
        'by_priority': {
            'high': user_tasks.filter(priority='high').count(),
            'medium': user_tasks.filter(priority='medium').count(),
            'low': user_tasks.filter(priority='low').count(),
        }
    }
    
    return Response(stats)