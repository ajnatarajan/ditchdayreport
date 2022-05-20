from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        """User database"""
        return "User: {} {}".format(self.first_name, self.last_name)


class Report(models.Model):
    report_text = models.TextField()
    negative_attitude_opt = models.BooleanField(default=False)
    trolling_opt = models.BooleanField(default=False)
    verbal_abuse_opt = models.BooleanField(default=False)
    unskilled_player_opt = models.BooleanField(default=False)
    is_andy_tong_opt = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Report database"""
        return self.report_text
