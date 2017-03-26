from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class SaveLocation(MPTTModel):
    name = models.CharField(max_length=250)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = verbose_name_plural = 'Nơi lưu'

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=250, verbose_name='Tên dự án')
    investor = models.CharField(max_length=250, verbose_name='Chủ đầu tư')
    location = models.CharField(max_length=250, verbose_name='Địa điểm')
    total_investment = models.CharField(max_length=20, verbose_name='Tổng mức đầu tư')
    equity_source = models.CharField(max_length=250, verbose_name='Nguồn vốn')
    time = models.CharField(max_length=250, verbose_name='Thời gian thực hiện')

    class Meta:
        verbose_name = verbose_name_plural = 'Dự án'

    def get_absolute_url(self):
        return reverse('doc:project-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=250, verbose_name='Tên')
    location = TreeForeignKey(SaveLocation, verbose_name='Nơi lưu')
    project = models.ForeignKey(Project, verbose_name='Dự án', null=True, blank=True)
    summary = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Tập hồ sơ'

    def __str__(self):
        if self.project:
            return "%s - %s" % (self.project.name, self.name)
        else:
            return self.name


class Document(models.Model):
    number = models.CharField(max_length=250, verbose_name='Số văn bản')
    date = models.DateField(verbose_name='Ngày')
    summary = models.TextField(verbose_name='Trích yếu')
    issued_by = models.CharField(max_length=250, verbose_name='Nơi ban hành')
    collections = models.ManyToManyField(Collection, verbose_name='Tập hồ sơ', blank=True)
    projects = models.ManyToManyField(Project, verbose_name='Dự án', blank=True)
    file = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Tài liệu'

    def get_projects(self):
        return self.projects.all()

    def get_collections(self):
        return self.collections.all()

    def __str__(self):
        return self.number
