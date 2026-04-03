from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from portals import views as portal_views  
from portals.views import *
from portals.monitoring import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
app_name = 'portals'

def debug_view(request, *args, **kwargs):
    return HttpResponse(f"Args: {args}, Kwargs: {kwargs}")

urlpatterns = [
    path('debug/', debug_view, name='debug-view'),
    path('', include('vet.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls, name='admin-vet'),
    #users sign up
    path('user/signup/vet_officer/', user_views.vet0fficer_signup_view, name='vet-register'),
    path('user/signup/cooperative/', user_views.cooperative_signup_view, name='cooperative-register'),
    path('user/signup/farmer/',user_views.farmer_signup_view,name='farmer-register'),
    path('user/signup/official/',user_views.Official_signup_view,name='official-register'),
    #users login 
    path('vet/login/',user_views.vet_login,name='vet-login'),
    path('farmer/login/',user_views.farmer_login,name='farmer-login'),
    path('official/login/',user_views.official_login,name='official-login'),
     path('cooperative/login/',user_views.cooperative_login,name='cooperative-login'),
    path('logout/', user_views.user_logout, name='logout'),
    #password reset
    path("password-reset", auth_views.PasswordResetView.as_view(template_name="user/password_reset.html"), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view( template_name="user/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"), name="password_reset_complete"),

    #users portals
    path('vet_portal/', portal_views.portal_vet, name='vet-portal'),
    path('vet_list/', portal_views.vet_list, name='vet-list'),
    path('vet_list_vet/', portal_views.vet_list_vet, name='vet-list_vet'),
    path('farmer_portal/', portal_views.portal_farmer, name='farmer-portal'),
    path('official_portal/', portal_views.portal_official, name='official-portal'),
    path('cooperative_portal/', portal_views.cooperative, name='cooperative-portal'),

#################################FARMER  Urls######################################## 
    ##calf
    path('calf',  calf, name='calf'),
    path('calves-list', CalfList.as_view(), name='calves-list'),
    path('calves/create/',CalfCreate.as_view(), name='add_calf'),
    path('calves/update/<int:pk>/',CalfUpdate.as_view(), name='edit_calf'),
    path('calves/delete/<int:pk>/', CalfDelete.as_view(), name='remove_calf'),

# dead animal
    path('dead_animal/',  dead_animal, name='dead_animal'),
    path('dead-animal-list/', DeadAnimalList.as_view(), name='dead-animal-list'),
    path('dead-animal/create/', DeadAnimalCreate.as_view(), name='add-dead-animal'),
    path('dead-animal/update/<int:pk>/', DeadAnimalUpdate.as_view(), name='update_dead_animal'),
    path('dead-animal/delete/<int:pk>/', DeadAnimalDelete.as_view(), name='delete_dead_animal'),

# Culling
    path('culling/',  culling, name='culling'),
    path('culling-list/', CullingList.as_view(), name='culling-list'),
    path('culling/create/',  CullingCreate.as_view(), name='create_culling'),
    path('culling/update/<int:pk>/', CullingUpdate.as_view(), name='update_culling'),
    path('culling/delete/<int:pk>/', CullingDelete.as_view(), name='delete_culling'),
#  new animal
    path('new_animal/',  new_animal, name='new_animal'),
    path('new-animal-list/', NewAnimalList.as_view(), name='new-animal-list'),
    path('new-animal/create/', NewAnimalCreate.as_view(), name='add-new-animal'),
    path('new-animal/update/<int:pk>/',  NewAnimalUpdate.as_view(), name='edit-new-animal'),
    path('new-animal/delete/<int:pk>/', NewAnimalDelete.as_view(), name='remove-new-animal'),

# livestock inventory
    path('livestock/',  livestock, name='livestock'),
    path('livestock-list/',LivestockList.as_view(), name='livestock-list'),
    path('livestock/create/', LivestockCreate.as_view(), name='add-livestock'),
    path('livestock/update/<int:pk>/', LivestockUpdate.as_view(), name='edit-livestock'),
    path('livestock/delete/<int:pk>/', LivestockDelete.as_view(), name='remove-livestock'),

#sales of stock

    path('animal_sales/',  animal_sales, name='animal_sales'),
    path('animal-sales-list/', AnimalSaleList.as_view(), name='animal-sales-list'),
    path('animal-sales/create/', AnimalSaleCreate.as_view(), name='add-animal-sale'),
    path('animal-sales/update/<int:pk>/', AnimalSaleUpdate.as_view(), name='edit-animal-sale'),
    path('animal-sales/delete/<int:pk>/', AnimalSaleDelete.as_view(), name='delete-animal-sale'),
   
    path('heat-sign-monitoring/',  heat_sign_monitoring, name='heat_sign_monitoring'),
    path('heat-sign-monitoring-list/', HeatSignMonitoringList.as_view(), name='heat-sign-monitoring-list'),
    path('heat-sign-monitoring/create/', HeatSignMonitoringCreate.as_view(), name='add-heat-sign-monitoring'),
    path('heat-sign-monitoring/update/<int:pk>/', HeatSignMonitoringUpdate.as_view(), name='edit-heat-sign-monitoring'),
    path('heat-sign-monitoring/delete/<int:pk>/', HeatSignMonitoringDelete.as_view(), name='remove-heat-signmonitoring'),

    path('pregnancy-monitoring/',  pregnancy_monitoring, name='pregnancy_monitoring'),
    path('pregnancy-monitoring-list/', PregnancyMonitoringList.as_view(), name='pregnancy-monitoring-list'),
    path('pregnancy-monitoring/create/', PregnancyMonitoringCreate.as_view(), name='pregnancy-monitoring-create'),
    # path('pregnancy-monitoring/<int:pk>/', PregnancyMonitoringDetail.as_view(), name='pregnancy-monitoring-detail'),
    path('pregnancy-monitoring/update/<int:pk>/', PregnancyMonitoringUpdate.as_view(), name='pregnancy-monitoring-update'),
    path('pregnancy-monitoring/delete/<int:pk>/', PregnancyMonitoringDelete.as_view(), name='pregnancy-monitoring-delete'),


    #FEEDS
    path('feeds/',  feeds, name='feeds'),
    path('feeds-list/', FeedsList.as_view(), name='feeds-list'),
    path('feeds/create/', FeedsCreate.as_view(), name='feeds-create'),
    # path('pregnancy-monitoring/<int:pk>/', PregnancyMonitoringDetail.as_view(), name='pregnancy-monitoring-detail'),
    path('feeds/update/<int:pk>/',FeedsUpdate.as_view(), name='feeds-update'),
    path('feeds/delete/<int:pk>/', FeedsDelete.as_view(), name='feeds-delete'),

    path('equipment/',  equipment, name='dairy_equipment'),
    path('dairy-equipment/create/', DairyEquipmentCreate.as_view(), name='dairy_equipment_create'),
    path('dairy-equipment-list/', DairyEquipmentList.as_view(), name='dairy-equipment-list'),
    path('dairy-equipment/update/<int:pk>/', DairyEquipmentUpdate.as_view(), name='dairy_equipment_update'),
    path('dairy-equipment/delete/<int:pk>/', DairyEquipmentDelete.as_view(), name='dairy_equipment_delete'),

    # DairyHygiene URLs
    path('hygiene/',  hygiene, name='hygiene'),
    path('dairy-hygiene/create/', DairyHygieneCreate.as_view(), name='dairy_hygiene_create'),
    path('dairy-hygiene-list/', DairyHygieneList.as_view(), name='dairy-hygiene-list'),
    path('dairy-hygiene/update/<int:pk>/', DairyHygieneUpdate.as_view(), name='dairy_hygiene_update'),
    path('dairy-hygiene/delete/<int:pk>/', DairyHygieneDelete.as_view(), name='dairy_hygiene_delete'),

    # Salaries URLs
    path('salaries/',  salaries, name='salaries'),
    path('salaries/create/', SalariesCreate.as_view(), name='salaries_create'),
    path('salaries-list/', SalariesList.as_view(), name='salaries-list'),
    path('salaries/update/<int:pk>/', SalariesUpdate.as_view(), name='salaries_update'),
    path('salaries/delete/<int:pk>/', SalariesDelete.as_view(), name='salaries_delete'),

    # LivestockInsurance URLs
    path('insurance/',  insurance, name='insurance'),
    path('livestock-insurance/create/', LivestockInsuranceCreate.as_view(), name='livestock_insurance_create'),
    path('livestock-insurance-list/', LivestockInsuranceList.as_view(), name='livestock-insurance-list'),
    path('livestock-insurance/update/<int:pk>/', LivestockInsuranceUpdate.as_view(), name='livestock_insurance_update'),
    path('livestock-insurance/delete/<int:pk>/', LivestockInsuranceDelete.as_view(), name='livestock_insurance_delete'),

    # VeterinaryDrugs URLs
    path('drugs/',  drugs, name='drugs'),
    path('veterinary-drugs/create/', VeterinaryDrugsCreate.as_view(), name='veterinary_drugs_create'),
    path('veterinary-drugs-list/', VeterinaryDrugsList.as_view(), name='veterinary-drugs-list'),
    path('veterinary-drugs/update/<int:pk>/', VeterinaryDrugsUpdate.as_view(), name='veterinary_drugs_update'),
    path('veterinary-drugs/delete/<int:pk>/', VeterinaryDrugsDelete.as_view(), name='veterinary_drugs_delete'),

    #Expenses
    path('expenses/',  expenses, name='expenses'),
    
    path('other-expenses/',other_expenses_view, name='other-expenses-view'),
    path('other-expenses/create/', OtherExpenseCreate.as_view(), name='other-expense-create'),
    path('other-expenses/list/', OtherExpenseList.as_view(), name='other-expense-list'),
    path('other-expenses/update/<int:pk>/', OtherExpenseUpdate.as_view(), name='other-expense-update'),
    path('other-expenses/delete/<int:pk>/', OtherExpenseDelete.as_view(), name='other-expense-delete'),
     # Archaricides URLs
     
    path('archaricides/',  archaricides, name='archaricides'),
    path('archaricides/create/', ArcharicidesCreate.as_view(), name='archaricides_create'),
    path('archaricides-list/', ArcharicidesList.as_view(), name='archaricides-list'),
    path('archaricides/update/<int:pk>/', ArcharicidesUpdate.as_view(), name='archaricides_update'),
    path('archaricides/delete/<int:pk>/', ArcharicidesDelete.as_view(), name='archaricides_delete'),

    path('minerals/',  minerals, name='minerals'),
    path('minerals/create/', MineralsCreate.as_view(), name='minerals_create'),
    path('minerals-list/', MineralsList.as_view(), name='minerals-list'),
    path('minerals/update/<int:pk>/', MineralsUpdate.as_view(), name='minerals_update'),
    path('minerals/delete/<int:pk>/', MineralsDelete.as_view(), name='minerals_delete'),


     # VeterinaryBills URLs
    path('bills/',  vet_bills, name='bills'),
    path('veterinary-bills/create/', VeterinaryBillsCreate.as_view(), name='veterinary_bills_create'),
    path('veterinary-bills/', VeterinaryBillsList.as_view(), name='veterinary-bills-list'),
    path('veterinary-bills/update/<int:pk>/', VeterinaryBillsUpdate.as_view(), name='veterinary_bills_update'),
    path('veterinary-bills/delete/<int:pk>/', VeterinaryBillsDelete.as_view(), name='veterinary_bills_delete'),

    path('add-gestation/',  add_gestation, name='add_gestation'),
    path('gestation-detail/',  gestation_detail, name='gestation_detail'),
    path('gestation/',  gestation, name='gestation'),
    path('notes/',  pdf_notes, name='notes'),


    path('employees/',  employees, name='employees'),
    path('employees/create/', EmployeesCreate.as_view(), name='employees_create'),
    path('employees-list/', EmployeesList.as_view(), name='employees-list'),
    path('employees/update/<int:pk>/', EmployeesUpdate.as_view(), name='employees_update'),
    path('employees/delete/<int:pk>/', EmployeesDelete.as_view(), name='employees_delete'),

    path('lactation/',  lactation, name='lactation'),
    path('lactating-cows/create/', LactatingCowCreate.as_view(), name='lactatingcow-create'),
    path('lactating-cows/', LactatingCowList.as_view(), name='lactatingcow-list'),
    path('lactating-cows/update/<int:pk>/', LactatingCowUpdate.as_view(), name='lactatingcow-update'),
    path('lactating-cows/delete/<int:pk>/', LactatingCowDelete.as_view(), name='lactatingcow-delete'),


    path('milk-record/',  milk_record, name='milk-record'),
    path('milk-records/create/', MilkRecordCreate.as_view(), name='milkrecord-create'),
    path('milk-records/', MilkRecordList.as_view(), name='milkrecord-list'),
    path('milk-records/update/<int:pk>/', MilkRecordUpdate.as_view(), name='milkrecord-update'),
    path('milk-records/delete/<int:pk>/', MilkRecordDelete.as_view(), name='milkrecord-delete'),
    path('api/milk-records/filter/', FilteredMilkRecordsView.as_view(), name='filtered-milk-records'),
    
    path('weekly-record/',  weekly_record, name='weekly-record'),
    path('weekly-milk-records/', WeeklyMilkRecordListView.as_view(), name='weekly-milk-record-list'),
    path('monthly-record/',  monthly_record, name='monthly-record'),
    path('monthly-milk-records/', MonthlyMilkRecordListView.as_view(), name='monthly-milk-record-list'),
    path('weekly-milk-records/delete/<int:pk>/', WeeklyMilkRecordDelete.as_view(), name='weeklymilkrecord-update'),
    path('monthly-milk-records/delete/<int:pk>/', MonthlyMilkRecordDelete.as_view(), name='monthlymilkrecord-delete'),

    
    # Template view for buyers 
    path('buyer/', buyers, name='buyer'),

    # API endpoints
    path('buyers-category/', buyers_by_category, name='buyers-by-category'),

    path('buyers-category/', get_buyers_by_category, name='buyers-by-category'),
    path('buyers/create/', BuyerCreate.as_view(), name='buyer-create'),
    path('buyers/', BuyerList.as_view(), name='buyer-list'),
    path('buyers/update/<int:pk>/', BuyerUpdate.as_view(), name='buyer-update'),
    path('buyers/delete/<int:pk>/', BuyerDelete.as_view(), name='buyer-delete'),
    path('buyers-category/', get_buyers_by_category, name='buyers-by-category'),
    
    path('payments/', payments, name='payments'),
    path('payments/create/', PaymentsCreate.as_view(), name='payments-create'),
    path('payments/list/', PaymentsList.as_view(), name='payments-list'),
    path('payments/update/<int:pk>/', PaymentsUpdate.as_view(), name='payments-update'),
    path('payments/delete/<int:pk>/', PaymentsDelete.as_view(), name='payments-delete'),
    
    path('sales-of-milk/',  sales_of_milk, name='sales_of_milk'),
    path('sales-of-milk/create/', SalesOfMilkCreate.as_view(), name='sales_of_milk_create'),
    path('sales-of-milk/list/', SalesOfMilkList.as_view(), name='sales_of_milk_list'),
    path('sales-of-milk/update/<int:pk>/', SalesOfMilkUpdate.as_view(), name='sales_of_milk_update'),
    path('sales-of-milk/delete/<int:pk>/', SalesOfMilkDelete.as_view(), name='sales_of_milk_delete'),
    path('api/sales/<str:milk_type>/', SalesOfMilkList.as_view(), name='sales-of-milk-list'),

    path('daily-milk/',  daily_record, name='daily-record'),
    path('daily-milk/list/', DailyMilkRecordList.as_view(), name='daily-milk-list'),
    path('daily-milk/delete/<int:pk>/', DailyMilkRecordDelete.as_view(), name='daily-delete'),


    #################  VET URLs###############################################
     #vet billing
    path('vet-billing/',  vetbilling, name='vet-billing'),
    path('vet-billing-view/',  vetbilling_view, name='vet-billing-view'),
    path('vet-billing/create/', VeterinaryBillingCreate.as_view(), name='vet-billing-create'),
    path('vet-billing/list/', VeterinaryBillingList.as_view(), name='vet-billing-list'),
    path('vet-billing/update/<int:pk>/', VeterinaryBillingUpdate.as_view(), name='vet-billing-update'),
    path('vet-billing/delete/<int:pk>/', VeterinaryBillingDelete.as_view(), name='vet-billing-delete'),

    # Deworming URLs
    path('deworming/',  deworming, name='deworming'),
    path('deworming-view/',  deworming_view, name='deworming-view'),
    path('deworming/create/', DewormingCreate.as_view(), name='deworming-create'),
    path('deworming/list/', DewormingList.as_view(), name='deworming-list'),
    path('deworming/update/<int:pk>/', DewormingUpdate.as_view(), name='deworming-update'),
    path('deworming/delete/<int:pk>/', DewormingDelete.as_view(), name='deworming-delete'),

    # Artificial Insemination URLs
    path('ai/',  artificial, name='ai'),
     path('ai-official/',  artificial_official_view, name='ai_official'),
     path('ai-coop/',  artificial_coop_view, name='ai_coop'),
    path('ai-view/',  artificial_view, name='ai-view'),
    path('ai_filter/',  ai_record_filter, name='ai-filter'),
    path('artificial-insemination/create/', ArtificialInseminationCreate.as_view(), name='ai-create'),
    path('artificial-insemination/list/', ArtificialInseminationList.as_view(), name='ai-list'),
    path('artificial-insemination/update/<int:pk>/', ArtificialInseminationUpdate.as_view(), name='ai-update'),
    path('artificial-insemination/delete/<int:pk>/', ArtificialInseminationDelete.as_view(), name='ai-delete'),

    # Pregnancy Diagnosis URLs
    path('pregnanacy-diag/',  pregdiagnosis, name='pregnancy-diag'),
    path('pregnanacy-view/',  pregdiagnosis_view, name='pregnancy-view'),
    path('pregnancy-diagnosis/create/', PregnancyDiagnosisCreate.as_view(), name='pd-create'),
    path('pregnancy-diagnosis/list/', PregnancyDiagnosisList.as_view(), name='pd-list'),
    path('pregnancy-diagnosis/update/<int:pk>/', PregnancyDiagnosisUpdate.as_view(), name='pd-update'),
    path('pregnancy-diagnosis/delete/<int:pk>/', PregnancyDiagnosisDelete.as_view(), name='pd-delete'),

    # Farm Consultation URLs
    path('consultation/',  consultation, name='consultation'),
    path('consultation-view/',  consultation_view, name='consultation-view'),
    path('farm-consultation/create/', FarmConsultationCreate.as_view(), name='fc-create'),
    path('farm-consultation/list/', FarmConsultationList.as_view(), name='fc-list'),
    path('farm-consultation/update/<int:pk>/', FarmConsultationUpdate.as_view(), name='fc-update'),
    path('farm-consultation/delete/<int:pk>/', FarmConsultationDelete.as_view(), name='fc-delete'),

    # Referral URLs
    path('referral/', referral,name='referral'),
    path('referral-view/', referral_view,name='referral-view'),
    path('referral/create/', ReferralCreate.as_view(), name='referral-create'),
    path('referral/list/', ReferralList.as_view(), name='referral-list'),
    path('referral/update/<int:pk>/', ReferralUpdate.as_view(), name='referral-update'),
    path('referral/delete/<int:pk>/', ReferralDelete.as_view(), name='referral-delete'),

     # SampleCollection URLs
    path('collection/',  sample_collection, name='collection'),
    path('collection-view/',  sample_collection_view, name='collection-view'),
    path('sample-collection/create/', SampleCollectionCreate.as_view(), name='sample-collection-create'),
    path('sample-collection/list/', SampleCollectionList.as_view(), name='sample-collection-list'),
    path('sample-collection/update/<int:pk>/', SampleCollectionUpdate.as_view(), name='sample-collection-update'),
    path('sample-collection/delete/<int:pk>/', SampleCollectionDelete.as_view(), name='sample-collection-delete'),

    # SampleProcessing URLs
    path('processing/',  sample_processing, name='processing'),
    path('processing-view/',  sample_processing_view, name='processing-view'),
    path('sample-processing/create/', SampleProcessingCreate.as_view(), name='sample-processing-create'),
    path('sample-processing/list/', SampleProcessingList.as_view(), name='sample-processing-list'),
    path('sample-processing/update/<int:pk>/', SampleProcessingUpdate.as_view(), name='sample-processing-update'),
    path('sample-processing/delete/<int:pk>/', SampleProcessingDelete.as_view(), name='sample-processing-delete'),


    # LaboratoryRecord URLs
    path('lab-record/',  lab_record, name='lab-record'),
    path('lab-record-view/',  lab_record_view, name='lab-record-view'),
    path('laboratory-record/create/', LaboratoryRecordCreate.as_view(), name='laboratory-record-create'),
    path('laboratory-record/list/', LaboratoryRecordList.as_view(), name='laboratory-record-list'),
    path('laboratory-record/update/<int:pk>/', LaboratoryRecordUpdate.as_view(), name='laboratory-record-update'),
    path('laboratory-record/delete/<int:pk>/', LaboratoryRecordDelete.as_view(), name='laboratory-record-delete'),

    path('incident/',  incidence_record, name='incident'),
    path('incident-view/',  incidence_view, name='incident-view'),
    path('incidents/create/', LivestockIncidentCreate.as_view(), name='livestock_incident_create'),
    path('incidents/', LivestockIncidentList.as_view(), name='livestock_incident_list'),
    path('incidents/update/<int:pk>/', LivestockIncidentUpdate.as_view(), name='livestock_incident_update'),
    path('incidents/delete/<int:pk>/', LivestockIncidentDelete.as_view(), name='livestock_incident_delete'),

    path('postmortem/',  post_mortem, name='postmortem'),
    path('postmortem-view/',  post_mortem_view, name='postmortem-view'),
    path('postmortem/create/', PostMortemRecordCreate.as_view(), name='postmortem-create'),
    path('postmortem/list/', PostMortemRecordList.as_view(), name='postmortem-list'),
    path('postmortem/update/<int:pk>/', PostMortemRecordgUpdate.as_view(), name='postmortem-update'),
    path('postmortem/delete/<int:pk>/', PostMortemRecordDelete.as_view(), name='postmortem-delete'),

    path('vaccination/',  vaccination, name='vaccination'),
    path('vaccination-view/',  vaccination_view, name='vaccination-view'),
    path('vaccination_official/',  vaccination_official_view, name='vaccination-official'),
    path('vaccination-records/', VaccinationRecordList.as_view(), name='vaccination-record-list'),
    path('vaccination_filter/',  vaccination_record_filter, name='vaccination-filter'),
    path('vaccination-records/create/', VaccinationRecordCreate.as_view(), name='vaccination-record-create'),
    path('vaccination-records/update/<int:pk>/', VaccinationRecordUpdate.as_view(), name='vaccination-record-update'),
    path('vaccination-records/delete/<int:pk>/', VaccinationRecordDelete.as_view(), name='vaccination-record-delete'),

    path('surgery/',  surgical_record, name='surgery'),  
    path('surgery-view/',  surgical_view, name='surgery-view'),  
    path('surgical-record/create/', SurgicalRecordCreate.as_view(), name='surgical_record_create'),
    path('surgical-record/list/', SurgicalRecordList.as_view(), name='surgical_record_list'),
    path('surgical-record/update/<int:pk>/', SurgicalRecordUpdate.as_view(), name='surgical_record_update'),
    path('surgical-record/delete/<int:pk>/',SurgicalRecordDelete.as_view(), name='surgical_record_delete'),
    
    path('clinical/',  clinical, name='clinical'),  
    path('clinical-view/',  clinical_view, name='clinical-view'), 
    path('clinical-record/create/', ClinicalRecordCreate.as_view(), name='clinical-record-create'),
    path('clinical-record/', ClinicalRecordList.as_view(), name='clinical-record-list'),
    path('clinical-record/update/<int:pk>/', ClinicalRecordUpdate.as_view(), name='clinical-record-update'),
    path('clinical-record/delete/<int:pk>/', ClinicalRecordDelete.as_view(), name='clinical-record-delete'),

    path('calving/', calving_record, name='calving-record'),
    path('calving-record/create/', CalvingRecordCreate.as_view(), name='calving-record-create'),
    path('calving-record/list/', CalvingRecordList.as_view(), name='calving-record-list'),
    path('calving-record/update/<int:pk>/', CalvingRecordUpdate.as_view(), name='calving-record-update'),
    path('calving-record/delete/<int:pk>/', CalvingRecordDelete.as_view(), name='calving-record-delete'),
    path('clients/',  client, name='clients'),
    path('clients/create/', ClientCreate.as_view(), name='client-create'),
    path('clients/', ClientList.as_view(), name='client-list'),
    path('clients/update/<int:pk>/', ClientUpdate.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientDelete.as_view(), name='client_delete'),

    path('diary/',  diary, name='diary'),
    path('diaries/create/', DiaryCreate.as_view(), name='diary-create'),
    path('diaries/', DiaryList.as_view(), name='diary-list'),
    path('diaries/update/<int:pk>/', DiaryUpdate.as_view(), name='diary_update'),
    path('diaries/delete/<int:pk>/', DiaryDelete.as_view(), name='diary_delete'),
    ##############Shop######################
    
    path('shop/',  shop, name='shop'),
    path('resources/',  resources, name='resources'),
    
    path('disease-reports/', disease_report, name='disease-report'),
    path('disease-reports/view/', disease_report_view, name='disease-report-view'),
    path('disease-reports/list', DiseaseReportList.as_view(), name='disease-report-list'),
    path('disease-reports/create/', DiseaseReportCreate.as_view(), name='disease-report-create'),
    path('disease-reports/update/<int:pk>/', DiseaseReportUpdate.as_view(), name='disease-report-update'),
    path('disease-reports/delete/<int:pk>/', DiseaseReportDelete.as_view(), name='disease-report-delete'),

    path('slaughterhouse/', slaughterhouse, name='slaughterhouse'),
    path('slaughterhouse_view/', slaughterhouse_view, name='slaughterhouse-view'),
    path('slaughterhouse/create/', SlaughterhouseCreate.as_view(), name='slaughterhouse_create'),
    path('slaughterhouse/list/', SlaughterhouseList.as_view(), name='slaughterhouse_list'),
    path('slaughterhouse/update/<int:pk>/', SlaughterhouseUpdate.as_view(), name='slaughterhouse_update'),
    path('slaughterhouse/delete/<int:pk>/', SlaughterhouseDelete.as_view(), name='slaughterhouse_delete'),
    
    # Employee URLs
    path('employee/', employee, name='employee'),
    path('employee-view/', employee_view, name='employee-view'),
    path('employee/create/', EmployeeCreate.as_view(), name='employee_create'),
    path('employee/list/', EmployeeList.as_view(), name='employee_list'),
    path('employee/update/<int:pk>/', EmployeeUpdate.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>/', EmployeeDelete.as_view(), name='employee_delete'),
    
    # Butcher URLs
    path('butcher/', butcher, name='butcher'),
    path('butcher_view/', butcher_view, name='butcher-view'),
    path('butcher/create/', ButcherCreate.as_view(), name='butcher_create'),
    path('butcher/list/', ButcherList.as_view(), name='butcher_list'),
    path('butcher/update/<int:pk>/', ButcherUpdate.as_view(), name='butcher_update'),
    path('butcher/delete/<int:pk>/', ButcherDelete.as_view(), name='butcher_delete'),
    
    # Invoice URLs
    path('invoice/', invoice, name='invoice'),
    path('invoice-view',invoice_view, name='invoiceview'),
    path('invoice/create/', InvoiceCreate.as_view(), name='invoice_create'),
    path('invoice/list/', InvoiceList.as_view(), name='invoice_list'),
    path('invoice/update/<int:pk>/', InvoiceUpdate.as_view(), name='invoice_update'),
    path('invoice/delete/<int:pk>/', InvoiceDelete.as_view(), name='invoice_delete'),

    # questions
    path('quiz/', quiz_page, name='quiz'),
    path('score/', score, name='score'),
    path('start_quiz/', start_quiz, name='start-quiz'),
    path('submit_quiz/', submit_quiz, name='submit-quiz'),
    
    # path('questions/', QuestionListView.as_view(), name='question-list'),
    #path('submit-answer/', SubmitAnswerView.as_view(), name='submit-answer'),
    path('cpd/', tutorial, name='cpd'),
    path('cpdtest/', tutorialtest, name='cpdtest'),
    path('lessons/', lesson, name='lessons'),
    path('tutorials/create/', TutorialCreate.as_view(), name='tutorial-create'),
    path('tutorials/list/', TutorialList.as_view(), name='tutorial-list'),
    path('tutorials/update/<int:pk>/', TutorialUpdate.as_view(), name='tutorial-update'),
    path('tutorials/delete/<int:pk>/', TutorialDelete.as_view(), name='tutorial-delete'),
    path('questions/create/', QuestionCreateAPIView.as_view(), name='question-create'),
    path('questions/<int:section_id>/', QuizView.as_view(), name='questions-list'),   
    path('questions/submit/<int:section_id>/', QuizSubmit.as_view(), name='questions-submit'),
    path('questions/res/', QuizResultList.as_view(), name='questions-res'),  
    path('download/<int:section_id>/', download_file, name='download_file'),
    path('questions/result/', result, name='questions-result'),
    
    path('sections/<int:lesson_id>/', SectionList.as_view(), name='section-list'),
    path('sections/comments/create/<int:section_id>/', CommentCreateView.as_view(), name='comment-create'),
    path('sections/comments/<int:section_id>/', CommentListView.as_view(), name='comment-list'),
    path('sections/create/', SectionCreate.as_view(), name='section-create'),
    
    path('examination/', livestock_examination, name='livestock-examination'),
    path('livestock-examination/create/', LivestockExaminationCreate.as_view(), name='livestock-examination-create'),
    path('livestock-examination/list/', LivestockExaminationList.as_view(), name='livestock-examination-list'),
    path('livestock-examination/update/<int:pk>/', LivestockExaminationUpdate.as_view(), name='livestock-examination-update'),
    path('livestock-examination/delete/<int:pk>/', LivestockExaminationDelete.as_view(), name='livestock-examination-delete'),

    
    path('calving/', calving_record, name='calving-record'),
    path('calving-record/create/', CalvingRecordCreate.as_view(), name='calving-record-create'),
    path('calving-record/list/', CalvingRecordList.as_view(), name='calving-record-list'),
    path('calving-record/update/<int:pk>/', CalvingRecordUpdate.as_view(), name='calving-record-update'),
    path('calving-record/delete/<int:pk>/', CalvingRecordDelete.as_view(), name='calving-record-delete'),
    
    path('livestock-examination/', assessment_record, name='assesment-record-page'),
    path('livestock-examination/view', assessment_record_view, name='assesment-view'),
    path('assesment-records/create/', AssessmentRecordCreate.as_view(), name='assesment-record-create'),
    path('assesment-records/list/', AssessmentRecordList.as_view(), name='assesment-record-list'),
    path('assesment-records/update/<int:pk>/', AssessmentRecordUpdate.as_view(), name='assesment-record-update'),
    path('assesment-records/delete/<int:pk>/', AssessmentRecordDelete.as_view(), name='assesment-record-delete'),
    
    path('kills/', daily_kill_report, name='daily-kills'),
    path('kills_view/', daily_kill_report_view, name='daily-kills-view'),
     path('kills_filter/', daily_kill_filter, name='daily-kills-filter'),
    path('daily-kills/create/', DailyKillCreate.as_view(), name='daily_kill_create'),
    path('daily-kills/list/', DailyKillList.as_view(), name='daily-kills-list'),
    path('daily-kills/update/<int:pk>/', DailyKillUpdate.as_view(), name='daily_kill_update'),
    path('daily-kills/delete/<int:pk>/', DailyKillDelete.as_view(), name='daily_kill_delete'),
    
    path('movement-permit/', movement_permit_report, name='movement-permit-report'),
    path('movement-permit_report/', movement_permit_report_view, name='movement-permit-view'),
    path('movement-permits/create/', MovementPermitCreate.as_view(), name='movement_permit_create'),
    path('movement-permits/', MovementPermitList.as_view(), name='movement-permit-list'),
    path('movement-permits/update/<int:pk>/', MovementPermitUpdate.as_view(), name='movement_permit_update'),
    path('movement-permits/delete/<int:pk>/', MovementPermitDelete.as_view(), name='movement_permit_delete'),
    path('movement-permits/stream/<int:permit_id>/', MovementPermitList.as_view(), name='permit_view'),

    
    path('no_objections/', no_objection_report, name='no_objection_report'),
    path('no_objections/view', no_objection_report_view, name='no_objection_report_view'),
    path('no_objections/create/', NoObjectionCreate.as_view(), name='no_objection_create'),
    path('no_objections/list/', NoObjectionList.as_view(), name='no-objection-list'),
    path('no_objections/update/<int:pk>/', NoObjectionUpdate.as_view(), name='no_objection_update'),
    path('no_objections/delete/<int:pk>/',NoObjectionDelete.as_view(), name='no_objection_delete'),

    
    path('monthly-report/', monthly_report, name='monthly_report'),
    path('monthly-report-official/', monthly_report_view, name='monthly_report_official'),
    path('monthly-reports/create/', MonthlyReportCreate.as_view(), name='monthly_report_create'),
    path('monthly-reports/', MonthlyReportList.as_view(), name='monthly-report-list'),
    path('monthly-reports/update/<int:pk>/', MonthlyReportUpdate.as_view(), name='monthly_report_update'),
    path('monthly-reports/delete/<int:pk>/', MonthlyReportDelete.as_view(), name='monthly_report_delete'),

    path('practitioner/record/', practitioner_record, name='practitioner_record'),
    path('prac-filter/',  prac_record_filter, name='prac_filter'),
    path('practitioner/record/view/', practitioner_record_view, name='practitioner_record_view'),
    path('practitioner/create/', PractitionerCreate.as_view(), name='practitioner_create'),
    path('practitioner/list/', PractitionerList.as_view(), name='practitioner_list'),
    path('practitioner/update/<int:pk>/', PractitionerUpdate.as_view(), name='practitioner_update'),
    path('practitioner/delete/<int:pk>/', PractitionerDelete.as_view(), name='practitioner_delete'),

    path('quarterly-report/', quarterly_report, name='quarterly_report'),
    path('quarterly-report/view/', quarterly_report_view, name='quarterly_report_view'),

    path('quarterly-report/create/', QuarterlyReportCreate.as_view(), name='quarterly-report-create'),
    path('quarterly-report/list/', QuarterlyReportList.as_view(), name='quarterly-report-list'),
    path('quarterly-report/update/<int:pk>/', QuarterlyReportUpdate.as_view(), name='quarterly-report-update'),
    path('quarterly-report/delete/<int:pk>/', QuarterlyReportDelete.as_view(), name='quarterly-report-delete'),
    
    path('yearly-report/', yearly_report, name='yearly_report'),
    path('yearly-report/view/', yearly_report_view, name='yearly_report_view'),
    path('yearly-report/create/', YearlyReportCreate.as_view(), name='yearly-report-create'),
    path('yearly-report/list/', YearlyReportList.as_view(), name='yearly-report-list'),
    path('yearly-report/update/<int:pk>/', YearlyReportUpdate.as_view(), name='yearly-report-update'),
    path('yearly-report/delete/<int:pk>/', YearlyReportDelete.as_view(), name='yearly-report-delete'),
    path('generate-certificate/<str:first_name>/<str:last_name>/', generate_certificate, name='generate_certificate'),
    path('get-certificate/<str:first_name>/<str:last_name>/', get_certificate, name='get_certificate'),
    #path('answers/', UserAnswerCreate.as_view(), name='user-answer-create'),
    
    path('irrigation/', irrigation, name='ui-irrigation'),
    path('irrigation/view/', irrigation_view, name='ui-irrigation-view'),
    path('uterine-irrigation/create/', UterineIrrigationCreate.as_view(), name='uterine_irrigation_create'),
    path('uterine-irrigation/list/', UterineIrrigationList.as_view(), name='ui-list'),
    path('uterine-irrigation/update/<int:pk>/', UterineIrrigationUpdate.as_view(), name='uterine_irrigation_update'),
    path('uterine-irrigation/delete/<int:pk>/', UterineIrrigationDelete.as_view(), name='uterine_irrigation_delete'),
    
    path('emergency-care/', emergency_care, name='emergency-care'),
    path('emergency-care/view/', emergency_care_view, name='emergency-care-view'),
    path('emergency-care/create/', EmergencyCareCreate.as_view(), name='emergency-care-create'),
    path('emergency-care/list/', EmergencyCareList.as_view(), name='emergency-care-list'),
    path('emergency-care/update/<int:pk>/',EmergencyCareUpdate.as_view(), name='emergency-care-update'),
    path('emergency-care/delete/<int:pk>/', EmergencyCareDelete.as_view(), name='emergency-care-delete'),
    
    path('price-list/', price_list, name='price_list'),
    path('price-list/view/', price_list_view, name='price_list_view'),
    path('price-list/create/', PriceListCreate.as_view(), name='price_list_create'),
    path('price-list/list/', PriceListList.as_view(), name='price-list'),
    path('price-list/update/<int:pk>/', PriceListUpdate.as_view(), name='price_list_update'),
    path('price-list/delete/<int:pk>/', PriceListDelete.as_view(), name='price_list_delete'),

    
    path('supplier/', supplier, name='supplier'),
    path('supplier/view/', supplier_view, name='supplier_view'),
    path('supplier/create/', SupplierCreate.as_view(), name='supplier_create'),
    path('supplier/list/', SupplierList.as_view(), name='supplier-list'),
    path('supplier/update/<int:pk>/', SupplierUpdate.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', SupplierDelete.as_view(), name='supplier_delete'),

    
    path('client/', client, name='client'),
    path('client/view/', client_view, name='client_view'),
    path('client/create/', CustomerCreate.as_view(), name='client_create'),
    path('client/list/', CustomerList.as_view(), name='client-list'),
    path('client/update/<int:pk>/', CustomerUpdate.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', CustomerDelete.as_view(), name='client_delete'),

    
    path('creditor/', creditor, name='creditor'),
    path('creditor/view/', creditor_view, name='creditor_view'),
    path('creditor/create/', CreditorCreate.as_view(), name='creditor_create'),
    path('creditor/list/', CreditorList.as_view(), name='creditor-list'),
    path('creditor/update/<int:pk>/', CreditorUpdate.as_view(), name='creditor_update'),
    path('creditor/delete/<int:pk>/', CreditorDelete.as_view(), name='creditor_delete'),

    
    path('debtor/', debtor, name='debtor'),
    path('debtor/view/', debtor_view, name='debtor_view'),
    path('debtor/create/', DebtorCreate.as_view(), name='debtor_create'),
    path('debtor/list/', DebtorList.as_view(), name='debtor-list'),
    path('debtor/update/<int:pk>/', DebtorUpdate.as_view(), name='debtor_update'),
    path('debtor/delete/<int:pk>/', DebtorDelete.as_view(), name='debtor_delete'),
    


    # ClientRequest URLs
    path('client-request/', client_request, name='client-request'),
    path('client-request/view/', client_request_view, name='client_request_view'),
    path('client-requests/create/', ClientRequestCreate.as_view(), name='client-request-create'),
    path('client-requests/', ClientRequestList.as_view(), name='client-request-list'),
    path('client-requests/update/<int:pk>/', ClientRequestUpdate.as_view(), name='client-request-update'),
    path('client-requests/delete/<int:pk>/', ClientRequestDelete.as_view(), name='client-request-delete'),

    # VetJudgment URLs
    path('vet-judgment/', vet_judgment, name='vet_judgment'),
    path('vet-judgment/view/', vet_judgment_view, name='vet_judgment_view'),
    path('vet-judgments/create/', VetJudgmentCreate.as_view(), name='vet-judgment-create'),
    path('vet-judgments/', VetJudgmentList.as_view(), name='vet-judgment-list'),
    path('vet-judgments/update/<int:pk>/', VetJudgmentUpdate.as_view(), name='vet-judgment-update'),
    path('vet-judgments/delete/<int:pk>/', VetJudgmentDelete.as_view(), name='vet-judgment-delete'),
    path("update-request-status/", update_request_status, name="update-request-status"),
    #path('get-requests/', get_requests, name='get-requests'),
    #Payment 
    path('mpesa/payment/<int:lesson_id>/', payment, name='mpesa-payment'),
    path('zoom/payment/<int:meeting_id>/', payment_zoom, name='zoom-payment'), 
    path('mpesa/initiate/', initiate_mpesa_payment, name='mpesa-initiate'),
    path('mpesa/pay/', zoom_mpesa_payment, name='mpesa-pay'),
    path('mpesa/callback/', mpesa_callback, name='mpesa-callback'),
    path('mpesa/status/', check_mpesa_status, name='mpesa-status'),
    
    #daily Checks 
    path('daily-checks/', daily_checks, name='daily-checks'),
    path('daily-checks/create/', DailyCheckCreate.as_view(), name='daily-check-create'),
    path('daily-checks-list/', DailyCheckList.as_view(), name='daily-check-list'),
    path('daily-checks/update/<int:pk>/', DailyCheckUpdate.as_view(), name='daily-check-update'),
    path('daily-checks/delete/<int:pk>/', DailyCheckDelete.as_view(), name='daily-check-delete'),
     
    path('management-committee/', management_committee, name='management-committee'),
    path('management-committee/create/', ManagementCommitteeCreate.as_view(), name='management-committee-create'),
    path('management-committee/list/', ManagementCommitteeList.as_view(), name='management-committee-list'),
    path('management-committee/update/<int:pk>/',ManagementCommitteeUpdate.as_view(), name='management-committee-update'),
    path('management-committee/delete/<int:pk>/',ManagementCommitteeDelete.as_view(), name='management-committee-delete'),

    # Hides and Skins Record URLs
    path('hides-skins/', hides_and_skins_record, name='hides-skins-record'),
    path('hides-skins/create/', HidesAndSkinsRecordCreate.as_view(), name='hides-skins-create'),
    path('hides-skins/list/', HidesAndSkinsRecordList.as_view(), name='hides-skins-list'),
    path('hides-skins/update/<int:pk>/', HidesAndSkinsRecordUpdate.as_view(), name='hides-skins-update'),
    path('hides-skins/delete/<int:pk>/', HidesAndSkinsRecordDelete.as_view(), name='hides-skins-delete'),   
        
   path('approved-dairy-farms/', approved_dairy_farms, name='approved-dairy-farms'),
    path('approved-dairy-farms/create/', ApprovedDairyFarmCreate.as_view(), name='approved-dairy-farms-create'),
    path('approved-dairy-farms/list/', ApprovedDairyFarmList.as_view(), name='approved-dairy-farms-list'),
    path('approved-dairy-farms/update/<int:pk>/', ApprovedDairyFarmUpdate.as_view(), name='approved-dairy-farms-update'),
    path('approved-dairy-farms/delete/<int:pk>/', ApprovedDairyFarmDelete.as_view(), name='approved-dairy-farms-delete'),
    
    path('slaughterhouse-hygiene/', slaughterhouse_hygiene_page, name='slaughterhouse-hygiene-page'),
    path('api/hygiene/create/', SlaughterhouseHygieneCreate.as_view(), name='hygiene-create'),
    path('api/hygiene/list/', SlaughterhouseHygieneList.as_view(), name='hygiene-list'),
    path('api/hygiene/update/<int:pk>/', SlaughterhouseHygieneUpdate.as_view(), name='hygiene-update'),
    path('api/hygiene/delete/<int:pk>/', SlaughterhouseHygieneDelete.as_view(), name='hygiene-delete'),

    # Asset URLs
    path('slaughterhouse-assets/', slaughterhouse_asset_page, name='slaughterhouse-assets-page'),
    path('api/assets/create/', SlaughterhouseAssetCreate.as_view(), name='asset-create'),
    path('api/assets/list/', SlaughterhouseAssetList.as_view(), name='asset-list'),
    path('api/assets/update/<int:pk>/', SlaughterhouseAssetUpdate.as_view(), name='asset-update'),
    path('api/assets/delete/<int:pk>/', SlaughterhouseAssetDelete.as_view(), name='asset-delete'),
    
    path("dairy/", dairy_cow_page, name="dairy_page"),
    path("dairy/data/", livestock_data, {"livestock_type": "dairy_cow"}, name="dairy_data"),

    path("beef/", beef_page, name="beef_page"),
    path("beef/data/", livestock_data, {"livestock_type": "beef"}, name="beef_data"),

    path("sheep/", sheep_page, name="sheep_page"),
    path("sheep/data/", livestock_data, {"livestock_type": "sheep"}, name="sheep_data"),

    path("goat/", goat_page, name="goat_page"),
    path("goat/data/",livestock_data, {"livestock_type": "goat"}, name="goat_data"),
    
    path('livestock-registration/', livestock_registration, name='livestock_registration'),
    path('api/livestock/create/', LivestockRegistrationCreate.as_view(), name='livestock-create'),
    path('api/livestock/list/', LivestockRegistrationList.as_view(), name='livestock-list'),
    path('api/livestock/update/<int:pk>/', LivestockRegistrationUpdate.as_view(), name='livestock-update'),
    path('api/livestock/delete/<int:pk>/', LivestockRegistrationDelete.as_view(), name='livestock-delete'),
    
     path('e-prescriptions/', eprescription, name='eprescriptions'),
    path('e-prescriptions/create/', VeterinaryEPrescriptionCreate.as_view(), name='vet_eprescription_create'),
    path('e-prescription/', VeterinaryEPrescriptionList.as_view(), name='eprescription_list'),
    path('e-prescriptions/update/<int:pk>/', VeterinaryEPrescriptionUpdate.as_view(), name='vet_eprescription_update'),
    path('e-prescriptions/delete/<int:pk>/', VeterinaryEPrescriptionDelete.as_view(), name='vet_eprescription_delete'),

    path('routine/', routine, name='routine'),
    path('routine-management/create/', RoutineManagementCreate.as_view(), name='routine_management_create'),
    path('routine-management/', RoutineManagementList.as_view(), name='routine_management_list'),
    path('routine-management/update/<int:pk>/', RoutineManagementUpdate.as_view(), name='routine_management_update'),
    path('routine-management/delete/<int:pk>/', RoutineManagementDelete.as_view(), name='routine_management_delete'),

    path('abortion/', abortion, name='abortion'),
    path('abortion-records/create/', AbortionRecordCreate.as_view(), name='abortion_record_create'),
    path('abortion-records/', AbortionRecordList.as_view(), name='abortion_record_list'),
    path('abortion-records/update/<int:pk>/', AbortionRecordUpdate.as_view(), name='abortion_record_update'),
    path('abortion-records/delete/<int:pk>/', AbortionRecordDelete.as_view(), name='abortion_record_delete'),
    
    path("extension-service/", extension_service, name="extension-service"),
    path("extension-service/create/", ExtensionServiceCreate.as_view(), name="extension-service-create"),
    path("extension-service/list/", ExtensionServiceList.as_view(), name="extension-service-list"),
    path("extension-service/update/<int:pk>/", ExtensionServiceUpdate.as_view(), name="extension-service-update"),
    path("extension-service/delete/<int:pk>/", ExtensionServiceDelete.as_view(), name="extension-service-delete"),
    path('api/users/', search_users, name='search-users'),
    
     path('field-quotation/', field_quotation, name='field_quotation'),
     path('field-quotation-view/', field_quotation_view, name='field_quotation_view'),


    # API Endpoints
    path('field-quotation/create/', FieldQuotationCreate.as_view(), name='field_quotation_create'),
    path('field-quotation/list/', FieldQuotationList.as_view(), name='field_quotation_list'),
    path('field-quotation/update/<int:pk>/', FieldQuotationUpdate.as_view(), name='field_quotation_update'),
    path('field-quotation/delete/<int:pk>/', FieldQuotationDelete.as_view(), name='field_quotation_delete'),
    path("zoom/auth/", zoom_auth, name="zoom-auth"),
    path("zoom/callback/", zoom_callback, name="zoom-callback"),
    path("zoom/schedule/", zoom_schedule, name="zoom_schedule"),
    path("zoom/attendance/<str:meeting_id>/", fetch_zoom_attendance, name="zoom_attendance"),
    
    path('dairy-farmer-view/', dairy_farmer_view, name='dairy_farmer_report_view'),
    path('milk-center-view/', milk_center_view, name='milk_center_report_view'),
    path('milk-price-view/',  milk_price_view, name='milk_price_report_view'),
    path('milk-payment-view/',  milk_payment_view, name='milk_payment_report_view'),

   
    path('dairy-farmer-registration/create/',  DairyFarmerRegistrationCreate.as_view(), name='dairy_farmer_registration_create'),
    path('dairy-farmer-registration/list/',  DairyFarmerRegistrationList.as_view(), name='dairy_farmer_registration_list'),
    path('dairy-farmer-registration/update/<int:pk>/',  DairyFarmerRegistrationUpdate.as_view(), name='dairy_farmer_registration_update'),
    path('dairy-farmer-registration/delete/<int:pk>/',  DairyFarmerRegistrationDelete.as_view(), name='dairy_farmer_registration_delete'),

   
    path('milk-collection-center/create/',  MilkCollectionCenterCreate.as_view(), name='milk_collection_center_create'),
    path('milk-collection-center/list/',  MilkCollectionCenterList.as_view(), name='milk_collection_center_list'),
    path('milk-collection-center/update/<int:pk>/',  MilkCollectionCenterUpdate.as_view(), name='milk_collection_center_update'),
    path('milk-collection-center/delete/<int:pk>/',  MilkCollectionCenterDelete.as_view(), name='milk_collection_center_delete'),

    
    path('current-milk-price/create/',  CurrentMilkPriceCreate.as_view(), name='current_milk_price_create'),
    path('current-milk-price/list/',  CurrentMilkPriceList.as_view(), name='current_milk_price_list'),
    path('current-milk-price/update/<int:pk>/',  CurrentMilkPriceUpdate.as_view(), name='current_milk_price_update'),
    path('current-milk-price/delete/<int:pk>/',  CurrentMilkPriceDelete.as_view(), name='current_milk_price_delete'),

    
    path('farmer-milk-payment/create/',  FarmerMilkPaymentCreate.as_view(), name='farmer_milk_payment_create'),
    path('farmer-milk-payment/list/',  FarmerMilkPaymentList.as_view(), name='farmer_milk_payment_list'),
    path('farmer-milk-payment/update/<int:pk>/',  FarmerMilkPaymentUpdate.as_view(), name='farmer_milk_payment_update'),
    path('farmer-milk-payment/delete/<int:pk>/',  FarmerMilkPaymentDelete.as_view(), name='farmer_milk_payment_delete'),

    
     path('supply/cooler/',collection_cooler, name='supply_cooler'),
    path('collection/center/',  collection_center, name='collection_center'),

   path('daily-supply/create/', MilkCollectionCoolerCreate.as_view(), name='daily_supply_create'),
    path('daily-supply/list/', MilkCollectionCoolerList.as_view(), name='daily_supply_list'),
    path('daily-supply/update/<int:pk>/', MilkCollectionCoolerUpdate.as_view(), name='daily_supply_update'),
    path('daily-supply/delete/<int:pk>/', MilkCollectionCoolerDelete.as_view(), name='daily_supply_delete'),

    path('collection/create/', MilkCollectionCenterRecordCreate.as_view(), name='collection_create'),
    path('collection/list/', MilkCollectionCenterRecordList.as_view(), name='collection_list'),
    path('collection/update/<int:pk>/', MilkCollectionCenterRecordUpdate.as_view(), name='collection_update'),
    path('collection/delete/<int:pk>/', MilkCollectionCenterRecordDelete.as_view(), name='collection_delete'),
    
    # ================= Revenue Collection =================
    path('revenue/', revenue_collection, name='revenue-view'),
    path('revenue-gov/', revenue_collection_gov, name='revenue-view-gov'),
    path('revenue/create/', DailyRevenueCollectionCreate.as_view(), name='revenue-create'),
    path('revenue/list/', DailyRevenueCollectionList.as_view(), name='revenue-list'),
    path('revenue/update/<int:pk>/', DailyRevenueCollectionUpdate.as_view(), name='revenue-update'),
    path('revenue/delete/<int:pk>/', DailyRevenueCollectionDelete.as_view(), name='revenue-delete'),

    # ================= Leave Requests =================
    path('leave/', leave_request_view, name='leave-view'),
     path('leave-gov/', leave_request_view_gov, name='leave-view-gov'),
    path('leave/create/', LeaveRequestCreate.as_view(), name='leave-create'),
    path('leave/list/', LeaveRequestList.as_view(), name='leave-list'),
    path('leave/update/<int:pk>/', LeaveRequestUpdate.as_view(), name='leave-update'),
    path('leave/delete/<int:pk>/', LeaveRequestDelete.as_view(), name='leave-delete'),

    # ================= Movement Permits =================
    path('movement_permit/', movement_permits_view, name='movement-permits-view'),
    path('movement_permit-gov/', movement_permits_gov, name='movement-permits-gov'),
    path('movement_permit/create/', MovementPermitsCreate.as_view(), name='movement-permits-create'),
    path('movement_permit/list/', MovementPermitsList.as_view(), name='movement-permits-list'),
    path('movement_permit/update/<int:pk>/', MovementPermitsUpdate.as_view(), name='movement-permits-update'),
    path('movement_permits/delete/<int:pk>/', MovementPermitsDelete.as_view(), name='movement-permits-delete'),

    # ================= No Objections =================
    path('no-objections/', no_objections_view, name='no-objections-view'),
     path('no-objections-gov/', no_objections_view_gov, name='no-objections-view-gov'),
    path('no-objections/create/', NoObjectionsCreate.as_view(), name='no-objections-create'),
    path('no-objections/list/', NoObjectionsList.as_view(), name='no-objections-list'),
    path('no-objections/update/<int:pk>/', NoObjectionsUpdate.as_view(), name='no-objections-update'),
    path('no-objections/delete/<int:pk>/', NoObjectionsDelete.as_view(), name='no-objections-delete'),
    # ================= Disease Reports =================
    path('disease-report/', disease_rep, name='disease-report-view'),
    path('disease-report-gov/', disease_rep_gov, name='disease-report-view-gov'),
    path('api/disease-report/create/', DiseaseReportMovsCreate.as_view(), name='disease_report_create'),
    path('api/disease-report/list/', DiseaseReportMovsList.as_view(), name='disease_rep_list'),
    path('api/disease-report/update/<int:pk>/', DiseaseReportMovsUpdate.as_view(), name='disease_report_update'),
    path('api/disease-report/delete/<int:pk>/', DiseaseReportMovsDelete.as_view(), name='disease_report_delete'),
    
    
    # Practitioners
    path('practitioners/', practitioner_, name='practitioners_view'),
    path('practitioners-gov/', practitioner_gov, name='practitioners_gov'),
    path('api/practitioners/create/', PractitionersCreate.as_view(), name='practitioner-create'),
    path('api/practitioners/', PractitionersList.as_view(), name='practitioner-list'),
    path('api/practitioners/update/<int:pk>/', PractitionersUpdate.as_view(), name='practitioner-update'),
    path('api/practitioners/delete/<int:pk>/', PractitionersDelete.as_view(), name='practitioner-delete'),

    # Slaughter Houses
    path('slaughterhouses/',slaughterhouse_view, name='slaughterhouses-page'),
    path('slaughterhouses-gov/',slaughterhouse_view_gov, name='slaughterhouses-page-gov'),
    path('api/slaughterhouses/create/', SlaughterHousesCreate.as_view(), name='slaughterhouse-create'),
    path('api/slaughterhouses/', SlaughterHousesList.as_view(), name='slaughterhouses-list'),
    path('api/slaughterhouses/update/<int:pk>/',SlaughterHousesUpdate.as_view(), name='slaughterhouse-update'),
    path('api/slaughterhouses/delete/<int:pk>/', SlaughterHousesDelete.as_view(), name='slaughterhouse-delete'),

    # Daily Kills
    path('daily-kills/', daily_kl, name='daily-kills-page'),
    path('daily-kills-gov/', daily_kl_gov, name='daily-kills-page-gov'),
    path('api/daily-kill/create/', DailyKillsCreate.as_view(), name='daily-kill-create'),
    path('api/daily-kill/', DailyKillsList.as_view(), name='daily_kil_list'),
    path('api/daily-kill/update/<int:pk>/', DailyKillsUpdate.as_view(), name='daily-kill-update'),
    path('api/daily-kill/delete/<int:pk>/', DailyKillsDelete.as_view(), name='daily-kill-delete'),

    # Template View (HTML Form/Dashboard)
    path('inseminations/', artificial_inseminations_view, name='artificial_inseminations_view'),
    path('inseminations_gov/', artificial_inseminations_view_gov, name='artificial_inseminations_view_gov'),


    # API Endpoints
    path('api/artificial-inseminations/', ArtificialInseminationsList.as_view(), name='list_ai'),
    path('api/artificial-inseminations/create/', ArtificialInseminationsCreate.as_view(), name='ai_create'),
    path('api/artificial-inseminations/update/<int:pk>/', ArtificialInseminationsUpdate.as_view(), name='ai_update'),
    path('api/artificial-inseminations/delete/<int:pk>/', ArtificialInseminationsDelete.as_view(), name='ai_delete'),
    
    # Template View (The HTML Page with the form and table)
    path('extension-services/', extension_serve, name='extension_services_view'),
    path('extension-services-gov/', extension_serve_gov, name='extension_services_view_gov'),


    # API Endpoints
    path('api/extension-services/', ExtensionServicesList.as_view(), name='extension_services_list'),
    path('api/extension-services/create/', ExtensionServicesCreate.as_view(), name='extension_services_create'),
    path('api/extension-services/update/<int:pk>/', ExtensionServicesUpdate.as_view(), name='extension_services_update'),
    path('api/extension-services/delete/<int:pk>/',ExtensionServicesDelete.as_view(), name='extension_services_delete'),
    
    # path('practitioner/', practitioners_, name='practitioners_view'),
    path('clerk/', clerk, name='clerk'),
     path('clerk_view/', clerk, name='clerk_view'),
    path('milk-clerk/create/', MilkCollectionClerkCreate.as_view()),
    path('milk-clerk/list/', MilkCollectionClerkList.as_view(),name='milk-clerk-list'),
    path('milk-clerk/update/<int:pk>/', MilkCollectionClerkUpdate.as_view()),
    path('milk-clerk/delete/<int:pk>/', MilkCollectionClerkDelete.as_view()),
    path('vaccinations/', vaccinations_list, name='vaccinations-list'),
     path('vaccinations-gov/', vaccinations_list_gov, name='vaccinations-list-gov'),


    path('api/vaccinations/', VaccinationsList.as_view(), name='vacc_list'),
    path('api/vaccinations/create/', VaccinationsCreate.as_view(), name='vaccinations_create'),
    path('api/vaccinations/update/<int:pk>/', VaccinationsUpdate.as_view(), name='vaccinations_update'),
    path('api/vaccinations/delete/<int:pk>/', VaccinationsDelete.as_view(), name='vaccinations_delete'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)