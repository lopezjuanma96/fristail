# Generated by Django 4.2.4 on 2023-08-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(max_length=200, verbose_name='text')),
                ('word_lang', models.CharField(max_length=50, verbose_name='language')),
                ('word_freq', models.FloatField(default=1.0, verbose_name='frequency')),
                ('word_date', models.DateTimeField(auto_now_add=True, verbose_name='posted date')),
            ],
        ),
    ]
