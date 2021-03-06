# Generated by Django 4.0.4 on 2022-05-18 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='Username', max_length=255, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=255, null=True)),
                ('role', models.CharField(blank=True, db_column='Role', max_length=255, null=True)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, db_column='City', max_length=255, null=True)),
                ('district', models.CharField(blank=True, db_column='District', max_length=255, null=True)),
                ('town', models.CharField(blank=True, db_column='Town', max_length=255, null=True)),
                ('street', models.CharField(blank=True, db_column='Street', max_length=255, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Contactinfo',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=255, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
            ],
            options={
                'db_table': 'contactinfo',
            },
        ),
        migrations.CreateModel(
            name='Fullname',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=255, null=True)),
                ('middlename', models.CharField(blank=True, db_column='MiddleName', max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=255, null=True)),
            ],
            options={
                'db_table': 'fullname',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('dateofbirth', models.DateField(blank=True, db_column='DateOfBirth', null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=255, null=True)),
                ('account', models.ForeignKey(db_column='AccountID', on_delete=django.db.models.deletion.CASCADE, to='apiroot.account')),
                ('address', models.ForeignKey(db_column='AddressID', on_delete=django.db.models.deletion.CASCADE, to='apiroot.address')),
                ('contactinfo', models.ForeignKey(db_column='ContactinfoID', on_delete=django.db.models.deletion.CASCADE, to='apiroot.contactinfo')),
                ('fullname', models.ForeignKey(db_column='FullnameID', on_delete=django.db.models.deletion.CASCADE, to='apiroot.fullname')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('position', models.CharField(blank=True, db_column='Position', max_length=255, null=True)),
                ('salary', models.BigIntegerField(blank=True, db_column='Salary', null=True)),
                ('startdate', models.DateField(blank=True, db_column='StartDate', null=True)),
                ('workingtime', models.IntegerField(blank=True, db_column='WorkingTime', null=True)),
                ('userid', models.OneToOneField(db_column='UserID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='apiroot.user')),
            ],
            options={
                'db_table': 'staffs',
            },
        ),
        migrations.CreateModel(
            name='Warehousestaff',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('userid', models.OneToOneField(db_column='UserID', on_delete=django.db.models.deletion.CASCADE, to='apiroot.user')),
            ],
            options={
                'db_table': 'warehousestaff',
            },
        ),
        migrations.CreateModel(
            name='Salesstaff',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('userid', models.OneToOneField(db_column='UserID', on_delete=django.db.models.deletion.CASCADE, to='apiroot.user')),
            ],
            options={
                'db_table': 'salesstaff',
            },
        ),
    ]
