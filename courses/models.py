from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='main_category_images/')

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='sub_category_images/')
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='sub_categories')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='courses')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name




