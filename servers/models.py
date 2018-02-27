from django.db import models
from django.contrib.auth.models import User
from universal.models import Version
import uuid

# NOTE:
#	Don't forget >>> models.Model.id and models.Model.pk
#
# are unique identifiers to the database.
# don't try and make a uuid though, it breaks things like that
# object_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#
# So actually... when using IDs these fields are autogenerated by default
# id = ...
# pk = ...
#
# However, note that they're automatically set to the instance number
# in the table it's data is contained within.
#
# BUG: *** FIXED ***
# inadvertently created an extra bug because ID didn't get researched properly
# too well and was to use id as a uuid... but it's fixed now lol.
#
# So now you can:
#	Server.objects.all()[n].unique_id
#
# and use that to relate POST data to SQL data and properly display
# the relation within the templates' output.
# FIX FOR ISSUE #4

class Tag(models.Model):
    #pk = ...
    #id = ...
    value = models.CharField(max_length=20)
    def __str__(self):
        return self.value

class Server(models.Model):
    #pk = ...
    #id = ...
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, None)
    address = models.URLField(max_length=200, null=True)
    website = models.URLField(max_length=200, null=True)
    description = models.TextField(null=True)
    votes = models.IntegerField(default=0, null=True)
    mt_version = models.ForeignKey(Version, None)
    tags = models.ManyToManyField(Tag, verbose_name='Tags', blank=True)
