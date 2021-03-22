"""soin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from portals import views as portal_views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', include('vet.urls')),
    path('admin/', admin.site.urls, name='admin-vet'),
    #users sign up
    path('user/signup/vet_officer/', user_views.VetOfficerSignUpView.as_view(), name='vet-register'),
    path('user/signup/farmer/',user_views.FarmerSignUpView.as_view(),name='farmer_register'),
    path('user/signup/student/',user_views.StudentSignUpView.as_view(),name='student_register'),
    #users login 
    path('user/login/',user_views.user_login,name='login'),
    path('logout/', user_views.user_logout, name='logout'),

    #users portals
    path('vet_portal/', portal_views.portal_vet, name='vet-portal'),
    path('farmer_portal/', portal_views.portal_farmer, name='farmer-portal'),
    path('student_portal/', portal_views.portal_student, name='student-portal'),
    #vet forms
    path('clinical_approach/',portal_views.clinical_approach,name='clinical-approach'),
    path('sick_approach', portal_views.sick_approach, name='sick-approach'),
    path('dead_approach', portal_views.dead_approach, name='dead-approach'),
    path('surgical_approach',portal_views.surgical_approach, name='surgical-approach'),
    path('deworming',portal_views.deworming,name='deworming'),
    path('vaccination',portal_views.vaccination,name='vaccination'),
    path('breeding_record/',portal_views.breeding_record,name='breeding_record'),
    path('artificial_insemination', portal_views.artificial_insemination, name='artificial-insemination'),
    path('pregnancy_diagnosis',portal_views.pregnancy_diagnosis,name='pregnancy_diagnosis'),
    path('calf_registration', portal_views.calf_registration, name='calf-registration'),
    path('livestock_inventory', portal_views.livestock_inventory, name='livestock-inventory'),
    path('consultation',portal_views.consultation,name='consultation'),
    path('sickform/', login_required(portal_views.Sick_Form_Pdf.as_view()), name='sickform'),
    path('deadform/', login_required(portal_views.Dead_Form_Pdf.as_view()), name='deadformpdf'),
    path('surgicalform/', login_required(portal_views.Surgical_Form_Pdf.as_view()), name='surgicalformpdf'),
    path('dewormingform/', login_required(portal_views.Deworming_Form_Pdf.as_view()), name='dewormingformpdf'),
    path('artificialform/', login_required(portal_views.Artificial_Insemination_Form_Pdf.as_view()), name='artificialform'),
    path('vaccinationform/', login_required(portal_views.Vaccination_Form_Pdf.as_view()), name='vaccinationform'),
    path('deadform/', login_required(portal_views.Dead_Form_Pdf.as_view()), name='deadform'),
    path('surgicalform/', login_required(portal_views.Surgical_Form_Pdf.as_view()), name='surgicalform'),
    path('dewormingform/', login_required(portal_views.Deworming_Form_Pdf.as_view()), name='dewormingform'),
    path('artificialform/', login_required(portal_views.Artificial_Insemination_Form_Pdf.as_view()), name='artificialformpdf'),
    path('vaccinationpdf/', login_required(portal_views.Vaccination_Form_Pdf.as_view()), name='vaccinationformpdf'),
    path('consultationform/', login_required(portal_views.Farm_Consultation_Form_Pdf.as_view()), name='consultationform'),
    path('pregnancyform/', login_required(portal_views.Pregnancy_Diagnosis_Form_Pdf.as_view()), name='pregnancyform'),
    path('gallery/', portal_views.display_images, name='display-images')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)