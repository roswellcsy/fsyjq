"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import api.views as api_views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'campaign/published', api_views.CampaignPublishedViewSet, 'publishedCampaign')
router.register(r'participate/campaign', api_views.MyCampaignViewSet, 'myCampaignlist')
router.register(r'participate/volunteerservice', api_views.MyVolunteerServiceViewSet, 'myVolunteerservice')
router.register(r'training/published', api_views.AbilityTrainingViewSet, 'training')
router.register(r'userinformation', api_views.UserInformationViewSet, 'userinformation')
router.register(r'policyqa', api_views.PolicyQAViewSet, 'policyqa')
router.register(r'professonaladvice', api_views.ProfessionalAdviceViewSet, 'professonaladvice')
router.register(r'volunteerinformation', api_views.VolunteerInformationViewSet, 'volunteerinformation')
# router.register(r'campaignperson', api_views.CampaignPersonViewSet, 'campaignperson')
router.register(r'user', api_views.UserViewSet, 'user')
router.register(r'campaign/signup', api_views.CampaignSignUpViewSet)
router.register(r'volserivce/signup', api_views.VolServiceSignUpViewSet)

# router.register(r'campaign/signup', api_views.CampaignSignupViewSet.as_view())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # url(r'^api/', include('api.url')),
    # POST email=email&password=password
    url(r'^api-register/', api_views.CreateUserView.as_view()),
    url(r'^token-api-auth/login/', obtain_jwt_token),
    url(r'^api-auth', include('rest_framework.urls')),
]
#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
