from django.db import models


class Field(models.Model):
    FTYPE_CHOICES = (
        ('NUMBER', 'Number'),
        ('STRING', 'String'),
        ('BOOLEAN', 'Boolean'),
    )
    fname = models.CharField(max_length=50, default='')
    ftype = models.CharField(max_length=50, choices=FTYPE_CHOICES, default=FTYPE_CHOICES[0][0])  # noqa

    def __unicode__(self):
        return '%d - %s(%s)' % (self.id, self.fname, self.ftype)


class Template(models.Model):
    tname = models.CharField(max_length=50, default='')
    # Owner to be constructed
    #owner = models.ForeignKey(User)
    description = models.TextField(blank=True)
    sample = models.TextField(blank=True)
    data_src = models.CharField(max_length=150, default='')
    thumbnail_src = models.CharField(max_length=150, default='')
    # Store the struct of the template
    fields = models.ManyToManyField(Field, blank=True, null=True)

    def __unicode__(self):
        return '%d - %s' % (self.id, self.tname)
