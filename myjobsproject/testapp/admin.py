from django.contrib import admin
from testapp.models import HydJobs,VizagJobs,BngJobs
# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','tittle','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)

class VizagJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','tittle','eligibility','address','email','phonenumber']
admin.site.register(VizagJobs,VizagJobsAdmin)

class BngJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','tittle','eligibility','address','email','phonenumber']
admin.site.register(BngJobs,BngJobsAdmin)
