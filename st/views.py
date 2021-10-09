from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from st.models import Message
from st.forms import (
  EditMessageForm,
)
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core import signing
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.debug import sensitive_post_parameters


# function based views


# home_main views


def home_page_en(request):

    if request.method == 'POST':

        form = EditMessageForm(request.POST)

        sender_name = request.POST.get('name', '')
        sender_email = request.POST.get('email', '')
        sender_subject = request.POST.get('subject', '')
        content = request.POST.get('message', '')

        msg_obj = Message(msg_sender_name=sender_name, msg_sender_email=sender_email, msg_subject=sender_subject, msg_content=content)

        msg_obj.save()

        return redirect('/')

    else:

        #members = Member.objects.all().order_by('-mem_current_points')
        #count = Member.objects.all().count()

        #total_points = 0

        #for member in members:
        #    total_points = total_points + member.mem_current_points

        #avr_points = total_points * 1.1 / count

        #avr_zero_point_seven = 0.7 * avr_points

        #activities = Activity.objects.all().order_by('activity_week_number')

        form = EditMessageForm()

        #return render(request, 'st/index.html', {'form': form, 'members': members, 'activities': activities, 'avr_points': avr_points, 'avr_zero_point_seven': avr_zero_point_seven})
        return render(request, 'st/index.html')

def services_page_en(request):

    if request.method == 'POST':

        form = EditMessageForm(request.POST)

        sender_name = request.POST.get('name', '')
        sender_email = request.POST.get('email', '')
        sender_subject = request.POST.get('subject', '')
        content = request.POST.get('message', '')

        msg_obj = Message(msg_sender_name=sender_name, msg_sender_email=sender_email, msg_subject=sender_subject, msg_content=content)

        msg_obj.save()

        return redirect('/services')

    else:

        #members = Member.objects.all().order_by('-mem_current_points')
        #count = Member.objects.all().count()

        #total_points = 0

        #for member in members:
        #    total_points = total_points + member.mem_current_points

        #avr_points = total_points * 1.1 / count

        #avr_zero_point_seven = 0.7 * avr_points

        #activities = Activity.objects.all().order_by('activity_week_number')

        form = EditMessageForm()

        #return render(request, 'st/index.html', {'form': form, 'members': members, 'activities': activities, 'avr_points': avr_points, 'avr_zero_point_seven': avr_zero_point_seven})
        return render(request, 'st/services.html')

def contact_us_page_en(request):

    if request.method == 'POST':

        form = EditMessageForm(request.POST)

        sender_name = request.POST.get('name', '')
        sender_email = request.POST.get('email', '')
        sender_subject = request.POST.get('subject', '')
        content = request.POST.get('message', '')

        msg_obj = Message(msg_sender_name=sender_name, msg_sender_email=sender_email, msg_subject=sender_subject, msg_content=content)

        msg_obj.save()

        return redirect('/contact_us')

    else:

        #members = Member.objects.all().order_by('-mem_current_points')
        #count = Member.objects.all().count()

        #total_points = 0

        #for member in members:
        #    total_points = total_points + member.mem_current_points

        #avr_points = total_points * 1.1 / count

        #avr_zero_point_seven = 0.7 * avr_points

        #activities = Activity.objects.all().order_by('activity_week_number')

        form = EditMessageForm()

        #return render(request, 'st/index.html', {'form': form, 'members': members, 'activities': activities, 'avr_points': avr_points, 'avr_zero_point_seven': avr_zero_point_seven})
        return render(request, 'st/contact.html')


def company_profile_page_en(request):

    if request.method == 'POST':

        form = EditMessageForm(request.POST)

        sender_name = request.POST.get('name', '')
        sender_email = request.POST.get('email', '')
        sender_subject = request.POST.get('subject', '')
        content = request.POST.get('message', '')

        msg_obj = Message(msg_sender_name=sender_name, msg_sender_email=sender_email, msg_subject=sender_subject, msg_content=content)

        msg_obj.save()

        return redirect('/company_profile')

    else:

        #members = Member.objects.all().order_by('-mem_current_points')
        #count = Member.objects.all().count()

        #total_points = 0

        #for member in members:
        #    total_points = total_points + member.mem_current_points

        #avr_points = total_points * 1.1 / count

        #avr_zero_point_seven = 0.7 * avr_points

        #activities = Activity.objects.all().order_by('activity_week_number')

        form = EditMessageForm()

        #return render(request, 'st/index.html', {'form': form, 'members': members, 'activities': activities, 'avr_points': avr_points, 'avr_zero_point_seven': avr_zero_point_seven})
        return render(request, 'st/profile.html')
"""
def home_en(request):

    if request.method == 'POST':

        form = EditMessageForm(request.POST)

        sender_name = request.POST.get('name', '')
        sender_email = request.POST.get('email', '')
        content = request.POST.get('message', '')

        msg_obj = Message(msg_sender_name=sender_name, msg_sender_email=sender_email, msg_content=content)

        msg_obj.save()

        return redirect('/en/')

    else:

        members = Member.objects.all().order_by('-mem_current_points')
        count = Member.objects.all().count()

        total_points = 0

        for member in members:
            total_points = total_points + member.mem_current_points

        avr_points = total_points * 1.1 / count

        avr_zero_point_seven = 0.7 * avr_points

        activities = Activity.objects.all().order_by('activity_week_number')

        form = EditMessageForm()

        return render(request, 'home/index_en.html', {'form': form, 'members': members, 'activities': activities, 'avr_points': avr_points, 'avr_zero_point_seven': avr_zero_point_seven})
"""

