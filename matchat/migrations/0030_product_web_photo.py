# Generated by Django 3.2.13 on 2022-05-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchat', '0029_product_web_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='web_photo',
            field=models.CharField(blank=True, max_length=2090, null=True),
        ),
    ]
