# Generated by Django 4.2.2 on 2023-06-10 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_rename_des1_people_des_rename_img1_people_img_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='des',
            new_name='des1',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='img',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='name',
            new_name='name1',
        ),
    ]
