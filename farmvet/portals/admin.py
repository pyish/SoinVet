from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from .views import get_valid_access_token  # your function
import requests
from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.contrib.admin.views.autocomplete import AutocompleteJsonView
from .models import (
   ApprovedDairyFarm, Question, CpdQuestions, Moderator, CpdChoices,
    Section, Tutorial, Attempt, UserRetake,ZoomMeeting
)
User = get_user_model()
@admin.register(ZoomMeeting)
class ZoomMeetingAdmin(admin.ModelAdmin):
    change_list_template = "admin/zoom_changelist.html"
    list_display = ("topic", "facilitator", "price","start_time", "is_paid", "user")
    list_filter = ("is_paid", "start_time")
    search_fields = ("topic", "meeting_id")

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("schedule/", self.admin_site.admin_view(self.schedule_zoom), name="schedule_zoom"),
        ]
        return custom_urls + urls

    # ----------------------
    # Custom admin view handler
    # ----------------------
    def schedule_zoom(self, request):
        
        # 1) Check authentication before showing form
        access_token = get_valid_access_token(request.user)

        if not access_token:
            messages.warning(request, "Please authenticate with Zoom before scheduling a meeting.")
            return redirect("zoom-auth")   # <-- Make sure this URL exists

        # 2) If authenticated, handle POST or show form
        if request.method == "POST":
            topic = request.POST.get("topic")
            start_time = request.POST.get("start_time")
            price = request.POST.get("price")
            facilitator = request.POST.get("facilitator")

            # Convert price to Decimal
            from decimal import Decimal
            try:
                price = Decimal(price)
            except:
                price = 0

            url = "https://api.zoom.us/v2/users/me/meetings"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            }
            payload = {
                "topic": topic,
                "type": 2,
                "start_time": start_time,
                "duration": 30,
                "timezone": "Africa/Nairobi",
            }

            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 201:
                meeting = response.json()

                ZoomMeeting.objects.create(
                    user=request.user,
                    facilitator=facilitator or request.user.get_full_name(),
                    meeting_id=meeting["id"],
                    topic=meeting["topic"],
                    price=price,
                    is_paid=False,
                    start_time=meeting["start_time"],
                    join_url=meeting["join_url"],
                )

                messages.success(request, "Zoom meeting created successfully.")
                return redirect("/admin/portals/zoommeeting/")

            else:
                messages.error(request, f"Zoom API Error: {response.text}")
                return redirect(request.path)

        # 3) GET request: render form with extra fields
        return render(request, "admin/schedule_meeting.html")

class CustomAutocompleteJsonView(AutocompleteJsonView):
    def __init__(self, model_admin=None, **kwargs):
        self.model_admin = model_admin
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class ModeratorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        # Check if a moderator with the same name already exists
        if Moderator.objects.filter(name=obj.name).exists():
            raise ValidationError(f"A moderator with the name '{obj.name}' already exists.")
        super().save_model(request, obj, form, change)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'moderator', 'correct_answer')
    list_filter = ('correct_answer', 'moderator')
    search_fields = ('text', 'moderator__name')
    fieldsets = (
        ('Question Details', {
            'fields': ('moderator', 'text')
        }),
        ('Options', {
            'fields': ('option_a', 'option_b', 'option_c', 'option_d', 'correct_answer')
        }),
    )
    autocomplete_fields = ('moderator',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('autocomplete/', self.admin_site.admin_view(CustomAutocompleteJsonView.as_view(model_admin=self)), name='your_app_name_question_autocomplete'),
        ]
        return custom_urls + urls

@admin.register(UserRetake)
class UserRetakeAdmin(admin.ModelAdmin):
    list_display = ('user', 'retakes_left')
    actions = ['reset_retakes']

    def reset_retakes(self, request, queryset):
        for user_retake in queryset:
            user_retake.reset_retakes()
        self.message_user(request, "Retakes have been reset to 3 for selected users.")

    reset_retakes.short_description = "Reset retakes to 3"

class CpdAnswersAdmin(admin.StackedInline):
    model = CpdChoices


class CpdQuestionsAdmin(admin.ModelAdmin):
    inlines = [CpdAnswersAdmin]







class TutorialAdmin(admin.ModelAdmin):
    change_list_template = "admin/tutorial_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "manage/",
                self.admin_site.admin_view(self.custom_view),
                name="portals_tutorial_manage"
            ),
        ]
        return custom_urls + urls

    def custom_view(self, request):
        changelist = self.get_changelist_instance(request)
        context = dict(
            self.admin_site.each_context(request),
            cl=changelist,
        )

        # ➤ ADD NEW TUTORIAL
        if request.method == "POST" and "add_new" in request.POST:
            Tutorial.objects.create(
                user=request.user,
                lesson=request.POST.get("new_lesson"),
                cpd_number=request.POST.get("new_cpd_number"),
                unit_price=request.POST.get("new_unit_price"),
                points=request.POST.get("new_points"),
                presented_by=request.POST.get("new_presented_by"),
                contact_hours=request.POST.get("new_contact_hours"),
                is_paid=("new_paid" in request.POST),
            )
            messages.success(request, "Tutorial added successfully!")

        # ➤ UPDATE ALL TUTORIALS
        if request.method == "POST" and "save_all" in request.POST:
            for obj in Tutorial.objects.all():
                obj.lesson = request.POST.get(f"lesson_{obj.id}")
                obj.cpd_number = request.POST.get(f"cpd_{obj.id}")
                obj.unit_price = request.POST.get(f"price_{obj.id}")
                obj.points = request.POST.get(f"points_{obj.id}")
                obj.presented_by = request.POST.get(f"presented_{obj.id}")
                obj.contact_hours = request.POST.get(f"contact_hours_{obj.id}")
                obj.is_paid = (f"paid_{obj.id}" in request.POST)
                obj.save()
            messages.success(request, "All tutorials updated successfully!")

        return TemplateResponse(request, "admin/tutorial_changelist.html", context)



admin.site.register(Tutorial, TutorialAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'file', 'content')
    search_fields = ('title',)
    list_filter = ('lesson',)
    fields = ('lesson', 'title', 'content', 'file')
    autocomplete_fields = ('lesson',)

    def get_urls(self):
        """
        Override get_urls to use the custom autocomplete view for the 'lesson' field.
        """
        urls = super().get_urls()
        custom_urls = [
            path('autocomplete/', self.admin_site.admin_view(CustomAutocompleteJsonView.as_view(model_admin=self)), name='your_app_name_section_autocomplete'),
        ]
        return custom_urls + urls
# Register other models
admin.site.register(Attempt)
admin.site.register(Question)
admin.site.register(Moderator)
admin.site.register(CpdChoices)
admin.site.register(ApprovedDairyFarm)
#admin.site.register(Deworming)
#admin.site.register(ArtificialInsemination)
#admin.site.register(PregnancyDiagnosis)
#admin.site.register(FarmConsultation)
#admin.site.register(Referral)

admin.site.register(Section)
admin.site.register(CpdQuestions)
