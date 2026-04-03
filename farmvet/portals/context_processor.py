from django.contrib.auth import get_user_model
from .models import *

def all_farmers(request):
    User = get_user_model()
    farmers = User.objects.filter(is_farmer=True).order_by('first_name')
    return {'all_farmers': farmers}
def all_officials(request):
    User = get_user_model()
    officials = User.objects.filter(is_official=True).order_by('first_name')
    return {'all_officials': officials}
def all_vets(request):
    User = get_user_model()
    vets = User.objects.filter(is_vet_officer=True).order_by('first_name')
    return {'all_vets': vets}
def all_cooperatives(request):
    User = get_user_model()
    all_cooperatives = User.objects.filter(is_cooperative=True).order_by('first_name')
    return {'all_cooperatives': all_cooperatives}

def user_role(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'is_farmer') and request.user.is_farmer:
            return {'role': 'farmer'}
        elif hasattr(request.user, 'is_vet_officer') and request.user.is_vet_officer:
            return {'role': 'vet'}
        elif hasattr(request.user, 'is_cooperative') and request.user.is_cooperative:
            return {'role': 'cooperative'}
    return {'role': 'guest'}

def choices(request):
    return {
        'LIVESTOCK_CATEGORY_CHOICES': LaboratoryRecord.LIVESTOCK_CATEGORY_CHOICES,
        'SEX_CHOICES': LaboratoryRecord.SEX_CHOICES,
        'AGE_CHOICES': LaboratoryRecord.AGE_CHOICES,
        'SAMPLE_TYPE_CHOICES': LaboratoryRecord.SAMPLE_TYPE_CHOICES,
        'SAMPLE_RATING_CHOICES': LaboratoryRecord.SAMPLE_RATING_CHOICES,
        'TRANSPORTATION_CHOICES': LaboratoryRecord.TRANSPORTATION_CHOICES,
        'LIVESTOCK_CATEGORY_CHOICES': PostMortemRecord.LIVESTOCK_CATEGORY_CHOICES,
        'SEX_CHOICES': PostMortemRecord.SEX_CHOICES,
        'YES_NO_CHOICES': PostMortemRecord.YES_NO_CHOICES,
        'DISPOSAL_CHOICES': PostMortemRecord.DISPOSAL_CHOICES,
        'CATEGORY_CHOICES': PregnancyDiagnosis.CATEGORY_CHOICES,
        'PD_RESULTS_CHOICES': PregnancyDiagnosis.PD_RESULTS_CHOICES,
        'AREA_OF_INTEREST_CHOICES_FARM': FarmConsultation.AREA_OF_INTEREST_CHOICES,
        'BILLING_CATEGORY_CHOICES': VeterinaryBilling.BILLING_CATEGORY_CHOICES,
        'MODE_OF_PAYMENT_CHOICES': VeterinaryBilling.MODE_OF_PAYMENT_CHOICES,
        'SPECIES_TARGETED_CHOICES':Deworming.SPECIES_TARGETED_CHOICES,
        'SERVED_BY_CHOICES': ArtificialInsemination.SERVED_BY_CHOICES,
        'ABORTION_STATUS_CHOICES': ArtificialInsemination.ABORTION_STATUS_CHOICES,
        'INSEMINATION_STATUS_CHOICES':ArtificialInsemination.INSEMINATION_STATUS_CHOICES,
        'ANIMAL_SPECIES_CHOICES': ClinicalRecord.ANIMAL_SPECIES_CHOICES,
        'DISEASE_NATURE_CHOICES': ClinicalRecord.DISEASE_NATURE_CHOICES,
        'YES_NO_CHOICES': ClinicalRecord.YES_NO_CHOICES,
        'AREA_OF_INTEREST_CHOICES': FarmConsultation.AREA_OF_INTEREST_CHOICES,
        'LIVESTOCK_CATEGORY_CHOICES': SampleProcessing.LIVESTOCK_CATEGORY_CHOICES,
        'SEX_CHOICES': SampleProcessing.SEX_CHOICES,
        'AGE_CHOICES': SampleProcessing.AGE_CHOICES,
        'SAMPLE_RATING_CHOICES': SampleProcessing.SAMPLE_RATING_CHOICES,
        'SAMPLE_COLLECTION_LIVESTOCK_CATEGORY_CHOICES': SampleCollection.LIVESTOCK_CATEGORY_CHOICES,
        'SAMPLE_COLLECTION_SEX_CHOICES': SampleCollection.SEX_CHOICES,
        'SAMPLE_COLLECTION_AGE_CHOICES': SampleCollection.AGE_CHOICES,
        'SAMPLE_COLLECTION_SAMPLE_TYPE_CHOICES': SampleCollection.SAMPLE_TYPE_CHOICES,
        'SAMPLE_COLLECTION_SAMPLE_RATING_CHOICES': SampleCollection.SAMPLE_RATING_CHOICES,
        'SURGICAL_LIVESTOCK_CATEGORIES': SurgicalRecord.LIVESTOCK_CATEGORIES,
        'SURGICAL_SEX_CHOICES': SurgicalRecord.SEX_CHOICES,
        'SURGICAL_AGE_CHOICES': SurgicalRecord.AGE_CHOICES,
        'SURGICAL_NATURE_OF_SURGERY': SurgicalRecord.NATURE_OF_SURGERY,
        'SURGICAL_TYPE_OF_SURGERY': SurgicalRecord.TYPE_OF_SURGERY,
        'SURGICAL_STATUS_CHOICES': SurgicalRecord.STATUS_CHOICES,
        'SURGICAL_PROGNOSIS_CHOICES': SurgicalRecord.PROGNOSIS_CHOICES,
        'VACCINATION_ANIMAL_SPECIES_CHOICES': VaccinationRecord.ANIMAL_SPECIES_CHOICES,
        'VACCINATION_TYPE_CHOICES': VaccinationRecord.VACCINATION_TYPE_CHOICES,
        'NATURE_OF_VACCINATION_PROGRAM_CHOICES': VaccinationRecord.NATURE_OF_VACCINATION_PROGRAM_CHOICES,
        'VACCINATION_SEX':VaccinationRecord.VACCINATION_SEX,
        'BILLING_CATEGORY_CHOICES':VeterinaryBilling.BILLING_CATEGORY_CHOICES,
        'MODE_OF_PAYMENT_CHOICES':VeterinaryBilling.MODE_OF_PAYMENT_CHOICES,
        'LIVESTOCK_CATEGORY_CHOICES':DiseaseReport.LIVESTOCK_CATEGORY_CHOICES,
        'AGE_CHOICES':DiseaseReport.AGE_CHOICES,
        'SEX_CHOICES':DiseaseReport.SEX_CHOICES,
        'YES_NO_CHOICES':DiseaseReport.YES_NO_CHOICES,
        'ASSIGN_TO_CHOICES':Invoice.ASSIGN_TO_CHOICES,
        'INVOICE_CATEGORY_CHOICES':Invoice.INVOICE_CATEGORY_CHOICES,
        'TRANSPORT_CHOICES':Butcher.TRANSPORT_CHOICES,
        'SL_CATEGORY_CHOICES':Slaughterhouse.CATEGORY_CHOICES,
        'E_POSITION_CHOICES':Employee.POSITION_CHOICES,
        'VET_CATEGORY':Practitioner.VET_CATEGORY_CHOICES,
        'SPECIALIZATION':Practitioner.SPECIALIZATION_CHOICES,
        'DISEASE_CHOICES':VaccinationRecord.DISEASE_CHOICES,
        'EMP_STATUS_CHOICES':Practitioner.EMP_STATUS_CHOICES,
        'SL_STATUS':Slaughterhouse.SL_STATUS,
        'ML_LICENSE_CHOICES':Employee.ML_LICENSE_CHOICES,
        'LICENSE_CHOICES':Butcher.LICENSE_CHOICES,
        'CLINICAL_PROGNOSIS':ClinicalRecord.PROGNOSIS,
        'PROGNOSIS':Referral.PROGNOSIS,
        'REFERRAL_CHOICE':Referral.REFERRAL_CHOICE,
        'FARM_MANAGER_CATEGORY':FarmConsultation.FARM_MANAGER_CATEGORY,
        'PLAN_CHOICES':VeterinaryBilling.PLAN_CHOICES,
        'PAYMENT_STATUS_CHOICES':VeterinaryBilling.PAYMENT_STATUS_CHOICES,
        'ABORTION_STATUS':UterineIrrigationRecord.ABORTION_STATUS,
        'RAB':UterineIrrigationRecord.RAB,
        'LIVESTOCK_CATEGORIES':UterineIrrigationRecord.LIVESTOCK_CATEGORIES,
        'LIVESTOCK_CATEGORY_CHOICES': EmergencyCare.LIVESTOCK_CATEGORY_CHOICES,
        'EMERGENCY_CATEGORY_CHOICES': EmergencyCare.EMERGENCY_CATEGORY_CHOICES,
        'CONDITION_CHOICES': EmergencyCare.CONDITION_CHOICES,
        'PROGNOSIS_DIAGNOSIS_CHOICES': EmergencyCare.PROGNOSIS_DIAGNOSIS_CHOICES,
        'REASONS':UterineIrrigationRecord.REASONS,
        'ANIMAL_SPECIES':ArtificialInsemination.ANIMAL_SPECIES,
        'VET_CATEGORY':ArtificialInsemination.VET_CATEGORY,
        'MEAT_CATEGORY_CHOICES':DailyKill.MEAT_CATEGORY_CHOICES,
        'RAB_STATUS':ArtificialInsemination.RAB,
        'BREED':ArtificialInsemination.COW_BREEDS,
        'SEMEN_SOURCE':ArtificialInsemination.SEMEN_SOURCE,
        'EMERGENCY_CONDITIONS':VetJudgment.EMERGENCY_CONDITIONS,
        'NON_EMERGENCY_CONDITIONS':VetJudgment.NON_EMERGENCY_CONDITIONS,
        'TELEMEDICINE_CATEGORIES':VetJudgment.TELEMEDICINE_CATEGORIES,
        'REQUEST_TYPES':VetJudgment.REQUEST_TYPES,
        'LIVESTOCK_CATEGORIES':VetJudgment.LIVESTOCK_CATEGORIES,
        'PROGNOSIS_CHOICES':VetJudgment.PROGNOSIS_CHOICES,
        'PRACTITIONER_JUDGMENT':VetJudgment.PRACTITIONER_JUDGMENT,
        'COMMUNICATION':ClientRequest.COMMUNICATION,
        'BUYER':Buyer.BUYER_CATEGORIES,
        'SALES_TO':SalesOfMilk.MILK_SALES_TO,
        'PAYMENT':Buyer.PAYMENT_MODES,
        'BREED_CHOICES':AnimalSale.BREED_CHOICES,
        'AGE':AnimalSale.AGE,
        'CHECKED_BY':DailyCheck.CHECKED_BY_CHOICES,
        'SECTION_CHECK':DailyCheck.SECTION_CHOICES,
        'VET_CAT_CH':Practitioner.VET_CATEGORY_CHOICES,
        'SUB_COUNTY':BOMET_SUBCOUNTY_CHOICES,
        'DESIGNATION':ApprovedDairyFarm.DESIGNATION_CHOICES,
        'CLEANING_CATEGORY':SlaughterhouseHygiene.CLEANING_CATEGORY_CHOICES,
        'CLEANING_PROCEDURE':SlaughterhouseHygiene.CLEANING_PROCEDURE_CHOICES,
        'ASSET_TYPE':SlaughterhouseAsset.ASSET_TYPE_CHOICES,
        'POSITION':ManagementCommittee.POSITION_CHOICES,
        'QUOTATION_CATEGORIES':FieldQuotation.QUOTATION_CATEGORIES,
        'BREEDING':DairyFarmerRegistration.BREEDS,
        'MEANS_OF_TRANSFER':MilkCollectionCenter.MEANS_OF_TRANSFER,
        'PROVIDER_CHOICES':ExtensionServices.PROVIDER_CHOICES,
        'LIVESTOCK_CHOICES':DailyKills.LIVESTOCK_CHOICES,
        'LEAVE_REASON_CHOICES':LeaveRequest.LEAVE_REASON_CHOICES,
        'LEAVE_STATUS_CHOICES':LeaveRequest.LEAVE_STATUS_CHOICES,
        
    }