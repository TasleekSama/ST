from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext as _
from datetime import date
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.timezone import now
#from model_utils import FieldTracker


# class based models

"""
class Member(models.Model):
	mem_uid = models.CharField(max_length=9, null=True, blank=True, default='')
	mem_full_name_en = models.CharField(max_length=100, null=True, blank=True, default='')
	mem_full_name_ar = models.CharField(max_length=100, null=True, blank=True, default='')
	mem_first_name_en = models.CharField(max_length=50, null=True, blank=True, default='')
	mem_first_name_ar = models.CharField(max_length=50, null=True, blank=True, default='')
	mem_last_name_en = models.CharField(max_length=50, null=True, blank=True, default='')
	mem_last_name_ar = models.CharField(max_length=50, null=True, blank=True, default='')
	mem_current_points = models.IntegerField(null=True, blank=True, default=0)
	mem_last_points = models.IntegerField(null=True, blank=True, default=0)
	mem_last_weekly_added_points = models.IntegerField(null=True, blank=True, default=0)
	mem_weekly_added_points = models.IntegerField(null=True, blank=True, default=0)
	mem_current_order_in_names = models.IntegerField(null=True, blank=True, default=0)
	mem_last_order_in_names = models.IntegerField(null=True, blank=True, default=0)
	tracker = FieldTracker()


	def __str__(self):
	    if self.mem_first_name_ar and self.mem_last_name_ar:
	        return self.mem_first_name_ar + ' ' + self.mem_last_name_ar
	    elif self.mem_first_name_en and self.mem_last_name_en:
		    return self.mem_first_name_en + ' ' + self.mem_last_name_en

    
	def save(self, *args, **kwargs):

		self.mem_full_name_ar = self.mem_first_name_ar + ' ' + self.mem_last_name_ar
		self.mem_full_name_en = self.mem_first_name_en + ' ' + self.mem_last_name_en

		self.mem_current_points = self.mem_current_points + self.mem_weekly_added_points

		self.mem_last_points = self.tracker.previous('mem_current_points')

		self.mem_last_weekly_added_points = self.mem_weekly_added_points

		self.mem_weekly_added_points = 0

		super(Member, self).save(*args, **kwargs)


class Activity(models.Model):
	activity_week_number = models.IntegerField(null=True, blank=True, default=0)
	activity_name_ar = models.CharField(max_length=200, null=True, blank=True, default='')
	activity_name_en = models.CharField(max_length=200, null=True, blank=True, default='')
	activity_date = models.DateField(_("Date"), null=True, blank=True, default=date.today)
	activity_image = models.CharField(max_length=200, null=True, blank=True, default='')
	day_one_ar = models.CharField(max_length=200, null=True, blank=True, default='')
	day_two_ar = models.CharField(max_length=200, null=True, blank=True, default='')
	day_three_ar = models.CharField(max_length=200, null=True, blank=True, default='')
	day_four_ar = models.CharField(max_length=200, null=True, blank=True, default='')
	day_five_ar = models.CharField(max_length=200, null=True, blank=True, default='')
	day_one_en = models.CharField(max_length=200, null=True, blank=True, default='')
	day_two_en = models.CharField(max_length=200, null=True, blank=True, default='')
	day_three_en = models.CharField(max_length=200, null=True, blank=True, default='')
	day_four_en = models.CharField(max_length=200, null=True, blank=True, default='')
	day_five_en = models.CharField(max_length=200, null=True, blank=True, default='')


	def __str__(self):
	    if self.activity_name_ar:
	        return self.activity_name_ar
	    elif self.activity_name_en:
	    	return self.activity_name_en
	    else:
	    	return ""
"""

class Message(models.Model):
	msg_sender_name = models.CharField(max_length=100, null=True, blank=True, default='')
	msg_sender_email = models.EmailField(max_length=70, null=True, blank=True, default='')
	msg_subject = models.CharField(max_length=100, null=True, blank=True, default='')
	msg_content = models.TextField(null=True, blank=True, default='')
	msg_date_time = models.DateTimeField(default=now, blank=True) #implicit attribute


	def __str__(self):
	    if self.msg_sender_name:
	        return self.msg_sender_name
	    return ''
