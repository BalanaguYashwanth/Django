from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from todo.models import data

@receiver(post_save,sender=User)
def save_data(sender,instance,created,**kw):
    if created:
        data.objects.create(user=instance)

def save_user_data(sender,instance,**kw):
    instance.data.save()

    