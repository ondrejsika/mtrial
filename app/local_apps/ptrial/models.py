from django.db import models
from django.template.defaultfilters import slugify

class Subject(models.Model):
    url_key = models.SlugField(max_length=8, blank=True,)

    name = models.CharField(max_length=8)

    def __unicode__(self):
        return u"%s" % (self.name, )

    def save(self, *args, **kwargs):
        self.url_key = slugify(self.name)
        return super(Subject, self).save(*args, **kwargs)


class Category(models.Model):
    url_key = models.SlugField(max_length=32, blank=True)

    subject = models.ForeignKey(Subject)
    parrent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        path = [self.name]

        obj = self
        while 1:
            if obj.parrent:
                path.append(obj.parrent.name)
                obj = self.parrent
            else:
                break

        return "%s %s" % (self.subject.name, " / ".join(reversed(path)))

    def save(self, *args, **kwargs):
        self.url_key = slugify(self.name)
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