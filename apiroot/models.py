from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=255, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        db_table = 'account'


class Address(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # producerid = models.ForeignKey('Producer', models.CASCADE, db_column='ProducerID')  # Field name made lowercase.
    # userid = models.ForeignKey('User', models.CASCADE, db_column='UserID')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    town = models.CharField(db_column='Town', max_length=255, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'address'

class Fullname(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # bookproductid = models.ForeignKey(Book, models.CASCADE, db_column='BookProductID')  # Field name made lowercase.
    # userid = models.ForeignKey('User', models.CASCADE, db_column='UserID')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'fullname'

class Contactinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # userid = models.ForeignKey('User', models.CASCADE, db_column='UserID')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'contactinfo'

class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    account = models.ForeignKey(Account, models.CASCADE, db_column='AccountID')
    contactinfo = models.ForeignKey(Contactinfo, models.CASCADE, db_column='ContactinfoID')
    address  = models.ForeignKey(Address, models.CASCADE, db_column='AddressID')
    fullname = models.ForeignKey(Fullname, models.CASCADE, db_column='FullnameID')
    class Meta:
        db_table = 'user'





class Staffs(models.Model):
    position = models.CharField(db_column='Position', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salary = models.BigIntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    workingtime = models.IntegerField(db_column='WorkingTime', blank=True, null=True)  # Field name made lowercase.
    userid = models.OneToOneField('User', models.CASCADE, db_column='UserID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'staffs'


class Warehousestaff(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.OneToOneField(User, models.CASCADE, db_column='UserID')  # Field name made lowercase.

    class Meta:
        
        db_table = 'warehousestaff'




class Salesstaff(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.OneToOneField('User', models.CASCADE, db_column='UserID')  # Field name made lowercase.

    class Meta:
        
        db_table = 'salesstaff'

# class Book(models.Model):
#     page = models.IntegerField(db_column='Page', blank=True, null=True)  # Field name made lowercase.
#     author = models.ForeignKey('Fullname', models.CASCADE, db_column='AuthorFullname')   # Field name made lowercase.
#     genre = models.IntegerField(db_column='Genre', blank=True, null=True)  # Field name made lowercase.
#     quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
#     productid = models.OneToOneField('Product', models.CASCADE, db_column='ProductID', primary_key=True)  # Field name made lowercase.

#     class Meta:
        
#         db_table = 'book'