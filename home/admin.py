from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.html import format_html
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','payment_type','product','totalAmount','orderDetails','cardDetails','status','deliveredAt','createdAt')
    list_display_links = ('order_id',)
    list_editable = ('status',)
    list_filter = ['status','payment_type','product','isPaid']
    date_hierarchy = 'createdAt'
    list_per_page = 15
    readonly_fields  = ['order_id','payment_type','totalAmount','product']
    def orderDetails(self,obj):
        #model name has to be lowercase
        return format_html(u'<a href="/admin/home/customerdetails/?order__id__exact=%s">%s</a>' % (obj.pk,"Order Details"))
    orderDetails.allow_tags=True

    def cardDetails(self,obj):
        #model name has to be lowercase
        if obj.payment_type == "Card":
            return format_html(u'<a href="/admin/home/card/?order__id__exact=%s">%s</a>' % (obj.pk,"Card Details"))
        else:
            return format_html(u'<p>-</p>')
    orderDetails.allow_tags=True



admin.site.register(Order,OrderAdmin)


class DetailsAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','order','email','contact_no','address','city','zipcode','state','country','createdAt')
    list_display_links = ('first_name','email')
    
admin.site.register(CustomerDetails,DetailsAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','package','extra')
    list_display_links = ('name',)
admin.site.register(Product,ProductAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ('name','number','order','expiry_date','cvc')
    list_display_links = ('name','number')
    
admin.site.register(Card,CardAdmin)