"""
def home_main_en(request):
    if request.method == 'POST':
        form = EditMessageForm(request.POST)

        sender_name = request.POST.get('name', '')
        sender_email = request.POST.get('email', '')
        content = request.POST.get('message', '')

        msg_obj = Message(msg_sender_name=sender_name, msg_sender_email=sender_email, msg_content=content)

        msg_obj.save()

        email = EmailMessage('sender_name', 'content', to=['sadxsad91@gmail.com'])
        email.send()

        return redirect('/en/')

    else:
        form = EditMessageForm()

        return render(request, 'home/home_main_en.html', {'form': form})


def home_main_ar(request):
    if request.method == 'POST':
        form = EditMessageForm(request.POST)

        sender_name = request.POST.get('name', '')
        sender_email = request.POST.get('email', '')
        content = request.POST.get('message', '')

        msg_obj = Message(msg_sender_name=sender_name, msg_sender_email=sender_email, msg_content=content)

        msg_obj.save()

        return redirect('/')

    else:
        form = EditMessageForm()

        return render(request, 'home/home_main_ar.html', {'form': form})


# activity_pages views


def activity_main_en(request):
    if request.method == 'POST':
        form = EditMessageForm(request.POST)

        sender_name = request.POST.get('name', '')
        sender_email = request.POST.get('email', '')
        content = request.POST.get('message', '')

        msg_obj = Message(msg_sender_name=sender_name, msg_sender_email=sender_email, msg_content=content)

        msg_obj.save()

        return redirect('/activity_main_en/')

    else:
        form = EditMessageForm()

        activities = Activity.objects.all()

        args = {'form': form, 'activities': activities}

        return render(request, 'home/activity_main_en.html', args)


def activity_main_ar(request):
    if request.method == 'POST':
        form = EditMessageForm(request.POST)

        sender_name = request.POST.get('name', '')
        sender_email = request.POST.get('email', '')
        content = request.POST.get('message', '')

        msg_obj = Message(msg_sender_name=sender_name, msg_sender_email=sender_email, msg_content=content)

        msg_obj.save()

        return redirect('/activity_main_ar/')

    else:
        form = EditMessageForm()

        activities = Activity.objects.all()

        args = {'form': form, 'activities': activities}

        return render(request, 'home/activity_main_ar.html', args)


# edit_user_profile views


@login_required(login_url='/accounts/login_en/')
def edit_user_profile_en(request):
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST)

        fna = request.POST.get('first_name_ar', '')
        fne = request.POST.get('first_name_en', '')
        mna = request.POST.get('mid_name_ar', '')
        mne = request.POST.get('mid_name_en', '')
        lna = request.POST.get('last_name_ar', '')
        lne = request.POST.get('last_name_en', '')
        uid = request.POST.get('uid', '')
        ma = request.POST.get('major_ar', '')
        me = request.POST.get('major_en', '')
        #email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        user_profile = UserProfile.objects.get(user=request.user)

        if fna:
            user_profile.mem_first_name_ar = fna

        if fne:
            user_profile.mem_first_name_en = fne

        if mna:
            user_profile.mem_mid_name_ar = mna

        if mne:
            user_profile.mem_mid_name_en = mne

        if lna:
            user_profile.mem_last_name_ar = lna

        if lne:
            user_profile.mem_last_name_en = lne

        if uid:
            user_profile.mem_uid = uid

        if ma:
            user_profile.mem_major_ar = ma

        if me:
            user_profile.mem_major_en = me

        #request.user.email = email

        if phone:
            user_profile.mem_phone = phone

        #request.user.save()
        user_profile.save()

        return redirect('/accounts/profile_en/')

    else:
        form = EditUserProfileForm()

        return render(request, 'home/edit_user_profile_en.html', {'form': form})


@login_required(login_url='/accounts/login_ar/')
def edit_user_profile_ar(request):
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST)

        fna = request.POST.get('first_name_ar', '')
        fne = request.POST.get('first_name_en', '')
        mna = request.POST.get('mid_name_ar', '')
        mne = request.POST.get('mid_name_en', '')
        lna = request.POST.get('last_name_ar', '')
        lne = request.POST.get('last_name_en', '')
        uid = request.POST.get('uid', '')
        ma = request.POST.get('major_ar', '')
        me = request.POST.get('major_en', '')
        #email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        user_profile = UserProfile.objects.get(user=request.user)

        if fna:
            user_profile.mem_first_name_ar = fna

        if fne:
            user_profile.mem_first_name_en = fne

        if mna:
            user_profile.mem_mid_name_ar = mna

        if mne:
            user_profile.mem_mid_name_en = mne

        if lna:
            user_profile.mem_last_name_ar = lna

        if lne:
            user_profile.mem_last_name_en = lne

        if uid:
            user_profile.mem_uid = uid

        if ma:
            user_profile.mem_major_ar = ma

        if me:
            user_profile.mem_major_en = me

        #request.user.email = email

        if phone:
            user_profile.mem_phone = phone

        #request.user.save()
        user_profile.save()

        return redirect('/accounts/profile_ar/')

    else:
        form = EditUserProfileForm()

        return render(request, 'home/edit_user_profile_ar.html', {'form': form})
"""