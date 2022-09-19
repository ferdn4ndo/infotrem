# Generated by Django 3.2.15 on 2022-09-18 03:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformationVote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Record primary key (UUID v4)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Record creation timestamp')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Record last update timestamp')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Vote value')),
            ],
        ),
    ]
