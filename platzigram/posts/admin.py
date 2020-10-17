"""post admin classes"""

#Django
from django.contrib import admin

#Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""
    
    list_display = (
        'pk', 
        'user', 
        'profile', 
        'title', 
        'photo'
        )
    
    list_display_links = (
        'pk', 
        'user'
        )

    search_fields= (
        'user__username', 
        'title',
        )

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    readonly_fields = ('created', 'modified', 'user')

    fieldsets = (
        ('Post', {
            'fields': (('title', 'photo'),)
        }),

        ('Metadata', {
            'fields': (
                ('user'),
                ('created', 'modified'),
            )
        })
    )



