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

    def get_related(self):
        objs = []
        if self.parent:
            for obj in self.parent.category_set.all():
                if obj.pk != self.pk:
                    objs.append(obj)
        else:
            for obj in self.subject.category_set.all():
                if obj.pk != self.pk and not obj.parent:
                    objs.append(obj)
        return objs

    def get_child(self):
        return self.category_set.all()

    def get_first_example(self):
        return self.example_set.order_by("number")[0]

    def has_child(self):
        return bool(self.get_child().count())

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

    def __repr__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s %s" % (self.subject.name, self.name_path())# self.tree().replace("/", " / "))

    def save(self, *args, **kwargs):
        self.uk = slugify(self.name)
        self.url = self.url_path()
        return super(Category, self).save(*args, **kwargs)

class Example(models.Model):
    number = models.IntegerField()
    category = models.ForeignKey(Category)

    entering = models.TextField()
    procedure = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    def get_nav(self, length=5):
        n = self.number
        related_examples = self.category.example_set.order_by("number")
        if related_examples.count() <= length:
            return related_examples
        if n < 3:
            return related_examples[:5]
        if n > related_examples.count()-3:
            return related_examples[4:]
        return related_examples[n-3:n+2]

    def get_next(self):
        try:
            return Example.objects.get(category=self.category, number=self.number+1)
        except Example.DoesNotExist:
            return None

    def get_prev(self):
        try:
            return Example.objects.get(category=self.category, number=self.number-1)
        except Example.DoesNotExist:
            return None

    def __unicode__(self):
        return u"%s (%i)" % (self.category, self.number, )

    class Meta:
        unique_together = (("number", "category"), )

    def save(self, *args, **kwargs):
        if not self.number:
            max_number = 0
            for obj in Example.objects.all():
                if obj.number > max_number:
                    max_number = obj.number
            self.number = max_number+1
        return super(Example, self).save(*args, **kwargs)



from django.contrib import admin
admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Example)