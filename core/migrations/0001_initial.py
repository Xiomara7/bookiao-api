# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookiaoUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('bookiaouser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('manager_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.bookiaouser',),
        ),
        migrations.CreateModel(
            name='BusinessHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weekday', models.IntegerField(choices=[(1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday'), (7, b'Sunday')])),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('business', models.ForeignKey(to='core.Business')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('bookiaouser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.bookiaouser',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('bookiaouser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('business', models.ForeignKey(to='core.Business')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.bookiaouser',),
        ),
        migrations.CreateModel(
            name='EmployeeHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weekday', models.IntegerField(choices=[(1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday'), (7, b'Sunday')])),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('lunch_hour_start', models.TimeField()),
                ('lunch_hour_end', models.TimeField()),
                ('employee', models.ForeignKey(to='core.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('duration_in_minutes', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='employeehours',
            unique_together=set([('employee', 'weekday')]),
        ),
        migrations.AddField(
            model_name='employee',
            name='services',
            field=models.ManyToManyField(to='core.Services'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='businesshours',
            unique_together=set([('business', 'weekday')]),
        ),
        migrations.AddField(
            model_name='appointments',
            name='client',
            field=models.ForeignKey(to='core.Client'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointments',
            name='employee',
            field=models.ForeignKey(to='core.Employee'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointments',
            name='services',
            field=models.ManyToManyField(to='core.Services'),
            preserve_default=True,
        ),
    ]
