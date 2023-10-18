# Generated by Django 4.2.4 on 2023-10-18 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0004_sentimenttexts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translatetexts',
            name='language_code_destiny',
            field=models.CharField(choices=[('fr', 'francaise'), ('de', 'deutch'), ('en', 'english'), ('zh-Hans', 'chinese')], max_length=7),
        ),
    ]