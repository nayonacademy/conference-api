# Generated by Django 3.0.2 on 2020-07-19 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('conference_name', models.CharField(max_length=100)),
                ('street_address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipCode', models.CharField(max_length=100)),
                ('speakers', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('organizerID', models.CharField(max_length=100)),
                ('locations', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('speaker', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ConfOwnProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.CharField(max_length=100)),
                ('reads', models.CharField(max_length=100)),
                ('useful', models.CharField(max_length=100)),
                ('attend', models.CharField(max_length=100)),
                ('favourite', models.CharField(max_length=100)),
                ('picture', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offensive', models.CharField(max_length=100)),
                ('violence', models.CharField(max_length=100)),
                ('spam', models.CharField(max_length=100)),
                ('appropriate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=100)),
                ('attendQ', models.CharField(max_length=100)),
                ('enjoyQ', models.CharField(max_length=100)),
                ('locationQ', models.CharField(max_length=100)),
                ('connectPeerQ', models.CharField(max_length=100)),
                ('awesome', models.CharField(max_length=100)),
                ('great', models.CharField(max_length=100)),
                ('average', models.CharField(max_length=100)),
                ('poor', models.CharField(max_length=100)),
                ('terrible', models.CharField(max_length=100)),
                ('favorite', models.CharField(max_length=100)),
                ('like', models.CharField(max_length=100)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Conference')),
            ],
        ),
    ]
