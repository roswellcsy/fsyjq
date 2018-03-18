# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import User, Campaign, PolicyQA, ProfessionalAdvice, VolunteerInformation, AbilityTraining, SingleUploadImg, UserInformation, VolunteerInformation 
import datetime

# 多对多需要嵌套，下方是例子
"""
嵌套序列化关系模型
在序列化模型中指定嵌套序列化关系模型将返回一个该嵌套序列化关系模型对应的数据模型中序列化的数据。
读起来有些拗口，看例子吧。

参数：

many 如果应用于多对多关系，则应将此参数设置为 True
序列化模型如下

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('order', 'title', 'duration')

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')
序列化结果如下：

 {
    'album_name': 'The Grey Album',
    'artist': 'Danger Mouse',
    'tracks': [
        {'order': 1, 'title': 'Public Service Announcement', 'duration': 245},
        {'order': 2, 'title': 'What More Can I Say', 'duration': 264},
        {'order': 3, 'title': 'Encore', 'duration': 159},
    ],
}
"""


class UserSerializer(serializers.ModelSerializer):

    # policyqas = serializers.PrimaryKeyRelatedField(queryset=PolicyQA.objects.all())
    """
    说明:只保留最基础的数据，外链数据一律不能加，否则会出问题
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            # cellphone=validated_data['cellphone'],
            # email=validated_data['email'],
            # policyqas=validated_data['policyqas']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserInformationSerializer(serializers.ModelSerializer):

    # person = serializers.SlugRelatedField(
    #     slug_field=User.USERNAME_FIELD, queryset=User.objects.all())
    user_information_user = UserSerializer(read_only=True)
    user_information_user_id = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all(), source='user_information_user')

    class Meta:
        model = UserInformation
        fields = (
            'id',
            'user_information_user_id',
            'user_information_user',
            'user_information_name',
            'user_information_sex',
            'user_information_cellphone',
            'user_information_email',
            'user_information_volunteer'
            )

# 志愿者信息
class VolunteerInformationSerializer(serializers.ModelSerializer):

    # slug_field是以外键的某个值作为关联
    # volinfo_user = serializers.SlugRelatedField(
    #     slug_field=User.USERNAME_FIELD, queryset=User.objects.all())
    volinfo_user = UserSerializer(read_only=True)
    volinfo_user_id = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all(), source='volinfo_user')

    class Meta:
        model = VolunteerInformation
        fields = (
            'id',
            # 'volinfo_name',
            # 'volinfo_sex',
            # 'volinfo_age',
            'volinfo_jiguan',
            'volinfo_live_address',
            'volinfo_marriage',
            'volinfo_idcard_type',
            'volinfo_id_num',
            'volinfo_birthday',
            # 'volinfo_email',
            'volinfo_graduate_school',
            'volinfo_graduate_date',
            'volinfo_education',
            'volinfo_profession',
            'volinfo_employer',
            'volinfo_position',
            'volinfo_mail_address',
            'volinfo_zipcode',
            'volinfo_contact_number',
            # 'volinfo_cellphone',
            'volinfo_service_area',
            'volinfo_service_date',
            'volinfo_skills',
            'volinfo_service_time',
            'volinfo_user',
            'volinfo_user_id'
        )

class CampaignPhotosSerializer(serializers.ModelSerializer):

    # person = serializers.SlugRelatedField(
    #     slug_field=User.USERNAME_FIELD, queryset=User.objects.all())

    class Meta:
        model = SingleUploadImg
        fields = (
            'id',
            'campaign_or_service_name',
            'photo_name',
            'photo_path',
            )

# 公开公益活动清单
class CampaignPublishedSerializer(serializers.ModelSerializer):

    # person = serializers.SlugRelatedField(
    #     slug_field=User.USERNAME_FIELD, queryset=User.objects.all())
    photos = CampaignPhotosSerializer(many=True, read_only=True)
    campaign_members = UserSerializer(many=True, read_only=True)
    campaign_volunteers = UserSerializer(many=True, read_only=True)
    # campaign_members_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.all(), source='campaign_members')
    # campaign_volunteers_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.all(), source='campaign_volunteers')

    class Meta:
        model = Campaign
        fields = (
            'id',
            'campaign_name',
            'campaign_type',
            'campaign_date',
            'campaign_date',
            'campaign_client',
            'campaign_address',
            'campaign_content',
            'campaign_paid',
            'campaign_signup_deadline',
            'campaign_contact',
            'campaign_certified_hours',
            'campaign_counts',
            'campaign_vol_counts',
            'photos',
            'campaign_members',
            'campaign_volunteers'
            )
        read_only_fields = (
            'id',
            'campaign_name',
            'campaign_type',
            'campaign_date',
            'campaign_date',
            'campaign_client',
            'campaign_address',
            'campaign_content',
            'campaign_paid',
            'campaign_signup_deadline',
            'campaign_contact',
            'campaign_certified_hours',
            'campaign_counts',
            'campaign_vol_counts',
            'photos',
            'campaign_members',
            'campaign_volunteers'
        )
    
    # def update(self, instance, validated_data):

    #     # ...
    #     validated_data['campaign_members'] = filter(None, validated_data['campaign_members'])
    #     for campaign_member in validated_data['campaign_members']:
    #         # user = User.objects.get(pk=campaign_members_id)
    #         instance.campaign_members.add(campaign_member)
    #     validated_data['campaign_volunteers'] = filter(None, validated_data['campaign_volunteers'])
    #     for campaign_volunteer in validated_data['campaign_volunteers']:
    #         # user = User.objects.get(pk=campaign_members_id)
    #         instance.campaign_volunteers.add(campaign_volunteer)

    #     return instance

class CampaignSignUpSerializer(serializers.ModelSerializer):
    campaign_members = UserSerializer(many=True, read_only=True)
    campaign_members_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.all(), source='campaign_members')

    class Meta:
       model = Campaign
       fields = (
           'id',
           'campaign_members',
           'campaign_members_ids',
           )
       read_only_fields = (
           'id',
       )
    
    def update(self, instance, validated_data):

        # ...
        validated_data['campaign_members'] = filter(None, validated_data['campaign_members'])
        for campaign_member in validated_data['campaign_members']:
            # user = User.objects.get(pk=campaign_members_id)
            instance.campaign_members.add(campaign_member)

        return instance


class VolServiceSignUpSerializer(serializers.ModelSerializer):
    campaign_volunteers = UserSerializer(many=True, read_only=True)
    campaign_volunteers_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.all(), source='campaign_volunteers')

    class Meta:
       model = Campaign
       fields = (
           'id',
           'campaign_volunteers',
           'campaign_volunteers_ids'
           )
       read_only_fields = (
           'id',
       )
    
    def update(self, instance, validated_data):

        # ...
        validated_data['campaign_volunteers'] = filter(None, validated_data['campaign_volunteers'])
        for campaign_volunteer in validated_data['campaign_volunteers']:
            # user = User.objects.get(pk=campaign_members_id)
            instance.campaign_volunteers.add(campaign_volunteer)

        return instance


# 个人报名公益活动（志愿服务）清单
class MyParticipateSerializer(serializers.ModelSerializer):

    # person = serializers.SlugRelatedField(
    #     slug_field=User.USERNAME_FIELD, queryset=User.objects.all())
    photos = CampaignPhotosSerializer(many=True)
    campaign_members = UserSerializer(many=True)
    # campaign_members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    campaign_volunteers = UserSerializer(many=True)

    class Meta:
        model = Campaign
        fields = (
            'campaign_name',
            'campaign_type',
            'campaign_date',
            'campaign_date',
            'campaign_client',
            'campaign_address',
            'campaign_content',
            'campaign_paid',
            'campaign_signup_deadline',
            'campaign_contact',
            'campaign_certified_hours',
            'campaign_counts',
            'campaign_vol_counts',
            'photos',
            'campaign_members',
            'campaign_volunteers'
            )

# 专业咨询
class ProfessionalAdviceSerializer(serializers.ModelSerializer):

    # slug_field是以外键的某个值作为关联
    proadv_user = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, queryset=User.objects.all())
    class Meta:
        model = ProfessionalAdvice
        fields = (
            'id',
            'proadv_question_title',
            'proadv_question_type',
            'proadv_question_content',
            'proadv_full_name',
            'proadv_sex',
            'proadv_age',
            'proadv_house_hold',
            'proadv_id_num',
            'proadv_ethnic',
            'proadv_political_status',
            'proadv_religion',
            'proadv_occupation',
            'proadv_studying_grade',
            'proadv_degree_of_education',
            'proadv_community',
            'proadv_contact',
            'proadv_live_address',
            'proadv_marriage',
            'proadv_user',
            'proadv_serv_date',
            'proadv_serv_content'
        )
        # extra_kwargs = {'password': {'write_only': True}}
# 政策咨询
class PolicyQASerializer(serializers.ModelSerializer):

    # slug_field是以外键的某个值作为关联
    qa_user = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, queryset=User.objects.all())
    class Meta:
        model = PolicyQA
        fields = (
            'id',
            'qa_fullname',
            'qa_sex',
            'qa_age',
            'qa_live_area',
            'qa_cellphone',
            'qa_occupation',
            'qa_marriage',
            'qa_title',
            'qa_type',
            'qa_content',
            'qa_o2o',
            'qa_ask_date',
            'qa_answer',
            'qa_answer_date',
            'qa_user'
        )


# 活动报名人信息
# class CampaignPersonSerializer(serializers.ModelSerializer):

#     # slug_field是以外键的某个值作为关联
#     campaign_person_user = serializers.SlugRelatedField(
#         slug_field=User.USERNAME_FIELD, queryset=User.objects.all())
#     class Meta:
#         model = CampaignPerson
#         fields = (
#             'id',
#             'campaign_person_name',
#             'campaign_person_sex',
#             'campaign_person_cellphone',
#             'campaign_person_user'
#         )

class AbilityTrainingSerializer(serializers.ModelSerializer):

    # slug_field是以外键的某个值作为关联
    volunteers = UserSerializer(many=True, read_only=True)
    volunteers_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.all(), source='volunteers')

    class Meta:
        model = AbilityTraining
        fields = (
            'id',
            'at_zhu_jiang_ren',
            'at_theme',
            'at_date',
            'at_content',
            'at_address',
            'at_counts',
            'at_sign_up_deadline',
            'volunteers',
            'volunteers_ids'
        )
        read_only_fields = (
            'id',
            'at_zhu_jiang_ren',
            'at_theme',
            'at_date',
            'at_content',
            'at_address',
            'at_counts',
            'at_sign_up_deadline',
        )

    def update(self, instance, validated_data):

        # ...
        validated_data['volunteers'] = filter(None, validated_data['volunteers'])
        for volunteer in validated_data['volunteers']:
            # user = User.objects.get(pk=campaign_members_id)
            instance.volunteers.add(volunteer)

        return instance