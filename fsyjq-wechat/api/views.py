# coding: utf-8
from rest_framework import viewsets, permissions
from .models import Campaign, User, PolicyQA, ProfessionalAdvice, VolunteerInformation, CampaignPerson
from .serializers import CampaignSerializer, UserSerializer, PolicyQASerializer, ProfessionalAdviceSerializer, VolunteerInformationSerializer, CampaignPersonSerializer
from rest_framework import mixins, generics

# Create your views here.

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticated, )

class CampaignPersonViewSet(viewsets.ModelViewSet):
    # queryset = PolicyQA.objects.all()
    serializer_class = CampaignPersonSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        """
        重写get_queryset，只返回username参数的咨询，其他viewset类似
        """
        queryset = CampaignPerson.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(campaign_person_user__username=username)
        return queryset

class VolunteerInformationViewSet(viewsets.ModelViewSet):
    # queryset = PolicyQA.objects.all()
    serializer_class = VolunteerInformationSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        """
        重写get_queryset，只返回username参数的咨询，其他viewset类似
        """
        queryset = VolunteerInformation.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(volinfo_user__username=username)
        return queryset

class ProfessionalAdviceViewSet(viewsets.ModelViewSet):
    # queryset = PolicyQA.objects.all()
    serializer_class = ProfessionalAdviceSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        """
        重写get_queryset，只返回username参数的咨询，其他viewset类似
        """
        queryset = ProfessionalAdvice.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(proadv_user__username=username)
        return queryset


class PolicyQAViewSet(viewsets.ModelViewSet):
    # queryset = PolicyQA.objects.all()
    serializer_class = PolicyQASerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        """
        重写get_queryset，只返回username参数的咨询，其他viewset类似
        """
        queryset = PolicyQA.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(qa_user__username=username)
        return queryset

# class UserViewSet(viewsets.ModelViewSet):
class UserViewSet(viewsets.ModelViewSet): # list+ detail
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        """
        重写get_queryset，只返回与用户名一致的信息
        """
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset


class CreateUserView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
