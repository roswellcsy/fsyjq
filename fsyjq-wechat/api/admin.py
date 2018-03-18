# coding: utf-8


from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from api.models import User, PolicyQA, ProfessionalAdvice, SingleUploadImg, Campaign, UserInformation, VolunteerInformation, AbilityTraining


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('密码不正确')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean_password(self):
        return self.initial['password']

class UserInformationInline(admin.StackedInline):
    model = UserInformation
    readonly_fields = ('user_information_volunteer',)
    verbose_name = '用户信息'
    extra = 0

class VolunteerInformationInline(admin.StackedInline):
    model = VolunteerInformation
    verbose_name = '志愿者信息'
    extra = 0

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    

    list_display = ('username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('last_login',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'last_login', 'password1', 'password2')}
         ),
    )
    # search_fields = ('cellphone',)
    # ordering = ('cellphone',)
    filter_horizontal = ()
    inlines = (UserInformationInline, VolunteerInformationInline)


# Now register the new UserAdmin
# admin.site.unregister(UserAdmin)
# admin.site.register(UserInformation)
admin.site.register(User, UserAdmin)

# admin.site.unregister(Group)


class PolicyQAAdmin(admin.ModelAdmin):
    readonly_fields = ['qa_user', 'qa_fullname', 'qa_sex', 'qa_age', 'qa_live_area', 'qa_cellphone', 
                        'qa_occupation', 'qa_marriage', 'qa_ask_date', 'qa_title', 'qa_type', 'qa_content',
                        'qa_o2o', 'qa_ask_date']
    fieldsets = [
        ('咨询人信息', {'fields': [
         'qa_user', 'qa_fullname', 'qa_sex', 'qa_age', 'qa_live_area', 'qa_cellphone', 'qa_occupation', 'qa_marriage']}),
        ('咨询内容', {'fields': ['qa_title', 'qa_type', 'qa_content',
                             'qa_o2o', 'qa_ask_date']}),
        # 以上为前端填写内容
        ('答复内容', {'fields': [
         'qa_answer', 'qa_answer_date']}),
    ]
    list_display = ('qa_title', 'qa_type', 'qa_fullname',
                    'qa_o2o', 'qa_status')


admin.site.register(PolicyQA, PolicyQAAdmin)


class ProfessionalAdviceAdmin(admin.ModelAdmin):
        # readonly_fields = ['user_subscribe_time', 'nickname', 'user_city',
    #                    'user_country', 'user_province', 'user_language',
    #                    'user_subscribe_time']
    readonly_fields = [
        'proadv_user', 'proadv_question_type', 'proadv_question_title', 'proadv_question_content',
        'proadv_full_name', 'proadv_sex', 'proadv_age',
        'proadv_house_hold', 'proadv_id_num', 'proadv_ethnic', 'proadv_political_status',
        'proadv_religion', 'proadv_occupation', 'proadv_studying_grade', 'proadv_degree_of_education',
        'proadv_community', 'proadv_contact', 'proadv_live_address', 'proadv_marriage',                               
    ]
    fieldsets = [
        ('初始信息', {'fields': [
         'proadv_user', 'proadv_question_type', 'proadv_question_title', 'proadv_question_content']}),
        ('服务对象基本信息', {'fields': ['proadv_full_name', 'proadv_sex', 'proadv_age',
                                 'proadv_house_hold', 'proadv_id_num', 'proadv_ethnic', 'proadv_political_status',
                                 'proadv_religion', 'proadv_occupation', 'proadv_studying_grade', 'proadv_degree_of_education',
                                 'proadv_community', 'proadv_contact', 'proadv_live_address', 'proadv_marriage',
                                 ]}),
        # 以上为前端填写内容
        ('个案基本信息', {'fields': [
         'proadv_from', 'proadv_rescue_methods', 'proadv_social_rescue', 'proadv_result']}),
        ('负责方信息', {'fields': ['proadv_sw_name',
                              'proadv_case_id', 'proadv_date']}),
        ('咨询记录', {'fields': ['proadv_serv_date', 'proadv_serv_time', 'proadv_serv_localtion',
                             'proadv_serv_counts', 'proadv_serv_type', 'proadv_serv_content']}),
        ('个案状态', {'fields': ['proadv_status']}),
    ]
    list_display = ('proadv_full_name', 'proadv_question_type', 'proadv_contact',
                    'proadv_sw_name', 'proadv_sex', 'status')
    # 遗留问题:想要在详细信息里列出姓名、性别和联系方式，因为不是field，会出错


admin.site.register(ProfessionalAdvice, ProfessionalAdviceAdmin)

admin.site.register(SingleUploadImg)

