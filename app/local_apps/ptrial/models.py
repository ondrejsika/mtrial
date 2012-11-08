from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

class Subject(models.Model):
    uk = models.SlugField(max_length=8, blank=True,)

    name = models.CharField(max_length=8)

    def __unicode__(self):
        return u"%s" % (self.name, )

    def save(self, *args, **kwargs):
        self.uk = slugify(self.name)
        return super(Subject, self).save(*args, **kwargs)


class Category(models.Model):
    uk = models.SlugField(max_length=32, blank=True)
    url = models.CharField(max_length=255, blank=True)

    subject = models.ForeignKey(Subject)
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=32)

    def path(self):
        path = [self]
        obj = self
        while obj.parent:
            path.append(obj.parent)
            obj = obj.parent
        path.reverse()
        return path

    def name_path(self):
        str_path = []
        for obj in self.path():
            str_path.append(obj.name)
        return " / ".join(str_path)

    def url_path(self):
        str_path = []
        for obj in self.path():
            obj.uk
            str_path.append(obj.uk)
        return "/".join(str_path)

    def get_related(self):
        if self.parent:
            return self.parent.category_set.all()

    def __repr__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s %s" % (self.subject.name, self.name_path())# self.tree().replace("/", " / "))

    def save(self, *args, **kwargs):
        self.uk = slugify(self.name)
        self.url = self.url_path()
        return super(Category, self).save(*args, **kwargs)

class Example(models.Model):
    category = models.ForeignKey(Category)

    entering = models.TextField()
    procedure = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s (%i)" % (self.category, self.pk, )



from django.contrib import admin
admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Example)