from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.html import format_html
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','payment_id','totalProducts','unitAmount','totalAmount','orderDetails','status','deliveredAt','createdAt')
    list_display_links = ('order_id','payment_id')
    list_editable = ('status',)
    list_filter = ['status']
    date_hierarchy = 'createdAt'
    def get_queryset(self, request):
      qs = Order.objects.filter(isPaid=True)
     
      return qs
    def orderDetails(self,obj):
        #model name has to be lowercase
        return format_html(u'<a href="/admin/home/customerdetails/?order__id__exact=%s">%s</a>' % (obj.pk,"Order Details"))
    orderDetails.allow_tags=True



admin.site.register(Order,OrderAdmin)


class DetailsAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','order','email','contact_no','address','city','zipcode','state','country','createdAt')
    list_display_links = ('first_name','email')
    
admin.site.register(CustomerDetails,DetailsAdmin)