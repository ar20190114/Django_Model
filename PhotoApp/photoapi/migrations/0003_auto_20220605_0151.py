# Generated by Django 3.1 on 2022-06-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapi', '0002_auto_20220604_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoimagemodel',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='photoimagemodel',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='img'),
        ),
    ]