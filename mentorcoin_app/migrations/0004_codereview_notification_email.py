# Generated by Django 2.0 on 2018-02-17 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorcoin_app', '0003_auto_20180217_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='codereview',
            name='notification_email',
            field=models.EmailField(default='jordan@example.com', max_length=254),
            preserve_default=False,
        ),
    ]