# Generated by Django 4.0.4 on 2022-05-20 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_report_delete_reports_rename_users_user_report_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='is_andy_tong_opt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='negative_attitude_opt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='trolling_opt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='unskilled_player_opt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='verbal_abuse_opt',
            field=models.BooleanField(default=False),
        ),
    ]
