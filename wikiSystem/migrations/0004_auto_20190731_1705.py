# Generated by Django 2.2.3 on 2019-07-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiSystem', '0003_auto_20190730_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pages',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
