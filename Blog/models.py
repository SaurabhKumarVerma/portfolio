from django.db import models

# # Create A blog models here.
# title
# Publication Date
# body
# image
#
#
# # Add theBlog app to setting
# # Create a mirragtion
# # migration
# # Add to the Admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pu_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
