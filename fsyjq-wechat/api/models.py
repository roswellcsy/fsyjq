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
            username=username,
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
    username = models.CharField(
        max_length=255, unique=True, verbose_name='用户名')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name_plural = '账户管理'

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

# 用户基本信息
class UserInformation(models.Model):
    class Meta:
        verbose_name_plural = '用户基本信息'

    def __str__(self):
        return '用户基本信息'
    # 与账号一一对应关系
    user_information_user = models.OneToOneField(
        User, verbose_name='平台用户')
    # 用户姓名
    user_information_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='姓名')
    # 用户性别
    # '1'代表男，'2'代表女
    sex = (
        ('1', '男'),
        ('2', '女'),
    )
    user_information_sex = models.CharField(
        max_length=1, default=1, choices=sex, verbose_name='性别')
    # 用户联系电话
    user_information_cellphone = models.CharField(
        max_length=11, verbose_name='手机号', blank=True, null=True)
    # 用户电邮
    user_information_email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='电邮')
    # 用户是否志愿者
    user_information_volunteer = models.BooleanField(default=False, verbose_name='志愿者')
    user_information_update_time = models.DateTimeField(auto_now=True)


# 单图片上传，提供公益活动使用
class SingleUploadImg(models.Model):
    class Meta:
        verbose_name_plural = '单图片上传'

    def __str__(self):
        return self.photo_name
    campaign_or_service_name = models.CharField(
        max_length=50, verbose_name='活动名称')
    photo_name = models.CharField(max_length=10, verbose_name='照片名字')
    photo_path = models.ImageField('图片', upload_to='media')
    upload_date = models.DateTimeField(auto_now=True)


# # 政策文章
# class Policy(models.Model):
#     pass


# 政策咨询
class PolicyQA(models.Model):
    class Meta:
        verbose_name_plural = '政策咨询'
    # 咨询人信息
    qa_fullname = models.CharField(max_length=10, verbose_name='姓名')

    sex = (
        ('1', '男'),
        ('2', '女'),
    )
    qa_sex = models.CharField(max_length=1, default=1, choices=sex, verbose_name='性别')  # 1男2女

    qa_age = models.PositiveIntegerField(
        verbose_name='年龄', null=True, blank=True)

    qa_live_area = models.CharField(
        max_length=255, verbose_name='居住区域', null=True, blank=True)

    qa_cellphone = models.CharField(
        max_length=11, verbose_name='联系方式', null=True, blank=True)

    qa_occupation = models.CharField(
        max_length=50, verbose_name='职业', null=True, blank=True)
    marriage_status = (
        ('1', '未婚'),
        ('2', '已婚'),
        ('3', '离异'),
        ('4', '丧偶'),
    )
    qa_marriage = models.CharField(
        max_length=1, choices=marriage_status, verbose_name='婚姻状况', null=True, blank=True)
    # 咨询内容
    qa_title = models.CharField(max_length=255, verbose_name='标题')

    type_options = (
        ('1', '居住证及相关'),
        ('2', '户籍及相关'),
        ('3', '计生及相关'),
        ('4', '住房及相关'),
        ('5', '子女教育及相关'),
        ('6', '积分制及相关'),
        ('7', '综合类（多种问题）'),
    )

    qa_type = models.CharField(max_length=1, default=1, choices=type_options, verbose_name='类型')

    qa_content = models.TextField(verbose_name='提问内容')

    o2o_type = (
        ('1', '线上'),
        ('2', '线下'),
    )

    qa_o2o = models.CharField(max_length=1, default=1, choices=o2o_type, verbose_name='线上线下回复')
    # 只在我的咨询显示
    qa_ask_date = models.DateTimeField(
        verbose_name='提问时间', auto_now_add=True)
    # 答复信息，只在我的咨询显示
    qa_answer = models.TextField(verbose_name='回答', null=True, blank=True)

    qa_answer_date = models.DateTimeField(
        verbose_name='回答时间', null=True, blank=True)

    # 咨询状态,默认False未回答,后台回答后可选True
    qa_status = models.BooleanField(default=False, verbose_name='咨询状态')
    # 与用户关系是一对一
    qa_user = models.ForeignKey(
        User, related_name='policyqas', verbose_name='用户')


