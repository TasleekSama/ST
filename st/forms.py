from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from st.models import Message
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


# class based forms


class EditMessageForm(forms.Form):
	msg_sender_name = forms.CharField()
	msg_sender_email = forms.EmailField()
	msg_subject = forms.CharField()
	msg_content = forms.CharField()

"""
class EditMemberForm(forms.Form):
	uid = forms.CharField()
	first_name_en = forms.CharField()
	first_name_ar = forms.CharField()
	mid_name_en = forms.CharField()
	mid_name_ar = forms.CharField()
	last_name_en = forms.CharField()
	last_name_ar = forms.CharField()
	major_en = forms.CharField()
	major_ar = forms.CharField()
	phone = forms.CharField()
"""