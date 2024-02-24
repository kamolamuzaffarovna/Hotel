from django.db import models
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import pre_save
from utils.make_slug import make_slugify


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
    slug = models.SlugField(unique=True, max_length=221, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Content(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, related_name='contents')
    content = RichTextField(null=True, blank=True)
    is_quota = models.BooleanField(default=False)


# class BlogParentLike(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, related_name='like')
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)


class Comment(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='comment/')
    message = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    # people = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='peoples')
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    likes = models.ManyToManyField('auth.User', related_name='comment_likes', blank=True)


class BlogCommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True, related_name='comment_like')

    @property
    def children(self):
        model = self.__class__
        return model.objects.filter(top_level_comment_id=self.id)


@receiver(pre_save, sender=Blog)
def blog_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        make_slugify(instance)


@receiver(pre_save, sender=Comment)
def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent:
        if not instance.parent.top_level_comment_id:
            instance.parent.top_level_comment_id = instance.parent_id
        else:
            instance.top_level_comment_id = instance.parent.top_level_comment_id
