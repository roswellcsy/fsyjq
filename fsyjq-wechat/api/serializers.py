# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import User, Campaign, PolicyQA, ProfessionalAdvice, CampaignPerson, VolunteerInformation, AbilityTraining
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
        fields = ('id', 'username', 'cellphone','email', 'last_login', 'is_admin', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            cellphone=validated_data['cellphone'],
            email=validated_data['email'],
            # policyqas=validated_data['policyqas']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CampaignSerializer(serializers.ModelSerializer):

    # person = serializers.SlugRelatedField(
    #     slug_field=User.USERNAME_FIELD, queryset=User.objects.all())

    class Meta:
        model = Campaign
        fields = ('campaign_name', 'campaign_type', 'campaign_date')

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
            'proadv_user'
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

# 志愿者信息
class VolunteerInformationSerializer(serializers.ModelSerializer):

    # slug_field是以外键的某个值作为关联
    volinfo_user = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, queryset=User.objects.all())
    class Meta:
        model = VolunteerInformation
        fields = (
            'id',
            'volinfo_name',
            'volinfo_sex',
            'volinfo_age',
            'volinfo_jiguan',
            'volinfo_live_address',
            'volinfo_marriage',
            'volinfo_idcard_type',
            'volinfo_id_num',
            'volinfo_birthday',
            'volinfo_email',
            'volinfo_graduate_school',
            'volinfo_graduate_date',
            'volinfo_education',
            'volinfo_profession',
            'volinfo_employer',
            'volinfo_position',
            'volinfo_mail_address',
            'volinfo_zipcode',
            'volinfo_contact_number',
            'volinfo_cellphone',
            'volinfo_service_area',
            'volinfo_service_date',
            'volinfo_skills',
            'volinfo_user'
        )

# 活动报名人信息
class CampaignPersonSerializer(serializers.ModelSerializer):

    # slug_field是以外键的某个值作为关联
    campaign_person_user = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, queryset=User.objects.all())
    class Meta:
        model = CampaignPerson
        fields = (
            'id',
            'campaign_person_name',
            'campaign_person_sex',
            'campaign_person_cellphone',
            'campaign_person_user'
        )