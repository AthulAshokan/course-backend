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
    

class Course(models.Model):
    SKILL_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name="courses")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="courses")
    instructor = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    rating = models.FloatField(default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVEL_CHOICES)
    certificate_image = models.ImageField(upload_to="certificates/", blank=True,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.instructor} - {self.sub_category} ({self.skill_level})"
