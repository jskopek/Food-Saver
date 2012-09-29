from django.contrib import admin
from receipts.models import Receipt


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at', 'number_products')

    def number_products(self, obj):
        return obj.products.count()

admin.site.register(Receipt, ReceiptAdmin)
