# Generated by Django 4.0.1 on 2022-01-13 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(choices=[('Science', 'Science'), ('English', 'English'), ('Math', 'Math'), ('Accounting', 'Accounting')], max_length=60)),
                ('Course_Number', models.DecimalField(decimal_places=0, default=0, max_digits=10000)),
                ('Instructor_Name', models.TextField(default='', max_length=300)),
                ('Duration', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
            ],
        ),
    ]
