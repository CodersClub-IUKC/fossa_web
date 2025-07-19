from django.contrib import admin
from django.utils.html import format_html
from .models import ContactMessage, Event, Testimonial, Gallery, Cabinet,Course

# Admin for ContactMessage
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

# Admin for Event
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'photo_preview')  

    def photo_preview(self, obj):
        if obj.image:  
            return format_html('<img src="{}" style="height: 40px; border-radius: 5px;" />', obj.image.url)
        return "No Photo"
    photo_preview.short_description = 'Photo'

# Admin for Testimonial
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at')

# Admin for Gallery
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'photo_preview')  # Added photo preview

    def photo_preview(self, obj):
        if obj.image:  # Use 'image' instead of 'photo'
            return format_html('<img src="{}" style="height: 40px; border-radius: 5px;" />', obj.image.url)
        return "No Photo"
    photo_preview.short_description = 'Photo'

# Admin for Cabinet
@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    list_display = ('role', 'name', 'photo_preview')  

    def photo_preview(self, obj):
        if obj.image: 
            return format_html('<img src="{}" style="height: 40px; border-radius: 5px;" />', obj.image.url)
        return "No Photo"
    photo_preview.short_description = 'Photo'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description') 
    list_filter = ('title', 'description')