class CampaignPhotosInline(admin.TabularInline):
    verbose_name = '活动照片'
    verbose_name_plural = '活动照片'
    # fieldsets = [
    #     (
    #         None,
    #         {
    #             'fields': ('campaign_person_name', 'campaign_person_sex', 'campaign_person_cellphone')
    #         }
    #     )
    # ]
    model = Campaign.photos.through
    # model = CampaignPerson
    extra = 1 #默认显示条目的数量


class CampaignMemberInline(admin.TabularInline):
    verbose_name = '报名人员清单'
    verbose_name_plural = '报名人员清单'
    model = Campaign.campaign_members.through
    # model = CampaignPerson
    extra = 1 #默认显示条目的数量


class CampaignVolunteerInline(admin.TabularInline):
    verbose_name = '报名志愿者清单'
    verbose_name_plural = '报名志愿者清单'
    model = Campaign.campaign_volunteers.through
    # model = CampaignPerson
    extra = 1 #默认显示条目的数量


class CampaignAdmin(admin.ModelAdmin):
    # readonly_fields = ['user_subscribe_time', 'nickname', 'user_city',
    #                    'user_country', 'user_province', 'user_language',
    #                    'user_subscribe_time']
    inlines = [CampaignPhotosInline, CampaignMemberInline, CampaignVolunteerInline]
    fieldsets = [
        ('活动信息', {'fields': ['campaign_name', 'campaign_type', 'campaign_date', 'campaign_signup_deadline', 'campaign_client', 'campaign_address',
                             'campaign_content', 'campaign_paid',
                             'campaign_contact', 'campaign_certified_hours', 'campaign_counts', 'campaign_vol_counts']}),
        # ('报名人选', {'fields': ['signup_user_list']}),
        # ('报名人', {'fields': ['campaign_person']})
    ]
    list_display = ('campaign_name', 'campaign_type', 'campaign_date',
                    'campaign_signup_deadline', 'campaign_counts', 'campaign_vol_counts')
           


admin.site.register(Campaign, CampaignAdmin)

# admin.site.register(CampaignPerson)

# class VolunteerInformationAdmin(admin.ModelAdmin):
#         # readonly_fields = ['user_subscribe_time', 'nickname', 'user_city',
#     #                    'user_country', 'user_province', 'user_language',
#     #                    'user_subscribe_time']
#     readonly_fields = []
#     fieldsets = [
#         ('志愿者基本信息', {'fields': ['volinfo_name', 'volinfo_sex', 'volinfo_age',
#                                 'volinfo_jiguan', 'volinfo_live_address', 'volinfo_marriage', 'volinfo_idcard_type',
#                                 'volinfo_id_num', 'volinfo_birthday', 'volinfo_email', 'volinfo_graduate_school',
#                                 'volinfo_graduate_date', 'volinfo_education', 'volinfo_profession', 'volinfo_employer',
#                                 'volinfo_position', 'volinfo_mail_address', 'volinfo_zipcode', 'volinfo_contact_number',
#                                 'volinfo_cellphone'
#                                 ]}),
#         ('志愿信息', {'fields': [
#          'volinfo_service_area', 'volinfo_service_date', 'volinfo_skills', 'volinfo_service_time']}),
#         ('关联用户', {'fields': ['volinfo_user']}),
#     ]
#     list_display = ('volinfo_name', 'volinfo_sex', 'volinfo_age',
#                     'volinfo_cellphone', 'volinfo_service_area', 'volinfo_service_date')
#     # 遗留问题:想要在详细信息里列出姓名、性别和联系方式，因为不是field，会出错


# admin.site.register(VolunteerInformation, VolunteerInformationAdmin)

class TrainingVolunteerInline(admin.TabularInline):
    verbose_name = '报名志愿者清单'
    verbose_name_plural = '报名志愿者清单'
    # fieldsets = [
    #     (
    #         None,
    #         {
    #             'fields': ('campaign_person_name', 'campaign_person_sex', 'campaign_person_cellphone')
    #         }
    #     )
    # ]
    model = AbilityTraining.volunteers.through
    # model = CampaignPerson
    extra = 5 #默认显示条目的数量

class AbilityTrainingAdmin(admin.ModelAdmin):
    inlines = [TrainingVolunteerInline, ]
    fieldsets = [
        ('志愿者培训课程信息', {'fields': ['at_zhu_jiang_ren', 'at_theme', 'at_date', 'at_content', 'at_address',
                                  'at_counts', 'at_sign_up_deadline']}),
        # ('报名人选', {'fields': ['signup_user_list']}),
        # ('活动清单', {'fields': ('signup_user_list',)}),
        # ('访问信息', {'fields': readonly_fields})
        # ('访问信息',{'fields': ['user_access_token', 'user_access_time', 'user_refresh_token', 'user_refresh_time']}),
    ]
    list_display = ('at_theme', 'at_date', 'at_zhu_jiang_ren',
                    'at_sign_up_deadline', 'at_counts')


admin.site.register(AbilityTraining, AbilityTrainingAdmin)


admin.site.unregister(Group)
