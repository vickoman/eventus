from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from geoposition.fields import GeopositionField


class TimeStampModel(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)    

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)
    imagen = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Event(TimeStampModel):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(editable=False)
    summary = models.TextField(max_length=255)
    content = models.TextField()
    Category = models.ForeignKey(Category)
    place = models.CharField(max_length=50)
    position = GeopositionField(null=True, blank=True)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    imagen = models.ImageField(upload_to='events')
    is_free = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    views = models.PositiveIntegerField(default=0)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)        
        super(Event, self).save(*args, **kwargs)        

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

class Assistant(TimeStampModel):
    assistant = models.ForeignKey(settings.AUTH_USER_MODEL)
    event = models.ManyToManyField(Event)
    attended = models.BooleanField(default=False)
    has_paid = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s" % (self.assistant.username, self.event.name)

    class Meta:
        verbose_name = 'Asistente'
        verbose_name_plural = 'Asistentes'

class Comments(TimeStampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    event = models.ForeignKey(Event)
    content = models.TextField()

    def __unicode__(self):
        return "%s %s" % (self.user.username, self.event.name)

    class Meta:
        verbose_name = 'Cometario'
        verbose_name_plural = 'Comentarios'

