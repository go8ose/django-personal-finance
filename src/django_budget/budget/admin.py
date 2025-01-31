from __future__ import unicode_literals
from django.contrib import admin
from django_budget.budget.models import Budget, BudgetEstimate


class BudgetAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_date'
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'start_date'),
        }),
        ('Metadata', {
            'classes': ('collapse',),
            'fields': ('created', 'updated', 'is_deleted')
        })
    )
    list_display = ('name', 'start_date', 'is_deleted')
    list_filter = ('is_deleted',)
    prepopulated_fields = {
        'slug': ('name',),
    }
    search_fields = ('name',)
    readonly_fields = ['created', 'updated']


class BudgetEstimateAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('budget', 'category', 'amount'),
        }),
        ('Metadata', {
            'classes': ('collapse',),
            'fields': ('created', 'updated', 'is_deleted')
        })
    )
    list_display = ('category', 'budget', 'amount', 'is_deleted')
    list_filter = ('is_deleted',)
    readonly_fields = ['created', 'updated']


admin.site.register(Budget, BudgetAdmin)
admin.site.register(BudgetEstimate, BudgetEstimateAdmin)
