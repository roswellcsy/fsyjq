# coding: utf-8
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, password):
        if not (username):
            raise '用户名不能为空'
        user = self.model(
            username = username,
            # email=self.normalize_email(email),
            # email = email,
            # mobile = mobile,
            last_login=timezone.now()
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, verbose_name='用户名')
    email = models.EmailField(max_length=255, blank=True, null=True)
    cellphone = models.CharField(
        max_length=11, verbose_name='手机号', blank=True, null=True)
    volunteer_or_not = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name_plural = '用户信息'
        
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.username

    def has_module_perms(self, api):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def get_full_name(self):
        # The user is identified by their email address
        return self.username


# 单图片上传
class SingleUploadImg(models.Model):
    class Meta:
        verbose_name_plural = '单图片上传'

    def __str__(self):
        return self.photo_name
    campaign_or_service_name = models.CharField(
        max_length=50, verbose_name='活动名称')
    photo_name = models.CharField(max_length=10, verbose_name='照片名字')
    photo = models.ImageField('图片', upload_to='media')


# # 政策文章
# class Policy(models.Model):
#     pass


# 政策咨询
class PolicyQA(models.Model):
    class Meta:
        verbose_name_plural = '政策咨询'
    qa_title = models.CharField(max_length=255, verbose_name='提问标题')
    qa_content = models.CharField(max_length=255, verbose_name='提问内容')
    qa_answer = models.CharField(max_length=255, verbose_name='回答')
    qa_ask_date = models.DateTimeField(
        verbose_name='提问时间', null=True, blank=True)
    qa_answer_date = models.DateTimeField(
        verbose_name='回答时间', null=True, blank=True)
    # 与用户关系是一对一
    qa_user = models.ForeignKey(User, verbose_name='用户', blank=True)


# 专业咨询，不注册也可以提
class ProfessionalAdvice(models.Model):
    class Meta:
        verbose_name_plural = '专业咨询列表'

    def __str__(self):
        return self.proadv_full_name
    # 初始信息
    proadv_user = models.ForeignKey(User, verbose_name='用户')
    proadv_question_title = models.CharField(
        max_length=255, verbose_name='咨询问题')
    proadv_question_content = models.CharField(
        max_length=255, verbose_name='咨询内容')

    # 对象基本信息
    proadv_full_name = models.CharField(
        max_length=10, verbose_name='姓名')
    # '1'代表男，'2'代表女
    sex = (
        ('1', '男'),
        ('2', '女'),
    )
    proadv_sex = models.CharField(
        max_length=1, choices=sex, verbose_name='性别')
    proadv_age = models.CharField(
        max_length=20, blank=True, verbose_name='年龄')
    proadv_house_hold = models.CharField(
        max_length=50, blank=True, verbose_name='户籍所在地')
    # (6)身份证明
    proadv_id_num = models.CharField(
        max_length=50, blank=True, verbose_name='身份证明')
    # (7)民族
    proadv_ethnic = models.CharField(
        max_length=50, blank=True, verbose_name='民族')
    # (8)政治面貌
    proadv_political_status = models.CharField(
        max_length=50, blank=True, verbose_name='政治面貌')
    # (9)宗教
    proadv_religion = models.CharField(
        max_length=50, blank=True, verbose_name='宗教')
    # (10)职业
    proadv_occupation = models.CharField(
        max_length=50, blank=True, verbose_name='职业')
    # (11)就读年级
    proadv_studying_grade = models.CharField(
        max_length=50, blank=True, verbose_name='就读年级')
    # (12)文化程度
    proadv_degree_of_education = models.CharField(
        max_length=50, blank=True, verbose_name='文化程度')
    # (13)所在社区
    proadv_community = models.CharField(
        max_length=50, blank=True, verbose_name='所在社区')
    # (14)联系方式
    proadv_contact = models.CharField(
        max_length=11, blank=True, verbose_name='联系方式(手机)')
    # (15)家庭住址
    proadv_live_address = models.CharField(
        max_length=50, blank=True, verbose_name='家庭住址')
    marriage_status = (
        ('1', '单身'),
        ('2', '同居'),
        ('3', '已婚'),
        ('4', '分居'),
        ('5', '离婚'),
        ('6', '丧偶'),
        ('7', '其它'),
    )
    proadv_marriage = models.CharField(
        max_length=1, choices=marriage_status, blank=True, verbose_name='婚姻状况')

    # 个案基本信息
    proadv_from = models.CharField(
        max_length=255, verbose_name='个案来源')

    proadv_rescue_methods = models.CharField(
        max_length=255, verbose_name='求助方法')

    question_type = (
        ('1', '亲子关系问题'),
        ('2', '婚姻问题'),
        ('3', '家庭纠纷'),
        ('4', '经济问题'),
        ('5', '职业问题'),
        ('6', '住屋问题'),
        ('7', '家庭暴力致伤/死(受害对象: 子女 / 配偶 / 老人 / 其它______)'),
        ('8', '个人精神/情绪问题'),
        ('9', '个人行为问题(吸毒/酒/赌博)'),
        ('10', '恋爱/交友问题'),
        ('11', '患病/复康问题(病类)'),
        ('12', '未婚怀孕'),
        ('13', '收养'),
        ('14', '其它'),
    )
    proadv_question_type = models.CharField(
        max_length=50, choices=question_type, blank=True, verbose_name='咨询问题类型')

    social_rescue = (
        ('1', '医疗救助'),
        ('2', '教育救助'),
        ('3', '住房救助'),
        ('4', '临时救助'),
        ('5', '最低生活保障救助'),
        ('6', '其它'),
    )
    proadv_social_rescue = models.CharField(
        max_length=50, choices=social_rescue, blank=True, verbose_name='社会救助')

    result = (
        ('1', '问题改善/解决结案'),
        ('2', '转为辅导个案'),
        ('3', '转介'),
    )
    proadv_result = models.CharField(
        max_length=1, choices=result, blank=True, verbose_name='咨询结果')

    # 负责方信息
    proadv_sw_name = models.CharField(max_length=50, verbose_name='社工姓名')
    proadv_case_id = models.CharField(max_length=50, verbose_name='个案编号')
    proadv_date = models.DateField('咨询日期')

    # 咨询记录
    proadv_serv_date = models.DateField('服务日期')
    proadv_serv_time = models.TimeField('服务时间')
    proadv_serv_localtion = models.CharField(max_length=255, verbose_name='服务地点')
    proadv_serv_counts = models.PositiveSmallIntegerField(default=0, verbose_name='服务次数')
    proadv_serv_type = models.CharField(max_length=255, verbose_name='服务方式')
    proadv_serv_content = models.TextField('服务内容')

    # 个案状态,默认True开启,后台可选False
    proadv_status = models.BooleanField(default=True, verbose_name='个案状态')
    def status(self):
        if self.proadv_status == True:
            return '开启'
        elif self.proadv_status == False:
            return '关闭'


