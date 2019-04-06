from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)  # 标题

    body = models.TextField()  # 内容
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)  # 摘要
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # CASCADE必须去掉默认的小括号
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错：


    def __str__(self):
        return self.tirle

    # 自定义 get_adsolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})