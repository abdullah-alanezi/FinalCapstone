from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StartUp(models.Model):

    sectors = models.TextChoices('sectors',['Energy','Healthcare','Real Estate','Pharma & Biotech','Chemicals','Environment Services','Industrial & Manufacturing','Agriculture & Food Processing','Financial Services','Transport & Logistics','Mining & Metals','Tourism & Quality of Life','Information & Communication Technology','Human Capital Innovation','Aerospace & Defense'])

    user = models.ForeignKey(User,on_delete = models.CASCADE)
    startup_name = models.CharField(max_length = 2048)
    startup_avatar = models.ImageField(upload_to='images/',default='iamges/default.jpg')
    startup_sector = models.CharField(max_length= 1024,choices= sectors.choices)
    startup_websits = models.TextField()
    startup_email = models.CharField(max_length=2048)
    startup_number = models.CharField(max_length=1024)
    startup_description = models.TextField()
    startup_founder_name = models.CharField(max_length=1024)
    startup_target_market = models.TextField()

    def __str__(self) -> str:
        return f'Startup name {self.startup_name}'



class TeamMember(models.Model):

    startup = models.ForeignKey(StartUp,on_delete=models.CASCADE)
    team_name = models.CharField(max_length=1024)
    team_avatar = models.ImageField(upload_to='images/',default='iamges/default.jpg')
    team_role = models.CharField(max_length=2048)
    team_linkdin = models.TextField()
    #member_cv = models.FileField()

    def __str__(self) -> str:
        return f'Team member name is {self.team_name}'


class FundingRound(models.Model):

    statuss = models.TextChoices('statuss',['Close','Open'])
    stages = models.TextChoices('stages',['Pre_Seed','Seed','Series A','Series B','Series C','Series D','Mezzanine','IPO'])

    startup = models.ForeignKey(StartUp,on_delete=models.CASCADE)
    fund_percentage = models.FloatField()
    fund_amount = models.IntegerField()
    fund_status = models.CharField(max_length=1024,choices=statuss.choices)
    fund_current_close = models.FloatField()
    fund_stage = models.CharField(max_length=1024,choices=stages.choices)

    def __str__(self) -> str:
        return f'Round for {self.startup.startup_name} in {self.fund_stage} stage'