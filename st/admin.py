from django.contrib import admin
from st.models import Message

"""
class MemberAdmin(admin.ModelAdmin):
	list_display = ('mem_full_name_ar', 'mem_current_points', 'mem_weekly_added_points')
	ordering = ('mem_first_name_ar', 'mem_last_name_ar')
	list_editable = ('mem_weekly_added_points',)
	readonly_fields = ('mem_last_points', 'mem_current_order_in_names', 'mem_last_order_in_names', 'mem_full_name_en', 'mem_full_name_ar',)

class ActivityAdmin(admin.ModelAdmin):
	list_display = ('activity_week_number', 'activity_image', 'day_one_ar', 'day_two_ar', 'day_three_ar', 'day_four_ar', 'day_five_ar', 'day_one_en', 'day_two_en', 'day_three_en', 'day_four_en', 'day_five_en')
	list_editable = ('activity_image', 'day_one_ar', 'day_two_ar', 'day_three_ar', 'day_four_ar', 'day_five_ar', 'day_one_en', 'day_two_en', 'day_three_en', 'day_four_en', 'day_five_en')
"""

admin.site.site_header = 'SigTech Administration'
#admin.site.register(Member, MemberAdmin)
#admin.site.register(Activity, ActivityAdmin)
admin.site.register(Message)
