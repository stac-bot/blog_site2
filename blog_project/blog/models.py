from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.



class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title =models.CharField(max_length=200)
    text = models.TextField()
    created_date= models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

#create the method that shows the pulished date
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    #create the method to approve the comments
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

        #create the method to get the page to the post

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

#create the model for the comments
class Comment(models.Model):
    post=models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author =models.CharField(max_length=200)
    text = models.TextField()
    created_date= models.DateTimeField(default =timezone.now)
    approved_comment=models.BooleanField(default=False)#comment is not approved till the author say's it is True

    #create method to approve the comments
    def approve(self):
        self.approved_comment =True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
