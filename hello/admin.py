from django.contrib import admin
from .models import UserProfile, ShoeFeatures, WomenShoeFeatures, OrderTransaction

UserProfile._meta.verbose_name = "User account"
ShoeFeatures._meta.verbose_name = "Men products"
WomenShoeFeatures._meta.verbose_name = "Women products"
OrderTransaction._meta.verbose_name = "Received order"


class ShoeFeaturesAdmin(admin.ModelAdmin):
    search_fields = ['product_id','type1' ,'type2', 'maincolor','subcolor', 'subcolor2','size', 'price','brand','productImage','description','short_description','productName','InStock', 'product_idName','material']
    list_display = ('product_idName', 'brand', 'productName', 'material', 'InStock')

class WomenShoeFeaturesAdmin(admin.ModelAdmin):
    search_fields = ['product_id','type1' ,'type2', 'maincolor','subcolor', 'subcolor2','size', 'price','brand','productImage','description','short_description','productName','InStock', 'product_idName','material']
    list_display = ('product_idName', 'brand', 'productName', 'material', 'InStock')

class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ['birthdate','phoneno', 'address', 'address1', 'city', 'state','zip_code','user__email','user__username','user__first_name','user__last_name']
    list_display = ('user', 'get_firstname','get_lastname','get_email', 'phoneno')
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_firstname(self, obj):
        return obj.user.first_name
    get_firstname.short_description = 'First Name'

    def get_lastname(self, obj):
        return obj.user.last_name
    get_lastname.short_description = 'Last Name'

class OrderTransactionAdmin(admin.ModelAdmin):
    search_fields = [
        'username', 'productName',
        'product_quantity', 'main_color', 'sub_color',
        'product_size', 'payment_method', 'created_by', 'delivery_status',
        'total_amount_vat'
    ]
    list_display = ( 'username', 'productName',
        'product_quantity', 'main_color', 'sub_color',
        'product_size', 'payment_method', 'created_by', 'delivery_status',
        'total_amount_vat')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ShoeFeatures, ShoeFeaturesAdmin)
admin.site.register(WomenShoeFeatures, WomenShoeFeaturesAdmin)
admin.site.register(OrderTransaction,OrderTransactionAdmin)