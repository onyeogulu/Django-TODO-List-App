# Generated by Django 4.2.4 on 2023-09-11 13:29

from django.db import migrations, models
import todoapplogin_app.models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapplogin_app", "0002_task_due_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="create",
            field=models.DateTimeField(
                blank=True, default=todoapplogin_app.models.now, null=True
            ),
        ),
    ]