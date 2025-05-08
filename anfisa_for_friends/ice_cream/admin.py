from django.contrib import admin

from .models import Category, Topping, Wrapper, IceCream


admin.site.empty_value_display = 'Не задано'


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category', 'is_published')
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)
    inlines = ()


class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0
    fields = ('title', 'is_published', 'is_on_main', 'category', 'wrapper')
    show_change_link = True


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title', 'slug', 'output_order'
    )


class WrapperAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper, WrapperAdmin)
admin.site.register(IceCream, IceCreamAdmin)