# 专业咨询
class ProfessionalAdvice(models.Model):
    class Meta:
        verbose_name_plural = '专业咨询列表'

    def __str__(self):
        return self.proadv_full_name
    # 初始信息
    # 用户信息关联，一对一
    proadv_user = models.ForeignKey(User, verbose_name='用户')
    proadv_question_title = models.CharField(
        max_length=255, verbose_name='咨询问题')
    proadv_question_content = models.TextField(
        verbose_name='咨询内容')
    proadv_update_time = models.DateTimeField(auto_now=True)
    # 对象基本信息
    proadv_full_name = models.CharField(
        max_length=10, verbose_name='姓名')
    # '1'代表男，'2'代表女
    sex = (
        ('1', '男'),
        ('2', '女'),
    )
    proadv_sex = models.CharField(
        max_length=1, default=1, choices=sex, verbose_name='性别')
    proadv_age = models.PositiveIntegerField(
        null=True, blank=True, verbose_name='年龄')
    proadv_house_hold = models.CharField(
        max_length=50, blank=True, verbose_name='户籍所在地')
    # (6)身份证明
    proadv_id_num = models.CharField(
        max_length=50, blank=True, verbose_name='身份证明')
    # (7)民族
    ethnic_options = (
        ('1', '汉族'),
        ('2', '少数民族'),
        ('3', '其他'),
    )
    proadv_ethnic = models.CharField(
        max_length=1, choices=ethnic_options, blank=True, verbose_name='民族')
    # (8)政治面貌
    political_options = (
        ('1', '中共党员'),
        ('2', '民主党派成员'),
        ('3', '共青团员'),
        ('4', '群众'),
        ('5', '其他'),
    )
    proadv_political_status = models.CharField(
        max_length=1, choices=political_options, blank=True, verbose_name='政治面貌')
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
        max_length=11, verbose_name='联系方式(手机)')
    # (15)家庭住址
    proadv_live_address = models.CharField(
        max_length=50, blank=True, verbose_name='家庭住址')
    marriage_status = (
        ('1', '未婚'),
        ('2', '已婚'),
        ('3', '离异'),
        ('4', '丧偶'),
    )
    proadv_marriage = models.CharField(
        max_length=1, choices=marriage_status, blank=True, verbose_name='婚姻状况')

    # 个案基本信息
    from_options = (
        ('1', '社工发现'),
        ('2', '本人求助'),
        ('3', '他人求助'),
        ('4', '他人介绍'),
        ('5', '机构转介'),
        ('6', '其    他'),
    )
    proadv_from = models.CharField(
        max_length=1, choices=from_options, verbose_name='个案来源')
    rescue_options = (
        ('1', '来    信'),
        ('2', '来    电'),
        ('3', '面    访'),
        ('4', '网上求助'),
        ('5', '其    他'),
    )
    proadv_rescue_methods = models.CharField(
        max_length=1, choices=rescue_options, verbose_name='求助方法')

    question_type = (
        ('1', '亲子关系问题'),
        ('2', '婚姻问题'),
        ('3', '家庭纠纷'),
        ('4', '经济问题'),
        ('5', '职业问题'),
        ('6', '住屋问题'),
        ('7', '家庭暴力致伤/死(受害对象:子女/配偶/老人/其它'),
        ('8', '个人精神/情绪问题'),
        ('9', '个人行为问题(吸毒/酒/赌博)'),
        ('10', '恋爱/交友问题'),
        ('11', '患病/复康问题(病类)'),
        ('12', '未婚怀孕'),
        ('13', '收养'),
        ('14', '其它'),
    )
    proadv_question_type = models.CharField(
        max_length=50, default=14, choices=question_type, blank=True, verbose_name='咨询问题类型')

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
    proadv_sw_name = models.CharField(null=True, blank=True, max_length=50, verbose_name='社工姓名')
    proadv_case_id = models.CharField(null=True, blank=True, max_length=50, verbose_name='个案编号')
    proadv_date = models.DateField(null=True, blank=True, verbose_name='咨询日期')

    # 咨询记录
    proadv_serv_date = models.DateField(null=True, blank=True, verbose_name='服务日期')
    proadv_serv_time = models.TimeField(null=True, blank=True, verbose_name='服务时间')
    proadv_serv_localtion = models.CharField(
        null=True, blank=True, max_length=255, verbose_name='服务地点')
    proadv_serv_counts = models.PositiveSmallIntegerField(
        default=0, verbose_name='服务次数')
    serv_type_options = (
        ('1', '面谈'),
        ('2', '电访'),
        ('3', '其他'),
    )
    proadv_serv_type = models.CharField(null=True, blank=True, max_length=1, choices=serv_type_options, verbose_name='服务方式')
    proadv_serv_content = models.TextField(null=True, blank=True, verbose_name='服务内容')

    # 个案完成状态,默认False开启,后台可选True关闭
    proadv_status = models.BooleanField(default=False, verbose_name='个案完成状态')

    def status(self):
        if self.proadv_status == True:
            return '完成'
        elif self.proadv_status == False:
            return '待跟进'


