from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Friend
from .serializers import FriendSerializer


class FriendList(generics.ListCreateAPIView):
    """
    List all friends, i.e. all instances of a user
    friended another user'.
    Create a friend, i.e. follow a user if logged in.
    Perform_create: associate the current logged in user with a friend.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FriendDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a friend
    No Update view, as we either friend or unfriend users
    Destroy a friend, i.e. unfriend someone if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer