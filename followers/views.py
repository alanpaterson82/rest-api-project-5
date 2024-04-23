from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import follow
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of a user
    followed another user'.
    Create a follow, i.e. follow a user if logged in.
    Perform_create: associate the current logged in user with a follow.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = follow.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class followDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follow
    No Update view, as we either follow or unfollow users
    Destroy a follow, i.e. unfollow someone if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = follow.objects.all()
    serializer_class = FollowerSerializer