# 用户基本信息



class VolunteerInformation(models.Model):
    class Meta:
        verbose_name_plural = '志愿者信息'

    def __str__(self):
        return '志愿者信息'
    # 志愿者信息
    volinfo_user = models.OneToOneField(User, verbose_name='平台用户')
    #(1)姓名
    # volinfo_name = models.CharField(max_length=20, verbose_name='姓名')
    # volinfo_name = volinfo_user.user_information_name
    # def volinfo_name(self):
    #     return self.volinfo_user.name
    # volinfo_name.short_description = '姓名'
    #(2)性别 值为1时是男性，值为2时是女性，值为0时是未知
    # SEX = (
    #     ('1', '男'),
    #     ('2', '女'),
    # )
    # volinfo_sex = models.CharField(
    #     max_length=1, choices=SEX, verbose_name='性别')
    # volinfo_sex = UserInformation.user_information_sex

    # def volinfo_sex(self):
    #     if self.volinfo_user.user_sex == '1':
    #         return '男'
    #     elif self.volinfo_user.user_sex == '2':
    #         return '女'
    # volinfo_sex.short_description = '性别'
    # volinfo_age = models.PositiveIntegerField(
    #     null=True, blank=True, verbose_name='年龄')

    #(3)籍贯
    volinfo_jiguan = models.CharField(
        max_length=100, blank=True, verbose_name='籍贯')
    #(4)住址
    volinfo_live_address = models.CharField(
        max_length=100, blank=True, verbose_name='住址')
    #(5)婚姻状况(已婚未婚)
    marriage_status = (
        ('1', '未婚'),
        ('2', '已婚'),
        ('3', '离异'),
        ('4', '丧偶'),
    )
    volinfo_marriage = models.CharField(
        max_length=1, choices=marriage_status, default='1', blank=True, verbose_name='婚姻状况')
    #(6)证件类型(身份证、护照、警官证、军官证)
    id_card_type = (
        ('1', '身份证'),
        ('2', '护照'),
        ('3', '警官证'),
        ('4', '军官证'),
    )
    volinfo_idcard_type = models.CharField(
        max_length=10, choices=id_card_type, default='1', blank=True, verbose_name='证件类型')
    #(7)证件号码
    volinfo_id_num = models.CharField(
        max_length=18, blank=True, verbose_name='证件号码')
    #(8)出生日期(年月日)
    volinfo_birthday = models.DateField(
        blank=True, null=True, verbose_name='出生日期')
    #(9)Email
    # volinfo_email = models.CharField(
    #     max_length=50, blank=True, verbose_name='电子邮箱')
    #(10)毕业院校
    volinfo_graduate_school = models.CharField(
        max_length=50, blank=True, verbose_name='毕业院校')
    #(11)毕业时间
    volinfo_graduate_date = models.DateField(
        blank=True, null=True, verbose_name='毕业时间')
    #(12)学历
    volinfo_education = models.CharField(
        max_length=5, blank=True, verbose_name='学历')
    #(13)专业
    volinfo_profession = models.CharField(
        max_length=50, blank=True, verbose_name='专业')
    #(14)工作单位
    volinfo_employer = models.CharField(
        max_length=50, blank=True, verbose_name='工作单位')
    #(15)职务
    volinfo_position = models.CharField(
        max_length=50, blank=True, verbose_name='职务')
    #(16)通讯地址
    volinfo_mail_address = models.CharField(
        max_length=50, blank=True, verbose_name='通讯地址')
    #(17)邮编
    volinfo_zipcode = models.CharField(
        max_length=10, blank=True, verbose_name='邮编')
    #(18)联系电话
    volinfo_contact_number = models.CharField(
        max_length=50, blank=True, verbose_name='固定电话')
    #(19)移动电话
    # volinfo_cellphone = models.CharField(max_length=11, verbose_name='移动电话')
    # volinfo_cellphone = UserInformation.user_information_cellphone
    # def volinfo_cell_number(self):
    #     return self.volinfo_user.cellphone
    # volinfo_cell_number.short_description = '移动电话'
    #(20)志愿服务区(禅城 - 社区)
    volinfo_service_area = models.CharField(
        max_length=50, blank=True, verbose_name='志愿服务区')
    #(21)志愿服务时间(法定休息日、工作日、不限)
    service_date_options = (
        ('1', '法定休息日'),
        ('2', '工作日'),
        ('3', '不限'),
    )
    volinfo_service_date = models.CharField(
        max_length=50, choices=service_date_options, default='1', blank=True, verbose_name='志愿服务时间')
    #(22)技能
    volinfo_skills = models.CharField(
        max_length=50, blank=True, verbose_name='技能')
    # 累计志愿服务时数
    volinfo_service_time = models.PositiveIntegerField(default=0, verbose_name='志愿活动认证时数')
    volinfo_update_time = models.DateTimeField(auto_now=True)

