# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pods', '0011_new_contributorpod'),
    ]

    operations = [
        migrations.AddField(
            model_name='pod',
            name='is_360',
            field=models.BooleanField(default=False, verbose_name='video 360'),
        ),
    ]
