from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Post(models.Model):
    image = models.ImageField(upload_to='static/postPhoto')
    post_title = models.CharField(max_length=200)
    post = models.TextField()
    post_date = models.DateTimeField(auto_now=True)


    post_category = models.ForeignKey(
        "Category", 
        on_delete = models.CASCADE
    )

    def __str__(self):
        if len(self.post_title) >= 50:
            return self.post_title[:50] + "..."
        return self.post_title
    

