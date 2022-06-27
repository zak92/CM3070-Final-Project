from django.db import models
from ..user_accounts.models import *
from django.shortcuts import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

# https://www.youtube.com/watch?v=YXmsi13cMhw

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("discussion-post-category-search", kwargs={
            "slug":self.slug
        })

    @property
    def num_posts(self):
        return  DiscussionForumPost.objects.filter(categories=self).count()
    
    @property
    def last_post(self):
        return  DiscussionForumPost.objects.filter(categories=self).latest("date_updated")

    class Meta:
      verbose_name_plural = "categories"
    

class Comment(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   comment = models.TextField(null=True)
   flagged = models.BooleanField(default=False)
   date = models.DateTimeField(auto_now_add=True)
   def __str__(self):
        return self.comment

   class Meta:
    ordering = ['-date']


class DiscussionForumPost(models.Model):
  author = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=80, null=True) 
  slug = models.SlugField(max_length=80, unique=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)# NULL=fALSE
  discussion_post = RichTextField(blank=True, null=True)
  comments = models.ManyToManyField(Comment, related_name="comments", blank=True)
  flagged = models.BooleanField(default=False)
  date_updated = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title



  def save(self, *args, **kwargs):
      if not self.slug:
          self.slug = slugify(self.title)
      super(DiscussionForumPost, self).save(*args, **kwargs)

  def get_url(self):
      return reverse("discussion-post", kwargs={
          "slug":self.slug
      })

  class Meta:
    ordering = ['-date_updated']