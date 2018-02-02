# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import User, Campaign, PolicyQA
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
        fields = ('title', 'person', 'date')

# 政策咨询
class PolicyQASerializer(serializers.ModelSerializer):

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
        # extra_kwargs = {'password': {'write_only': True}}