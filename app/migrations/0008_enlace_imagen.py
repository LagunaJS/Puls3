# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_enlace_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlace',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'enlaces/', blank=True),
        ),
    ]
