# coding: utf-8
from rest_framework import viewsets, permissions
from .models import Campaign, User
from .serializers import CampaignSerializer, UserSerializer
from rest_framework import mixins, generics

# Create your views here.

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticated, )


# class UserViewSet(viewsets.ModelViewSet):
class UserViewSet(viewsets.ReadOnlyModelViewSet): # list+ detail
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CreateUserView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
