# Generated by Django 3.2.15 on 2022-09-21 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_informationeffect_new_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinformation',
            old_name='railroad',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='companypaintscheme',
            old_name='railroad',
            new_name='company',
        ),
        migrations.AlterField(
            model_name='comment',
            name='replies_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='core.comment', verbose_name='The comment which this one is replying to'),
        ),
    ]