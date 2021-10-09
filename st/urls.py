from django.urls import path, re_path
from st import views
from django.contrib.auth import views as auth_views

app_name = 'st'

urlpatterns = [

	# home main paths:

	path('', views.home_page_en, name='home_page_en'),
	path('services/', views.services_page_en, name='services_page_en'),
	path('contact_us/', views.contact_us_page_en, name='contact_us_page_en'),
	path('company_profile/', views.company_profile_page_en, name='company_profile_page_en'),
	#path('en/', views.home_en, name='home_en'),

]