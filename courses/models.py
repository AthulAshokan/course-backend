from django.db import models
class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='main_category_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='sub_category_images/', blank=True, null=True)

    def __str__(self):
        return self.name