from django.db import models

# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=120)
    state = models.CharField(max_length=120, null=True, help_text='i.e. MA')
    city = models.CharField(max_length=120, null=True)
    house = models.CharField(max_length=120, null=True, help_text='Home Alley')
    lanes = models.IntegerField(null=True)


class Bowler(models.Model):
    first = models.CharField(max_length=60)
    middle = models.CharField(max_length=60)
    last = models.CharField(max_length=60)
    birthdate = models.DateField(name="Birth Date")
    gender = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60, help_text='i.e. MA')
    zipcode = models.IntegerField()
    email = models.EmailField()
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    avg = models.IntegerField()
    hdcp = models.IntegerField()

    # def __unicode__(self):
    #     return u'%s %s' % (self.first, self.last)


class Team(models.Model):
    name = models.CharField(max_length=120)
    avg = models.FloatField()
    hdcp = models.FloatField()
    bowler = models.ManyToManyField(Bowler, name="Bowler(s)")
    # bowler2 = models.OneToOneField(Bowler, on_delete=models.CASCADE)
    # bowler3 = models.OneToOneField(Bowler, on_delete=models.CASCADE)
    # bowler4 = models.OneToOneField(Bowler, on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField(max_length=255)


class Stat(models.Model):
    customerid = models.ForeignKey(Bowler, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    game1 = models.IntegerField()
    game2 = models.IntegerField()
    game3 = models.IntegerField()
    total = models.IntegerField()
    avg = models.FloatField()
    hdcp = models.FloatField()
