from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from app_eq_1.models import UserProfile


@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    if kwargs.get('created', True):
        UserProfile.objects.get_or_create(user=instance)

# @receiver(post_save, sender=User)
# def create(sender, instance, **kwargs):
#     if kwargs.get('created',True):
#         ctype = ContentType.objects.get_for_model(instance)
#         activity = Activity.objects.get_or_create(
#             actor = instance.user,
#             action = ' shared ',
#             content_type = ctype,
#             object_id = instance.id,
#             pub_date = instance.pub_date
#         )