from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import (
    UserProfile, Category, 
    Complaint, ComplaintHistory, Feedback, Notification,
    Department, FacultyProfile, StudentProfile
)


class UserProfileInline(admin.StackedInline):
    """Inline admin for user profiles"""
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = ('role', 'phone', 'department')


class CustomUserAdmin(UserAdmin):
    """Custom user admin with profile inline"""
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_role', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined', 'profile__role')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    
    def get_role(self, obj):
        """Get user role from profile"""
        try:
            return obj.profile.get_role_display()
        except:
            return 'No Profile'
    get_role.short_description = 'Role'


# Unregister the default User admin and register our custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin for user profiles"""
    list_display = ('user', 'role', 'phone', 'department', 'created_at')
    list_filter = ('role', 'department', 'created_at')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone', 'department')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin for categories"""
    list_display = ('name', 'description', 'complaints_count', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    
    def complaints_count(self, obj):
        """Count of complaints in this category"""
        return obj.complaints.count()
    complaints_count.short_description = 'Complaints'


class ComplaintHistoryInline(admin.TabularInline):
    """Inline admin for complaint history"""
    model = ComplaintHistory
    extra = 0
    readonly_fields = ('changed_by', 'from_status', 'to_status', 'timestamp')
    fields = ('changed_by', 'from_status', 'to_status', 'remarks', 'timestamp')


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    """Admin for complaints"""
    list_display = (
        'complaint_no', 'title', 'user', 'assigned_to', 'status', 
        'priority', 'category', 'created_at', 'resolved_at'
    )
    list_filter = (
        'status', 'priority', 'category', 'assigned_to', 
        'created_at', 'resolved_at'
    )
    search_fields = (
        'complaint_no', 'title', 'description', 'user__username',
        'assigned_to__username', 'category__name'
    )
    readonly_fields = ('complaint_no', 'created_at', 'updated_at', 'resolved_at')
    inlines = [ComplaintHistoryInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('complaint_no', 'title', 'description', 'user')
        }),
        ('Classification', {
            'fields': ('category', 'priority')
        }),
        ('Assignment & Status', {
            'fields': ('assigned_to', 'status', 'resolved_at')
        }),
        ('Attachments & Remarks', {
            'fields': ('attachment', 'remarks', 'admin_remarks')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        """Optimize queryset"""
        return super().get_queryset(request).select_related(
            'user', 'assigned_to', 'category'
        )


@admin.register(ComplaintHistory)
class ComplaintHistoryAdmin(admin.ModelAdmin):
    """Admin for complaint history"""
    list_display = ('complaint', 'changed_by', 'from_status', 'to_status', 'timestamp')
    list_filter = ('from_status', 'to_status', 'timestamp')
    search_fields = ('complaint__complaint_no', 'complaint__title', 'changed_by__username')
    readonly_fields = ('timestamp',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Admin for feedback"""
    list_display = ('complaint', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('complaint__complaint_no', 'user__username', 'comments')
    readonly_fields = ('created_at',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Admin for notifications"""
    list_display = ('user', 'message_preview', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__username', 'message')
    readonly_fields = ('created_at',)
    
    def message_preview(self, obj):
        """Show message preview"""
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'


# Legacy model admins
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Admin for departments"""
    list_display = ('name', 'faculty_count', 'student_count')
    search_fields = ('name',)
    
    def faculty_count(self, obj):
        """Count of faculty in this department"""
        return obj.facultyprofile_set.count()
    faculty_count.short_description = 'Faculty'
    
    def student_count(self, obj):
        """Count of students in this department"""
        return obj.studentprofile_set.count()
    student_count.short_description = 'Students'


@admin.register(FacultyProfile)
class FacultyProfileAdmin(admin.ModelAdmin):
    """Admin for faculty profiles"""
    list_display = ('user', 'faculty_id', 'department', 'assigned_complaints_count')
    list_filter = ('department',)
    search_fields = ('user__username', 'faculty_id', 'department__name')
    
    def assigned_complaints_count(self, obj):
        """Count of assigned complaints"""
        return obj.user.assigned_complaints.count()
    assigned_complaints_count.short_description = 'Assigned Complaints'


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    """Admin for student profiles"""
    list_display = ('user', 'student_id', 'department', 'complaints_count')
    list_filter = ('department',)
    search_fields = ('user__username', 'student_id', 'department__name')
    
    def complaints_count(self, obj):
        """Count of complaints by this student"""
        return obj.user.complaints.count()
    complaints_count.short_description = 'Complaints'


# Customize admin site
admin.site.site_header = "Complaint Management System"
admin.site.site_title = "CMS Admin"
admin.site.index_title = "Welcome to Complaint Management System"