from django.contrib import admin
from .models import Category, Writer, Cake, Slider


class AddCategory(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, AddCategory)

class AddWriter(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Writer, AddWriter)

class AddCake(admin.ModelAdmin):
	list_display = ['name', 'price', 'stock', 'status', 'created', 'updated']
	list_filter = ['status', 'created', 'updated']
	list_editable = ['price', 'stock', 'status']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Cake, AddCake)

class AddSlider(admin.ModelAdmin):
	list_display = ['title', 'created', 'updated']
	#list_editable = ['title',]

admin.site.register(Slider, AddSlider) 