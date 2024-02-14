from django.db import models
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import pre_save


class BaseModel(models.Model):
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(BaseModel):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='blog/')
    content = RichTextField()
    is_quota = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='comment/')
    message = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    top_level_comment_id = models.IntegerField(null=True, blank=True)

    @property
    def children(self):
        model = self.__class__
        return model.objects.filter(top_level_comment_id=self.id)


@receiver(pre_save, sender=Comment)
def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent:
        if not instance.parent.top_level_comment_id:
            instance.parent.top_level_comment_id = instance.parent_id
        else:
            instance.top_level_comment_id = instance.parent.top_level_comment_id