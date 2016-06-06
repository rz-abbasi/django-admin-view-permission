from django.contrib import admin
from admin_view_permission import admin as view_admin
from .models import *


## Modeladmin for the UI
class StackedModelAdmin(admin.StackedInline):
    model = TestModel2


class TabularModelAdmin(admin.TabularInline):
    model = TestModel3


class DefaultModelAdmin(admin.ModelAdmin):
    inlines = [
        StackedModelAdmin,
        TabularModelAdmin
    ]


## Modeladmin for testing
class InlineModelAdmin1(view_admin.AdminViewPermissionInlineModelAdmin):
    model = TestModel4


class InlineModelAdmin2(view_admin.AdminViewPermissionInlineModelAdmin):
    model = TestModel6


class ModelAdmin1(view_admin.AdminViewPermissionModelAdmin):
    inlines = [
        StackedModelAdmin,
        TabularModelAdmin,
    ]


class ModelAdmin2(view_admin.AdminViewPermissionModelAdmin):
    inlines = [
        InlineModelAdmin1,
        InlineModelAdmin2
    ]


admin.site.register(TestModel1, DefaultModelAdmin)
