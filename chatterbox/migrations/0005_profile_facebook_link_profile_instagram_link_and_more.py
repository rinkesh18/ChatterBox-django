# Generated by Django 4.2.19 on 2025-02-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chatterbox", "0004_banter_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="facebook_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="instagram_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="linkdlen_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="profile_bio",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="profile_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