# 公益活动信息，需要后台上传图片
class Campaign(models.Model):
    class Meta:
        verbose_name_plural = '公益活动信息'

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
    campaign_content = models.TextField(verbose_name='活动内容')
    # 服务费用
    campaign_paid = models.CharField(max_length=50, verbose_name='服务费用')
    # 活动图片
    photos = models.ManyToManyField(
        SingleUploadImg, blank=True, verbose_name='活动图片')
    # 报名截止日期
    campaign_signup_deadline = models.DateTimeField('报名截止时间')
    # 联系方式
    campaign_contact = models.CharField(max_length=50, verbose_name='活动联系方式')
    # 活动认证时数
    campaign_certified_hours = models.PositiveIntegerField(
        default=0, verbose_name='志愿活动认证时数（小时）')
    # 可报名参与人数
    campaign_counts = models.PositiveSmallIntegerField(default=0, verbose_name='可报名总人数')
    # 可报名志愿者人数
    campaign_vol_counts = models.PositiveSmallIntegerField(default=0, verbose_name='可报名志愿者人数')
    # 活动状态
    campaign_status = models.BooleanField(default=True, verbose_name='活动状态')
    campaign_update_time = models.DateTimeField(auto_now=True)
    # 报名人员
    # signup_user_list = models.ManyToManyField(
    #     CampaignPerson, blank=True, verbose_name='报名人员名单')

    # def user_list(self):
    #     return ','.join(['姓名:' + i.campaign_person_name + ',性别:' + i.campaign_person_sex + ',联系方式:' + i.campaign_person_cellphone for i in self.signup_user_list.all()])
    # user_list.short_description = '报名人员名单'
    campaign_members = models.ManyToManyField(
        User, blank=True, related_name='campaign_members', verbose_name='报名人员名单')
    campaign_volunteers = models.ManyToManyField(
        User, blank=True, related_name='campaign_volunteers', verbose_name='报名志愿者名单')
    


# 志愿者登记,用Profile,onetoonefiled来新增

# 能力培训
class AbilityTraining(models.Model):
    # 志愿者培训课程信息
    class Meta:
        verbose_name_plural = '能力培训'
    # 志愿者培训
    # 主讲人
    at_zhu_jiang_ren = models.CharField(
        max_length=50, verbose_name='主讲人')
    # 培训主题
    at_theme = models.CharField(max_length=100, verbose_name='培训主题')
    # 培训时间
    at_date = models.DateTimeField('培训时间')
    # 培训内容
    at_content = models.TextField(verbose_name='培训内容')
    # 培训地址
    at_address = models.CharField(max_length=100, verbose_name='培训地址')
    # 可报名人数
    at_counts = models.PositiveSmallIntegerField(default=0, verbose_name='可报名总人数')
    # 剩余可报名人数
    at_remain = models.PositiveSmallIntegerField(default=0, verbose_name='剩余可报名人数')
    # 培训报名截止日期
    at_sign_up_deadline = models.DateField('服务报名截止时间')
    at_update_time = models.DateTimeField(auto_now=True)
    # pass
    # 报名人员
    volunteers = models.ManyToManyField(
        User, blank=True, verbose_name='报名志愿者名单')

    # def user_list(self):
    #     return ','.join(['姓名:' + i.volinfo_name + ',性别:' + i.volinfo_sex + ',联系方式:' + i.volinfo_cellphone for i in self.volunteers.all()])
    # user_list.short_description = '报名志愿者名单'