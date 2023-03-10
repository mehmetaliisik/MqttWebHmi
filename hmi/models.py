from django.db import models

class Hmi(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
