# Generated by Django 3.1.5 on 2021-06-22 15:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created date')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('type', models.CharField(max_length=4)),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operations.member')),
            ],
        ),
    ]
