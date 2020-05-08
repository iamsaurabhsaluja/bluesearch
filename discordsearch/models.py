from django.db import models

# Create your models here.

class Messages( models.Model ):
    message_id = models.AutoField( primary_key = True )
    message = models.CharField( max_length = 255 )
    sender_name = models.CharField( max_length = 255 )
    created_time = models.DateTimeField( auto_now_add = True )
