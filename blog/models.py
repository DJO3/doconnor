from django.db import models
from django.core.urlresolvers import reverse
from markdown import markdown


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("tag_index", kwargs={"slug": self.slug})


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    posts = EntryQuerySet.as_manager()

    def save(self):
        self.body_html = markdown(self.body, ['codehilite'])
        super(Entry, self).save()

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class EduOrg(models.Model):
    title = models.CharField(max_length=200)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    courses = models.ManyToManyField(Course)
    slug = models.SlugField(max_length=200, unique=True)

    orgs = EntryQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ["-title"]


class About(models.Model):
    title = models.CharField(max_length=200)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    text = models.TextField()
    posts = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
        ordering = ["-created"]


class Edu(models.Model):
    title = models.CharField(max_length=200)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    text = models.TextField()
    posts = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Edu"
        verbose_name_plural = "Edu"
        ordering = ["-created"]


class EntryImage(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    image = models.ImageField(upload_to='blog_images')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title