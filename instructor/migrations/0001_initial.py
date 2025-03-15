# Generated by Django 5.1.7 on 2025-03-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertise', models.CharField(max_length=200)),
                ('experience', models.PositiveIntegerField()),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
