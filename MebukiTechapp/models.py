from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    catch_image = models.TextField()
    catch_image_alt = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    main = models.TextField()
    relation = models.ManyToManyField('self', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public_report = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def summary(self):
        return self.main[:50]

class Comment(models.Model):
    comment = models.TextField(default="", max_length=500)
    created_at = models.DateField(auto_now_add=True)
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    # on_delete=models.CASCADE = データが削除されたときは一緒に削除