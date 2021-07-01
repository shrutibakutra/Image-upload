from django.db import models
import uuid

# Create your models here.


class Member(models.Model):   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10)

    def __str__(self):
        return '%s: %s' % (self.id, self.name)


class Image(models.Model):   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)   
    created = models.DateTimeField("Created date", auto_now_add=True, null=True)    
    image = models.ImageField(upload_to ='uploads/')    
    type = models.CharField(max_length=4)


 # width = models.PositiveSmallIntegerField(null=True,editable=False)    
 #  # height = models.PositiveSmallIntegerField(null=True,editable=False)