# 活动，需要后台上传图片
class Campaign(models.Model):
    class Meta:
        verbose_name_plural = '公益活动'

    def __str__(self):
        return self.campaign_name

    # 活动名称
    campaign_name = models.CharField(max_length=50, verbose_name='活动名称')
    # 活动分类,小组类，活动类，其他
    TYPE = (
        ('1', '小组类'),
        ('2', '活动类'),
        ('3', '其他'),
    )
    campaign_type = models.CharField(
        max_length=50, choices=TYPE, verbose_name='活动分类')
    # 活动时间
    campaign_date = models.DateTimeField('活动时间')
    # 服务对象
    campaign_client = models.CharField(max_length=50, verbose_name='服务对象')
    # 活动地点
    campaign_address = models.CharField(max_length=50, verbose_name='活动地点')
    # 活动内容
    campaign_content = models.CharField(max_length=255, verbose_name='活动内容')
    # 服务费用
    campaign_paid = models.CharField(max_length=50, verbose_name='服务费用')
    # 活动图片
    photos = models.ManyToManyField(
        SingleUploadImg, blank=True, verbose_name='活动图片')
    # 报名截止日期
    campaign_signup_deadline = models.DateTimeField('报名截止时间')
    # 联系方式
    campaign_contact = models.CharField(max_length=50, verbose_name='活动联系方式')
    # 可报名人数
    campaign_counts = models.PositiveSmallIntegerField(verbose_name='可报名总人数')
    # 报名人员
    signup_user_list = models.ManyToManyField(
        User, blank=True, verbose_name='报名人员名单')

    def user_list(self):
        return ','.join(['姓名:' + i.name + ',联系方式:' + i.cellphone for i in self.signup_user_list.all()])
    user_list.short_description = '报名人员名单'

# 志愿者登记,用Profile,onetoonefiled来新增
class VolunteerRegistration(models.Model):
    pass


# 志愿服务
class VolunteerService(models.Model):
    pass


# 能力培训
class AbilityTraining(models.Model):
    pass
