# Generated by Django 5.0.6 on 2024-06-07 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_department2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department2',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='size',
            field=models.IntegerField(default=15),
            preserve_default=False,
        ),
    ]
