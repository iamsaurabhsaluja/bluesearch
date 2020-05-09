from django.db import models

# Create your models here.

class Messages( models.Model ):
    message = models.CharField( max_length = 255 )
    sender_id = models.CharField( max_length = 255 )
    created_time = models.DateTimeField( auto_now_add = True )

class Keywords( models.Model ):
    keyword = models.CharField( max_length = 255, db_index=True )
    message = models.ForeignKey( Messages, on_delete=models.CASCADE )
    created_time = models.DateTimeField( auto_now_add = True )
