# Generated by Django 3.1.1 on 2020-10-27 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='True', max_length=10),
        ),
    ]
