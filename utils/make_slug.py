from django.utils.text import slugify


def make_slugify(instance, new_slug=None):
    if new_slug:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug = f"{slug}-{qs.count()}"
        return make_slugify(instance, new_slug=slug)
    instance.slug = slug
