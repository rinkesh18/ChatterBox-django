from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create banter model:
class Banter(models.Model):
    user = models.ForeignKey(User, related_name='banters', on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=280)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name="banter_like",blank=True)

    
    # Keep tarck or count of likes
    def number_of_likes(self):
        return self.likes.count()
    
    
    def __str__(self):
        return (
            f"{self.body} by {self.user.username} at {self.created.strftime('%Y-%m-%d %H:%M')} "
          )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    profile_bio  = models.CharField(null=True,blank=True,max_length=500)
    profile_link = models.CharField(null=True,blank=True,max_length=100)
    facebook_link = models.CharField(null=True,blank=True,max_length=100)
    instagram_link =models.CharField(null=True,blank=True,max_length=100)
    linkdlen_link = models.CharField(null=True,blank=True,max_length=100)
    
    def follow_count(self):
        return self.follows.count()
    
    def following_count(self):
        return self.followed_by.count()
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User )
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Check if the profile already exists
        if not hasattr(instance, 'profile'):
            user_profile = Profile.objects.create(user=instance)
            user_profile.follows.set([instance.id])  # Follow themselves
            user_profile.save()