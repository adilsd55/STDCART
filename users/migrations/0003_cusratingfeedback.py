# Generated by Django 4.2.3 on 2023-07-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CusRatingFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_code', models.IntegerField(default=1)),
                ('ratings', models.FloatField()),
                ('feedback', models.CharField(max_length=200)),
                ('user_type', models.CharField(default='users', max_length=200)),
            ],
        ),
    ]
