# Generated by Django 4.1.7 on 2023-03-31 15:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Surname', models.CharField(default='', max_length=20)),
                ('Name', models.CharField(default='', max_length=20)),
                ('Patronic', models.CharField(default='', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientContactDetails',
            fields=[
                ('ID_contact_categories', models.CharField(default='', max_length=40)),
                ('Contact', models.CharField(default='', max_length=40)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='contact_categories',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name_category', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='procedure',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name_procedure', models.CharField(default='', max_length=40)),
                ('description', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Recording_window',
            fields=[
                ('Start_time', models.TimeField(blank=True, null=True)),
                ('End_time', models.TimeField(blank=True, null=True)),
                ('Date', models.TimeField(blank=True, null=True)),
                ('ID_specialist', models.CharField(default='', max_length=40)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ID_client', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Surname', models.CharField(default='', max_length=20)),
                ('Name', models.CharField(default='', max_length=20)),
                ('Patronic', models.CharField(default='', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='specialist_procedure',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ID_specialist', models.CharField(default='', max_length=40)),
                ('ID_procedure', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialistAdress',
            fields=[
                ('City', models.CharField(default='', max_length=20)),
                ('Street', models.CharField(default='', max_length=20)),
                ('House', models.CharField(default='', max_length=10)),
                ('ID_specialist', models.CharField(default='', max_length=40)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialistContactDetails',
            fields=[
                ('ID_contact_categories', models.CharField(default='', max_length=40)),
                ('Contact', models.CharField(default='', max_length=40)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
