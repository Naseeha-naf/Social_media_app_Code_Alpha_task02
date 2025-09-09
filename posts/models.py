from django.db import models
from django.contrib.auth.models import User


# Post model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Who posted
    content = models.TextField()  # Text content of post
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  # Optional image
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user.username} - {self.content[:30]}"


# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:20]}"


# Like model
class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')  # Prevent duplicate likes

    def __str__(self):
        return f"{self.user.username} likes {self.post.id}"
