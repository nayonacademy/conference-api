# Generated by Django 3.0.2 on 2020-07-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200719_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='conference',
            name='address',
            field=models.CharField(max_length=244),
        ),
        migrations.AlterField(
            model_name='conference',
            name='name',
            field=models.CharField(max_length=244),
        ),
        migrations.AlterField(
            model_name='conference',
            name='website',
            field=models.CharField(max_length=244),
        ),
    ]
