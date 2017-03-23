from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager

# Create your models here.


class SaveLocation(MPTTModel):
    name = models.CharField(max_length=250)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Doc(models.Model):
    no = models.CharField(max_length=250, verbose_name='Số văn bản')
    date = models.DateField(verbose_name='Ngày')
    summary = models.TextField(verbose_name='Trích yếu')
    issued_by = models.CharField(max_length=250, verbose_name='Nơi ban hành')
    tags = TaggableManager()
    location = models.ForeignKey(SaveLocation, verbose_name='Nơi lưu')

    def __str__(self):
        return self.no
