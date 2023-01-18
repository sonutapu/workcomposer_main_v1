from django.db import models

# Create your models here.

class user_table(models.Model):
    emp_id=models.BigIntegerField(null=True)  ##if u take sqllite then take integer field
    username=models.CharField(max_length=100,null=True)
    fname=models.CharField(max_length=100,null=True)
    lname=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    pass1=models.CharField(max_length=100,null=True)
    pass2=models.CharField(max_length=100,null=True)
    teamname=models.CharField(max_length=100,null=True)
    user_id = models.BigIntegerField(null=True)
    created_on=models.DateTimeField(null=True)
    isactive=models.BooleanField("1") 
    
    class Meta:
        db_table:"user_table"


class master_table(models.Model):
    User_Type=models.CharField(max_length=100,null=True)
    is_active=models.BooleanField(max_length=100,null=True)
    
    class Meta:
        db_table:"master_table"


class Logtable_time(models.Model):
    master_id=models.IntegerField(null=True)
    Date=models.DateField(blank=True,null=True)
    user_id = models.IntegerField(null=True)
    login_time=models.TimeField(null=True)
    logout_time = models.TimeField(null=True)
    # duration=models.DurationField(null=True)
    idle_time=models.TimeField(null=True)
    class Meta:
        db_table:"Logtable_time"

class team_table(models.Model):
    Team_Name=models.CharField(max_length=100,null=True)
    Is_Active=models.BooleanField(max_length=100,null=True)
    Create_on=models.DateTimeField()
    
    class Meta:
        db_table:"team_table"

class project_table(models.Model):
    # master_id=models.IntegerField(null=True)
    Project_Name=models.CharField(max_length=100,null=True)
    Assigned_Team=models.CharField(max_length=100,null=True)
    Create_on=models.DateTimeField()
    Created_by=models.CharField(max_length=100,null=True)
    
    class Meta:
        db_table:"project_table"

# class mouse_idle_time():
#     idletime= models.CharField(max_length=100,null=True)
    
#     class Meta:
#         db_table:"mouse_idle_time"