# Generated by Django 4.2.2 on 2023-06-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_emailcheckcode_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailcheckcode',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
