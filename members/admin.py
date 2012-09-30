from django.contrib import admin
from members.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'num_products', 'next_expiration')

    def num_products(self, obj):
        return len(obj.get_products())

    def next_expiration(self, obj):
        products = obj.get_perishables().order_by("expires_at")
        return products[0].expires_at if products.exists() else False

admin.site.register(Member, MemberAdmin)
