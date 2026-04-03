from rest_framework import serializers
from django.db.models import Sum
from datetime import timedelta, date
from .models import *

class PregnancyMonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = PregnancyMonitoring
        fields = [
            'id', 'user', 'name', 'reg_no', 'date_of_ai','exp_heat_date','repeat_heat_date',
            'first_preg_diag_date','steaming_up_date', 'expected_dob' 
            
        ]
        read_only_fields = ['exp_heat_date','repeat_heat_date', 'first_preg_diag_date', 'steaming_up_date', 'expected_dob']

class HeatSignMonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatSignMonitoring
        fields = [
            'id',
            'user',
            'name',
            'reg_no',
            'status',
            'date_of_heat_sign',
            'date_of_repeat_monitoring',
            'exp_date_of_repeated_heat',
            'reason_skip_monitoring'
        ]
        read_only_fields = ['date_of_repeat_monitoring', 'exp_date_of_repeated_heat']
class AnimalSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalSale
        fields = [
            'id',
            'user',
            'number_sold',
            'name',
            'reg_no',
            'date_sold',
            'breed',
            'age',
            'sex',
            'weight',
            'selling_price',
            'reason',
            'comment',
        ]

class LivestockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livestock
        fields = [
            'id',
            'user',
            'animal_type',
            'breed_category',
            'date_added',
            'no_of_animals',
            'no_of_males',
            'no_of_females',
            'no_of_adults',
            'no_of_young',
            'no_of_dead',
            'reason_for_death',
            'comment'
        ]

class NewAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewAnimal
        fields = [
            'id',
            'user',
            'name',
            'reg_no',
            'source',
            'farmer_name',
            'animal_type',
            'breed',
            'breeding_level',
            'defect',
            'defect_reason',
            'animal_color',
            'market_value',
            'medical_history',
            'assessed_by_vet',
            'insured',
            'insuring_company',
            'date_added'
        ]

class CullingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culling
        fields = [
            'id',
            'user', 
            'name', 
            'reg_no', 
            'age', 
            'gender',
            'animal_type',
            'breed', 
            'culling_method', 
            'no_of_culled', 
            'culling_reason', 
            'culling_date', 
            'culling_price', 
            'comment'
        ]

class DeadAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeadAnimal
        fields = [
            'id',
            'user', 
            'name', 
            'farm_name', 
            'no_of_affected', 
            'gender', 
            'breed', 
            'sickness_period', 
            'cause_of_death', 
            'death_date', 
            'death_time', 
            'signs_before_death', 
            'postmortem_by_vet', 
            'safety_precaution', 
            'comment'
        ]

class CalfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calf
        fields = [
            'id',
            'user',
            'name_given',
            'registration_number',
            'dam_details',
            'birth_date',
            'breed',
            'gender',
            'sire_details',
            'color',
            'birth_weight',
            'medical_conditions',
            'registration_date',
            'expected_weaning',
            'breeding_level',
            'comments'
        ]

class FeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = [
            'id',
            'user',
            'date_of_purchase',
            'feed_type',
            'company',
            'expiry_date',
            'quantity_purchased',
            'trade_name',
            'weight',
            'cost',
            'comment'
        ]


class MineralsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minerals
        fields = ['id', 'user', 'date_of_purchase', 'mineral_type', 'quantity', 'company', 'expiry_date', 'cost', 'comment']

class VeterinaryBillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeterinaryBills
        fields = ['id', 'user', 'date_of_billing', 'bill_category', 'amount','amount_billed','balance', 'billing_details', 'comment']
        read_only_fields=['balance']
class ArcharicidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archaricides
        fields = ['id', 'user', 'date_of_purchase', 'chemical_name','trade_name','quantity', 'company', 'application_rate', 'expiry_date', 'times_used', 'cost', 'comment']

class DairyEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DairyEquipment
        fields = ['id', 'user', 'name','date_of_purchase', 'quantity', 'equipment_type','model_number', 'company', 'cost', 'source', 'comment']

class DairyHygieneSerializer(serializers.ModelSerializer):
    class Meta:
        model = DairyHygiene
        fields = ['id', 'user','chemical_name','trade_name','date_of_purchase', 'item_purchased', 'company', 'quantity', 'cost', 'expiry_date', 'comment']
class SalariesSerializer(serializers.ModelSerializer):
    employee_name = serializers.SlugRelatedField(queryset=Employees.objects.all(), slug_field='id')
    
    class Meta:
        model = Salaries
        fields = ['id', 'user','employee_name', 'employee_position', 'identification', 'mode_of_payment','bank_account','salary_amount','amount', 'balance', 'payment_date', 'payment_type', 'comment']
        read_only_fields = ['bank_account','balance']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        employee_instance = Employees.objects.get(id=data['employee_name'])  
        data['employee_names'] = employee_instance.employee_name 
        print(data)
        return data


class LivestockInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockInsurance
        fields = ['id', 'user', 'number_insured','breed','animal_species','number_insured','company', 'mode_of_payment', 'payment_date', 'total', 'comment']

class VeterinaryDrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeterinaryDrugs
        fields = ['id', 'user','date_of_purchase', 'name', 'category','company','expiry_date', 'strange_condition', 'vet_reg', 'cost', 'comment']

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = [
            'id',
            'user',
            'enrollment_date',
            'employee_name',
            'id_no',
            'phone_no',
            'county',
            'district',
            'village',
            'next_of_kin',
            'next_of_kin_phone_no',
            'chief_name',
            'chief_phone_no',
            'employee_position',
            'salary',
            'payment_method',
            'bank_account',
            'mode_of_employment',
            'contract_rewal_period',
        ]

class LactatingCowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=1)

    class Meta:
        model = LactatingCow
        fields = ['id', 'user', 'cow_name', 'reg_no', 'sire_details', 'breed',
                  'breeding_level', 'age', 'calving_down_date', 'no_of_calves',
                  'average_daily_milk', 'lactation_stage', 'expected_date_of_drying_off']


class MilkRecordSerializer(serializers.ModelSerializer):
    cow_name = serializers.SlugRelatedField(queryset=LactatingCow.objects.all(), slug_field='cow_name')
    employee_name = serializers.SlugRelatedField(queryset=Employees.objects.all(), slug_field='id')
    class Meta:
        model = MilkRecord
        fields = ['id','user', 'cow_name', 'employee_name', 'date', 'time_of_milking', 'quantity']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Concatenate id and employee_name
        employee_instance = Employees.objects.get(id=data['employee_name'])  # Retrieve employee instance using employee_name field
        data['employee_names'] = employee_instance.employee_name 
        #print(data)
        return data
class WeeklyMilkRecordSerializer(serializers.ModelSerializer):
    cow_name = serializers.SlugRelatedField(queryset=LactatingCow.objects.all(), slug_field='cow_name')
    
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = WeeklyMilkRecord
        fields = ['id','cow_name',  'week_start_date', 'total_quantity']

    def get_total_quantity(self, obj):
        week_end_date = obj.week_start_date + timedelta(days=6)
        total_quantity = MilkRecord.objects.filter(
            cow_name=obj.cow_name,
            date__range=[obj.week_start_date, week_end_date]
        ).aggregate(Sum('quantity'))['quantity__sum'] or 0.0
        return total_quantity

class DailyMilkRecordSerializer(serializers.ModelSerializer):
    cow_name = serializers.SlugRelatedField(queryset=LactatingCow.objects.all(), slug_field='cow_name')
    
    class Meta:
        model = DailyMilkRecord
        fields = ['id','cow_name', 'date', 'total_quantity']

class MonthlyMilkRecordSerializer(serializers.ModelSerializer):
    cow_name = serializers.SlugRelatedField(queryset=LactatingCow.objects.all(), slug_field='cow_name')
    
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = MonthlyMilkRecord
        fields = ['id','cow_name', 'month', 'total_quantity']

    def get_total_quantity(self, obj):
        start_date = obj.month.replace(day=1)
        next_month = start_date.month % 12 + 1
        year = start_date.year if next_month > 1 else start_date.year + 1
        end_date = date(year, next_month, 1) - timedelta(days=1)
        total_quantity = MilkRecord.objects.filter(
            cow_name=obj.cow_name,
            date__range=[start_date, end_date]
        ).aggregate(Sum('quantity'))['quantity__sum'] or 0.0
        return total_quantity

class BuyerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Buyer
        fields = ['id','user','name', 'category', 'contact','date_of_enrollment','duration_of_supply','payment_mode','agreed_price_per_kg']

class OtherExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherExpense
        fields = ['id', 'date', 'description', 'cost', 'comment']
            
class SalesOfMilkSerializer(serializers.ModelSerializer):
    # accepts the buyer's ID in POST/PATCH/PUT
    buyer = serializers.PrimaryKeyRelatedField(
        queryset=Buyer.objects.all(),
        write_only=True          # hide the numeric ID in the response (optional)
    )
    # shows the buyer's name in GET responses
    buyer_name = serializers.CharField(
        source='buyer.name',
        read_only=True
    )

    class Meta:
        model = SalesOfMilk
        fields = [
            'id',
            'user',
            'date_of_sales',
            'milk_sales_to',
            'buyer',          # ID expected on write
            'buyer_name',     # name returned on read
            'balance',
            'total_cash_received',
            'comment',
        ]


class PaymentsSerializer(serializers.ModelSerializer):
    payment_received_from = serializers.CharField(source='buyer.name', read_only=True)
    buyer = serializers.PrimaryKeyRelatedField(queryset=Buyer.objects.all(), write_only=True)
    category_of_buyer = serializers.ReadOnlyField(source='buyer.category')
    buyer_choices = serializers.SerializerMethodField()
    category_choices = serializers.SerializerMethodField()

    class Meta:
        model = Payments
        fields = [
            'id',
            'user',
            'category',
            'buyer',
            'buyer_choices',
            'category_choices',
            'category_of_buyer',
            'date_of_payment',
            'total_kg_supplied',
            'price_per_kg',
            'total_amount_to_receive',
            'previous_balance',
            'grand_total',
            'amount_received',
            'balance',
            'payment_received_from',
            'payment_received_by',
            'contracts',
            'remarks',
        ]

    def get_buyer_choices(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            buyers = Buyer.objects.filter(user=request.user)
        else:
            buyers = Buyer.objects.none()

        return [{'id': b.id, 'name': b.name, 'category': b.category} for b in buyers]

    def get_category_choices(self, obj):
        return [{'value': key, 'label': val} for key, val in Payments.CATEGORIES]
    
class VeterinaryBillingSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = VeterinaryBilling
        fields = ['id','user','assigned_to', 'billing_category','other_billing_category','total_amount_billed', 'total_paid', 'balance', 'mode_of_payment',
                  'agreed_date', 'payment_plan', 'farmer_name', 'village', 'contact','vet_to_be_paid','vet_category',
                  'reg_no', 'vet_contact', 'signature']
        read_only_fields=['balance']

class DewormingSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Deworming
        fields = ['id','user','assigned_to', 'species_targeted', 'other','animal_name','no_of_adults', 'no_of_young_ones', 'body_conditions',
                    'deworming_date', 'drug_of_choice', 'parasites', 'withdrawal_period', 'side_effects',
                    'nxt_deworming_date', 'farmer_name', 'village', 'contact','vet_name','vet_category', 'reg_no', 'vet_contact',
                    'signature']

class ArtificialInseminationSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    assigned_to_cooperative = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(),required=False,allow_null=True)

    class Meta:
        model = ArtificialInsemination
        fields = [
            'id', 'user', 'assigned_to', 'assigned_to_official','assigned_to_cooperative','assigned_by', 'farm_name', 'species', 'cow_name', 
            'reg_no','animal_status', 'dam_details','sire_details', 'no_of_repeats', 'rab_status', 'abortion_status', 
            'time_of_heat_sign', 'date_of_heat_sign', 'insemination_date', 'insemination_time', 'insemination_status', 
            'semen_type', 'breed_used', 'other_breed', 'bull_name', 'bull_reg_no', 'semen_source', 'other_source', 
            'heat_sign_mtr_date', 'repeat_heat_date', 'first_pd_date', 'expected_delivery_date', 'owners_name', 
            'sub_county', 'ward', 'village', 'contact',  'vet_name', 'vet_category', 'vet_reg_no', 
            'vet_contact', 'signature_stamp'
        ]
        read_only_fields = ['assigned_by', 'heat_sign_mtr_date', 'repeat_heat_date', 'first_pd_date', 'expected_delivery_date']

   

class PregnancyDiagnosisSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = PregnancyDiagnosis
        fields = ['id','user','assigned_to', 'cow_name', 'reg_no', 'category', 'date_of_ai', 'pg_diag_date', 'pd_results',
                  'pd_method', 'positive_pd_months', 'negative_pd_comment', 'pd_nxt_date', 'expctd_delivery_date',
                  'comment', 'owners_name', 'village', 'contact','vet_name','vet_category', 'vet_reg_no', 'vet_contact',
                  'signature']

class FarmConsultationSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = FarmConsultation
        fields = ['id','user','assigned_to','visit_date','area_of_interest','other','recommendation', 
                   'manager',  'farmer_name', 'contact', 'village',
                  'vet_name','vet_category', 'vet_reg_no', 'vet_contact', 'signature']

class ReferralSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Referral
        fields = ['id','user','assigned_to', 'species', 'treatment_duration', 'previous_treatment_state', 'prognosis',
                  'referral_date', 'referral_choice', 'r_vet_name', 'r_vet_contact',
                  'farmer_name', 'village', 'contact','vet_name','vet_category', 'vet_reg_no', 'vet_contact', 'signature',
                  'stamp', 'comment']
        
class SurgicalRecordSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = SurgicalRecord
        fields = [
            'id',
            'user',
            'assigned_to',
            'livestock_category_affected',
            'other_livestock_category',
            'name_of_animal',
            'registration_number',
            'sex_of_animal',
            'age_of_animal',
            'nature_of_surgery',
            'type_of_surgery',
            'other_surgery',
            'status_before_operation',
            'pre_operative_management',
            'date_of_operation',
            'post_operation_management',
            'prognosis_of_patient',
            'case_history',
            'comment',
            'owner_name',
            'owner_village',
            'owner_mobile_number',
           
            'practitioner',
            'vet_category',
            'vet_mobile_number',
            'signature',
            
        ]

class SampleCollectionSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = SampleCollection
        fields = [
            'id',
            'user',
            'assigned_to',
            'livestock_category',
            'other_livestock',
            'name_of_animal',
            'registration_number',
            'age_of_animal',
            'sex_of_animal',
            'history_of_animal',
            'clinical_signs_of_animal',
            'type_of_sample_collected',
            'date_of_sampling',
            'sample_storage_condition',
            'means_of_transportation',
            'sample_rating',
            'owner_name',
            'owner_village',
            'owner_mobile_number',
           
            'vet_in_charge_name',
            'vet_category',
            'vet_in_charge_registration_number',
            'vet_in_charge_mobile_number',
            'signature',
            
        ]

class SampleProcessingSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = SampleProcessing
        fields = [
           'id',  
            'user',
            'assigned_to',
            'livestock_category',
            'type_of_sample_received',
            'sample_rating',
            'animal_name',
            'registration_number',
            'sex_of_animal',
            'age_of_animal',
            'date_of_reception',
            'date_of_sample_processing',
            'number_of_days_for_processing',
            'date_of_sample_results',
            'laboratory_findings',
            'comment',
            'owner_name',
            'owner_village',
            'owner_mobile_number',
            'lab_technologist_name',
            'lab_technologist_registration_number',
            'lab_technologist_mobile_number',
            'laboratory_name',
            'signature',
            
        ]
class LaboratoryRecordSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = LaboratoryRecord
        fields = [
            'id',
            'user',
            'assigned_to',
            'livestock_category',
            'other_livestock',
            'name_of_animal',
            'registration_number',
            'age_of_animal',
            'sex_of_animal',
            'history_of_animal',
            'clinical_signs',
            'type_of_sample_collected',
            'date_of_sampling',
            'sample_storage_condition',
            'means_of_transportation',
            'sample_rating',
            'owner_name',
            'owner_village',
            'owner_mobile_number',
            'vet_in_charge_name',
            'vet_registration_number',
            'vet_mobile_number',
           'signature',
            'stamp'
        ]
class LivestockIncidentSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = LivestockIncident
        fields = [
            'id',
            'user',
            'assigned_to',
            'livestock_category',
            'animal_name',
            'sex',
            'age',
            'case_history',
            'number_of_sick_animals',
            'morbidity_rate',
            'incidence_date',
            'incidence_time',
            'cadaver_signs',
            'open_for_pm',
            'no_pm_reason',
            'path_condition',
            'sample_sent',
            'cause_notifiable',
            'cause_zoonotic',
            'precaution',
            'disposal_way',
        ]
class VaccinationRecordSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = VaccinationRecord
        fields = [
            'id',
            'user',
            'assigned_to',
            'assigned_to_official',
            #'assigned_by',
            'species_targeted',
            'other_species',
            'number_of_animals_vaccinated',
            'age_of_animal',
            'sex_of_animal',
            'breed_of_animal',
            'color_of_animal',
            'other_description',
            'vaccination_of',
            'other_disease',
            'vaccines_used',
            'batch_number',
            'dosage',
            'expiry_date',
            'date_of_vaccination',
            'vaccination_type',
            'next_date_of_vaccination',
            'name_of_rash',
            'village_vaccination_done',
            'nature_of_vaccination_program',
            'name_of_owner',
            'sub_county',
            'ward',
            'village',
            'contact',
            
            'name_of_vet_incharge',
            'vet_category',
            'registration_number',
            'mobile_number',
            'signature',
            
        ]
        read_only_fields = ['assigned_by']

    
class PostMortemRecordSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = PostMortemRecord
        fields = [
            'id',
            'user',
            'assigned_to',
            'livestock_category',
            'other_livestock',
            'name_of_animal',
            'reg_no',
            'sex',
            'age',
            'case_history',
            'number_of_sick_animals',
            'number_of_dead',
            'morbidity_rate',
            'date_of_incidence',
            'time_of_incidence',
            'signs_of_cadaver',
            'cadaver_open_for_pm',
            'reasons_for_not_opening',
            'major_pathological_conditions',
            'cause_of_death',
            'sample_sent_to_lab',
            'cause_of_death_notifiable',
            'cause_of_death_zoonotic',
            'precautions_if_zoonotic',
            'cadaver_disposed_by',
            'owner_name',
            'owner_village',
            'owner_mobile_number',
            
            'vet_in_charge_name',
            'vet_category',
            'vet_in_charge_registration_number',
            'vet_in_charge_mobile_number',
            'signature',
            
        ]
        
class ClinicalRecordSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = ClinicalRecord
        fields = [
            'id',
            'user',
            'assigned_to',
            'animal_species_affected',
            'other_species',
            #'number_of_animals_sick',
            'name_of_animal_affected',
            'registration_number',
            'age_of_animal',
            'breed_of_animal',
            'nature_of_disease',
            'case_history',
            'refer_case_to_other_vet',
            'clinical_signs',
            'prognosis',
            'differential_diagnosis',
            'final_diagnosis',
            'treatment_plan',
            'drugs_of_choice',
            'date_of_start_dose',
            'final_treatment_date',
            'is_zoonotic',
            'precautions',
            'is_disease_notifiable',
            'notified_authority',
            'comment',
            'owner_name',
            'owner_village',
            'owner_contact',
            
            'vet_in_charge_name',
            'vet_category',
            'vet_registration_number',
            'vet_contact',
            'vet_signature',
            
        ]
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','user', 'date_of_enrollment', 'full_name', 'mobile_number', 'location', 'livestock_interest', 'remarks']
        
class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id','user', 'date','time_of_event', 'main_activity', 'client_contact', 'remarks']
        
class DiseaseReportSerializer(serializers.ModelSerializer):
    #assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = DiseaseReport
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'date',
            'livestock_category',
            'other_livestock_category',
            'number_of_animals_affected',
            'sex_of_animals_affected',
            'age_of_animals_affected',
            'clinical_signs',
            'number_of_dead_animals',
            'propose_control_measures',
            'sample_taken_to_lab',
            'tentative_diagnosis',
            'village_disease_occurred',
            'sub_county',
            'county',
            'owner_name',
            'owner_mobile_number',
            'vet_in_charge_name',
            'vet_registration_number',
            'vet_mobile_number',
            'signature',
           
        ]
        

# Slaughterhouse Serializer
class SlaughterhouseSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    assigned_to_vet = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Slaughterhouse
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'assigned_to_vet',
            'reg_date',
            'name', 
            'county', 
            'sub_county', 
            'location',
            'slaughterhouse_status',
            'slaughterhouse_category', 
            'livestock_slaughtered', 
            'number_of_employees', 
            'roller_mark_number',
            'inspector_name',
            'inspector_registration_number',
            'inspector_employment_number',
            'inspector_mobile_number'
        ]


# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    assigned_to_vet = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    slaughterhouse = serializers.CharField()

    class Meta:
        model = Employee
        fields = [
            'id',
            'user',
            'assigned_to_vet',
            'enrollment_date',
            'slaughterhouse',
            'name',
            'id_number',
            'mobile_number',
            'position',
            'medical_license_status',
        ]

# Butcher Serializer
class ButcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Butcher
        fields = [
            'id', 
            'user',
            'enrollment_date',
            'name', 
            'id_number', 
            'mobile_number', 
            'medical_license_status', 
            'livestock_slaughtered', 
            'meat_container_number', 
            'meat_carrier_number', 
            'means_of_transport'
        ]

class InvoiceSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Invoice
        fields = [
            'id',
            'user',
            'assigned_to',
            'invoice_category',
            'other_invoice_category',
            'invoice_particulars',
            'date_of_invoice',
            'total_amount_due',
            'payment_method',
            'farmer_name',
            'village',
            'contact',
           
            'vet_in_charge_of_invoice',
            'vet_category',
            'vet_registration_number',
            'vet_contact',
            'signature',
            
        ]
        
        
# class ChoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Choice
#         fields = ['id', 'text']

# class QuestionSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True, read_only=True)

#     class Meta:
#         model = Question
#         fields = ['id', 'text', 'choices']

# class UserAnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserAnswer
#         fields = ['id','user', 'question', 'choice']
        
        
#tutorial
        
class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpdChoices
        fields = ['id', 'text', 'is_correct']


class SectionSerializer(serializers.ModelSerializer):
    lesson_id = serializers.IntegerField(source='lesson.id', read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'lesson_id', 'lesson', 'title', 'content','file','is_paid','created_at']

class TutorialSerializer(serializers.ModelSerializer):
    #user_has_paid = serializers.SerializerMethodField()
    has_paid = serializers.BooleanField(read_only=True)

    class Meta:
        model = Tutorial
        fields = [
            'id', 
            'lesson', 
            'cpd_number', 
            'unit_price', 
            'points', 
            'presented_by',
            'contact_hours',
            'is_paid', 
            'created_at', 
            'has_paid',
            
        ]

    def get_user_has_paid(self, obj):
        # Get the user from request context
        user = self.context['request'].user

        # Return True only if the tutorial belongs to this user AND is_paid is True
        return obj.user_id == user.id and obj.is_paid
        
class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'section', 'author', 'author_name', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
        
# class UserAnswersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserAnswers
#         fields = ['user', 'question', 'choice']
#cpd quiz
class CpdChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpdChoices
        fields = ['id', 'choice_text','is_correct']

class CpdQuestionsSerializer(serializers.ModelSerializer):
    choices = CpdChoicesSerializer(many=True)

    class Meta:
        model = CpdQuestions
        fields = ['id', 'question_text', 'choices']

class QuizResultSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  
    section = serializers.StringRelatedField()  

    class Meta:
        model = QuizResult
        fields = ['id', 'user', 'section', 'score', 'passed', 'timestamp']
        # read_only_fields = ['id', 'timestamp']
# class QuestionResultSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField()  
      

#     class Meta:
#         model = QuestionResult
#         fields = ['id', 'user', 'score', 'passed', 'timestamp']
#         # read_only_fields = ['id', 'timestamp']
       
class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = '__all__'
        
class LivestockExaminationRecordSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = LivestockExaminationRecord
        fields = [
            'id',
            'user',
            'assigned_to',
            'livestock_category',
            'other_category',
            'age_of_animal',
            'breed',
            'sex_of_animal',
            'number_of_animals',
            'origin_of_animal',
            'destination',
            'reason_for_examination',
            'recommendation',
            'owner_name',
            'owner_mobile_number',
            'veterinary_officer_in_charge',
            'registration_number',
            'veterinary_officer_mobile_number',
            'veterinary_officer_signature',
            'created_at',
        ]

class CalvingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalvingRecord
        fields = [
            'id',
            'user',
            'date_of_calving',
            'insemination_date',
            'days_to_calving_down',
            'cow_name',
            'registration_number',
            'calving_procedure',
            'rab_status',
            'hours_for_natural_expulsion',
            'calf_sex',
            'calf_status',
            'reason_for_dead_foetus',
            'comment',
            'created_at',
        ]
        read_only_fields = ['days_to_calving_down', 'created_at']
class AssessmentRecordSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())


    class Meta:
        model = AssessmentRecord
        fields = [
            'id',
            'user',
            'assigned_to',
            'livestock_category',
            'other_category',
            'breed',
            'date_of_assessment',
            'name_of_animal',
            'registration_number',
            'color_of_animal',
            'age_of_animal',
            'sex_of_animal',
            'number_of_animals',
            'origin_of_animal',
            'place_of_assessment',
            'destination',
            'reason_for_assessment',
            'recommendation',
            'owner_of_animal',
            'owner_mobile_number',
            'veterinary_practitioner_in_charge',
            'practitioner_registration_number',
            'practitioner_contact',
            'signature_and_stamp',
        ]
        
class DailyKillSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    
    assigned_by = serializers.StringRelatedField()
    

    class Meta:
        model = DailyKill
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'assigned_by',
            'date',
            'livestock_category',
            #'number_of_females_killed',
            #'number_of_males_killed',
            'total_kills_per_day',
            'condemnation_done',
            'condemnation_status',
            'comment_by_inspector',
            'inspector_name',
            'inspector_reg_number',
            'inspector_status',
        ]
class MovementPermitSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

 # Displays assigned_to as a string
    class Meta:
        model = MovementPermit
        fields = [
            'id', 'user', 'assigned_to_official', 'date_of_permit', 'sub_county_district',
            'ward_level', 'authorized_by', 'registration_number', 'phone_number',
            'uploaded_permit'
        ]


class NoObjectionSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())


    class Meta:
        model = NoObjection
        fields = [
            'id', 'user', 'assigned_to_official', 'date_of_confirmation', 'sub_county_district',
            'ward_level', 'confirmed_by', 'registration_number', 'phone_number',
            'uploaded_no_objection_form'
        ]


class MonthlyReportSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())


    class Meta:
        model = MonthlyReport
        fields = [
            'id', 'user', 'assigned_to_official', 'date_of_submission', 'sub_county',
            'ward_level', 'submitted_by', 'registration_number', 'phone_number',
            'uploaded_report'
        ]
class QuarterlyReportSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())


    class Meta:
        model = QuarterlyReport
        fields = [
            'id', 'user', 'assigned_to_official', 'date_of_submission', 'sub_county',
            'ward_level', 'submitted_by', 'registration_number', 'phone_number',
            'uploaded_report'
        ] 
class YearlyReportSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())


    class Meta:
        model = YearlyReport
        fields = [
            'id', 'user', 'assigned_to_official', 'date_of_submission', 'sub_county',
            'ward_level', 'submitted_by', 'registration_number', 'phone_number',
            'uploaded_report'
        ]      
class PractitionerSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())


    class Meta:
        model = Practitioner
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'assigned_by',
            'first_name',
            'last_name',
            'reg_date',
            'phone_number',
            'email',
            'county',
            'subcounty',
            'ward',
            'area_of_operation',
            'specialization',
            'vet_category',
            'registration_number',
            'employment_status'
        ]
        read_only_fields=['assigned_by']

class UterineIrrigationRecordSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = UterineIrrigationRecord
        fields = [
            'id',  
            'user',
            'assigned_to',
            'livestock_category',
            'name_of_animal',
            'registration_number',
            'registration_date',
            'reason',
            'number_of_repeats',
            'abortion_status_history',
            'rabies_status_history',
            'exp_ex_date',
            'previous_insemination_by',
            'treatment_plan',
            'drugs_of_choice',
            'comment',
            'owner_name',
            'village',
            'contact',
    
            'vet_in_charge',
            'vet_category',
            'registration_number_vet',
            'contact_vet',
            'sign_and_stamp',
        ]



class EmergencyCareSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = EmergencyCare
        fields = [
            'id',
            'user',
            'assigned_to',
            'date',
            'livestock_category',
            'other_category',
            'number_of_animals_affected',
            'name_of_affected_animal',
            'registration_number',
            #'registration_date',
            'emergency_category',
            'condition_of_emergency',
            'case_history',
            'clinical_signs',
            'prognosis',
            'differential_diagnosis',
            'final_diagnosis',
            'referral_status',
            'treatment_plan',
            'drugs_of_choice',
            #'comment',
            'owner_name',
            'village',
            'contact',
    
            'vet_category',
            'vet_registration_number',
            'vet_contact',
            'signature_and_stamp',
        ]
class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = [
            'id',
            'user',
            'date_of_purchase',
            'product_name',
            'manufacturing_company',
            'buying_price',
            'retail_price',
            'wholesale_price',
            'expiring_date',
        ]
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'id',
            'user',
            'date_of_enrollment',
            'supply_number',
            'name',
            'mobile_number',
            'location',
            'business_name',
            'mode_of_payment',
            'account_details',
        ]
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'user',
            'date_of_enrollment',
            'name',
            'mobile_number',
            'location',
            'remarks',
        ]
        
class CreditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creditor
        fields = [
            'id',
             'user',
            'date_of_transaction',
            'name',
            'mobile_number',
            'total_amount_to_pay',
            'amount_paid',
            'balance_to_pay',
            'agreed_date_of_balance_payment',
            'remarks',
        ]
class DebtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debtor
        fields = [
            'id',
             'user',
            'date_of_transaction',
            'name',
            'mobile_number',
            'invoice_no',
            'total_invoice_amount',
            'correction_done',
            'amount_of_correction',
            'total_amount_to_pay',
            'previous_balance',
            'grand_total',
            'amount_paid',
            'balance_to_pay',
            'remarks',
        ]
class ClientRequestSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(
        slug_field='username', 
        queryset=User.objects.filter(is_vet_officer=True)
    )
    assigned_by = serializers.SlugRelatedField(
        slug_field='username', 
        queryset=User.objects.filter(is_farmer=True),
        required=False,  # Make it optional because we'll set it automatically
        allow_null=True
    )
    consent_display = serializers.SerializerMethodField()  # Read-only display field
    consent = serializers.BooleanField()  # Editable field

    class Meta:
        model = ClientRequest
        fields = [
            'id', 
            'user',
            'assigned_to',
            'assigned_by', 
            'farmer_name',
            'contact',
            'location',
            'date_of_request',
            'time_of_request',
            'telemedicine_category',
            'request_type', 
            'communication_methods',
            'emergency_condition',
            'non_emergency_condition', 
            'case_history',
            'livestock_category', 
            'other_livestock_category', 
            'consultation_fee', 
            'photo',
            'consent', 
            'status', 
            'judgement',         
            'consent_display',
        ]
        read_only_fields = ['user', 'farmer_name', 'contact', 'assigned_by', 'location']  # Prevent manual input

    def get_consent_display(self, obj):
        return "Yes" if obj.consent else "No"

    def create(self, validated_data):
        request = self.context["request"]  # Get the request object
        user = request.user  # Get the authenticated user

        validated_data["user"] = user  # Set the authenticated user as the request owner

        # If 'assigned_to' exists, set 'assigned_by' to the authenticated user
        if "assigned_to" in validated_data and validated_data["assigned_to"]:
            validated_data["assigned_by"] = user

        return super().create(validated_data)

class VetJudgmentSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.filter(is_farmer=True))

    class Meta:
        model = VetJudgment
        fields = [
            'id', 
            'user',
            'assigned_to', 
            'date_of_judgment', 
            'telemedicine_category', 
            'request_type', 
            'emergency_condition',
            'non_emergency_condition',
            'livestock_category',
            'other_livestock_category',
            'tentative_diagnosis',
            'prognosis',
            'practitioner_judgment',
            'prescription_details',
            'vet_name', 
            'kvb_no', 
            'vet_category', 
            'vet_contact', 
            'referral_details',
        ]
        read_only_fields = ['vet_name', 'kvb_no', 'vet_category', 'vet_contact']  # Prevent manual input
        
class DailyCheckSerializer(serializers.ModelSerializer):
    #check_section_display = serializers.CharField(source='get_check_section_display', read_only=True)
    #section_status_display = serializers.CharField(source='get_section_status_display', read_only=True)

    class Meta:
        model = DailyCheck
        fields = [
            'id',
            'user',
            'date_of_check',
            'time_of_check',
            'check_section',
            'remarks',
            'checked_by',
            'contact',
        ]
       # read_only_fields = ['user']
class ManagementCommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementCommittee
        fields = [
            'id',
            'user',
            'name',
            'id_number',
            'contact',
            'position',
            'date_of_enrolment',
            'date_of_election',
            'time_period',
            'next_election_date',
            'remarks',
        ]


class HidesAndSkinsRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HidesAndSkinsRecord
        fields = [
            'id',
             'user',
            'date_of_kills',
            'category',
            'number_collected',
            'date_of_transportation',
            'means_of_transportation',
            'reg_no_of_vehicle',
            'taken_by',
            'contact',
            'remarks',
        ]
class ApprovedDairyFarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovedDairyFarm
        fields = [
            'id',
            
            'date_of_approval',
            'name_of_farm',
            'county',
            'sub_county',
            'location',
            'name_of_owner',
            'contact',
            'farm_breeding_level',
            'average_milk_per_cow',
            'highest_milk_producer',
            'approved_by',
            'designation',
            'officer_contact',
            'comment',
        ]
class SlaughterhouseHygieneSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlaughterhouseHygiene
        fields = [
            'id',
             'user',
            'date_of_cleaning',
            'cleaning_category',
            'cleaning_procedure',
            'state_other_cleaning',
            'cleaning_done_by',
            'contact_of_cleaner',
            'supervised_by',
            'supervisor_contact',
            'remarks',
        ]


class SlaughterhouseAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlaughterhouseAsset
        fields = [
            'id',
             'user',
            'date_of_entry',
            'type_of_asset',
            'other_asset',
            'model_number',
            'registration_number',
            'original_cost',
            'appossession_value',
            'depossession_value',
            'remarks',
        ]
class LivestockRegistrationSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = LivestockRegistration
        fields = [
            "id",
            "user",
            "livestock_type",
            "date_of_registration",
            "breed",
            "sex",
            "age",
            "body_weight",
            "colour",
            "number_of_births",
            "given_name",
            "registration_number",
            "breeding_level",
            "dam_details",
            "sire_details",
            "origin",
            "country_of_importation",
            "source",
            "farm_name",
            "owner_name",
            "owner_phone",
            "owner_id_number",
            "county",
            "sub_county",
            "village",
           
            "practitioner_name",
            "reg_number",
            "contact",
            "signature_and_stamp",
            "photo",
            
        ]
        
class VeterinaryEPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeterinaryEPrescription
        fields = [
            "id",
            "user",
            "pharmacy_name",
            "location",
            "vet_practitioner_incharge",
            "kvb_no",
            "licence_no",
            "contact",
            "sign",
            "signed_on",
            "drug_category",
            "prescription_target",
            "date_of_prescription",
            "livestock_type",
            "breed",
            "age",
            "drug_trade_name",
            "manufacturing_company",
            "batch_number",
            "drug_dosage",
            "route_of_administration",
            "drug_volume",
            "clinical_use",
            "duration_of_treatment",
            "withdrawal_period",
            "quantity_purchased",
            "storage_condition",
            "side_effect",
            "expiry_date",
            "vets_comments",
            "buyer_name",
            "buyer_category",
            "buyer_kvb_no",
            "buyer_licence_no",
            "buyer_signature",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        
class RoutineManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineManagement
        fields = [
            "id",
            "user",
            "date_of_service",
            "livestock_category",
            "number_of_animals",
            "animal_name",
            "reg_no",
            "age",
            "routine_management",
            "other_management_practice",
            "owner_name",
            "village",
            "contact",
            
            "vet_practitioner_incharge",
            "vet_category",
            "vet_reg_no",
            "signature_and_stamp",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        
class AbortionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbortionRecord
        fields = [
            "id",
            "user",
            "livestock_category",
            "number_of_animals_aborted",
            "animal_name",
            "reg_no",
            "date_of_insemination",
            "date_of_abortion",
            "reason_for_abortion",
            "other_reason",
            "treatment_given",
            "remarks",
            "owner_name",
            "contact",
            "village",
           
            "vet_practitioner_name",
            "vet_category",
            "vet_reg_no",
            "vet_contact",
            "signature_and_stamp",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        
class ExtensionServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtensionService
        fields = [
            "id",
            "date_of_extension",
            "venue",
            "target_group",
            "topic_covered",
            "number_of_participants",
            "female_attendance",
            "male_attendance",
            "children_attendance",
            "name_of_group",
            "location",
            "group_project",
            "village",
            "sub_county",
            "chairperson",
            "secretary",
            "treasurer",
            "member",
            "facilitator_name",
            "facilitator_contact",
            "gps_token",
            "extension_organized_by",
            "remarks",
            "group_photo",
            "created_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_by", "created_at", "updated_at"]
        
class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_farmer', 'is_vet_officer']
        

class FieldQuotationSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.filter(is_farmer=True))
    class Meta:
        model = FieldQuotation
        fields = [
            'id',
            'user',
            'assigned_to',
            'date_of_quotation',
            'quotation_category',
            'number_of_animals',
            'payment_description',
            'amount_to_payment',
            'name_of_farm',
            'owner_name',
            'owner_contact',
            'services_provided_by',
            'practitioner_name',
            'kvb_registration_number',
            'practitioner_contact',
            'signature_and_stamp',
        ]
        read_only_fields = ['user'] 
        
        
class DairyFarmerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DairyFarmerRegistration
        fields = [
            "id",
            "user",
            "date_of_registration",
            "full_name",
            "mobile_number",
            "total_number_of_dairy_cows",
            "number_of_lactating_cows",
            "breeds_used",
            "location",
            "milk_supply_number",
        ]


class MilkCollectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkCollectionCenter
        fields = [
            "id",
            "user",
            "date_of_enrollment",
            "name_of_collection_centre",
            "location",
            "agent_incharge",
            "mobile_number",
            "approximate_number_of_farmers",
            "means_of_transfer",
            "transporter_name",
            "transporter_mobile",
            "time_of_milk_collection",
        ]


class CurrentMilkPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentMilkPrice
        fields = [
            "id",
            "user",
            "date_of_amendment",
            "last_milk_price",
            "current_milk_price",
            "remarks",
        ]


class FarmerMilkPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerMilkPayment
        fields = [
            "id",
            "user",
            "date_of_payment",
            "milk_supply_number",
            "name_in_full",
            "total_milk_supplied",
            "amount_to_be_paid",
            "amount_paid",
            "balance",
            "remarks",
        ]
        
class MilkCollectionCoolerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkCollectionCooler
        fields = [
            'id',
            'user',
            'date',
            'location',
            'supply_number',
            'collection_status',
            'reason',
            'total_kg_supplied',
            'name_of_supplier',
            'remarks'
        ]

class MilkCollectionClerkSerializer(serializers.ModelSerializer):

    class Meta:
        model = MilkCollectionClerk
        fields = [
            "id",
            "user",
            "location",
            "date",
            "supply_number",
            
            "total_kg_supplied"
        ]
# Serializer for MilkCollectionCenterRecord
class MilkCollectionCenterRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = MilkCollectionCenterRecord
        fields = [
            'id',
            'user',
            'date',
            'supply_number',
            'collection_status',
            'reason',
            'total',
            'name_of_center',
            'name_of_agent',
            'remarks'
        ]
class DailyRevenueCollectionSerializer(serializers.ModelSerializer):

    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())


    class Meta:
        model = DailyRevenueCollection
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'date_of_record',
            'sub_county',
            'source_of_revenue',
            'total_collection',
            'remarks',
            'created_at',
            'updated_at',
        ]
class LeaveRequestSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())


    class Meta:
        model = LeaveRequest
        fields = (
            'id',
            'user',
            'assigned_to_official',
            'date_of_leave_request',
            'sub_county',
            'total_annual_leave_days',
            'days_of_leave_taken',
            'remaining_days',
            'reason_for_leave',
            'name_of_officer',
            'employment_number',
            'working_station',
            'leave_status',
            'remarks',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('id', 'created_at', 'updated_at', 'leave_status')
        
class MovementPermitsSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = MovementPermits
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'date_of_record',
            'sub_county',
            'livestock_category',
            'total_animals',
            'price_per_animal',
            'total_revenue_collected',
            'created_at',
        ]
        
        read_only_fields = ['id', 'created_at', 'total_revenue_collected']

    def validate(self, data):
        """
        Optional: Automatically calculate total_revenue_collected 
        before saving if it's not provided or to ensure accuracy.
        """
        total_animals = data.get('total_animals')
        price = data.get('price_per_animal')
        
        if total_animals and price:
            data['total_revenue_collected'] = total_animals * price
            
        return data
class NoObjectionsSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = NoObjections
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'date_of_record',
            'sub_county',
            'livestock_category',
            'number_of_animals',
            'cost_of_no_objection',
            'total_revenue_collected',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at', 'total_revenue_collected']

    def validate(self, data):
        """
        Ensures total_revenue_collected is the product of 
        number_of_animals and cost_of_no_objection.
        """
        count = data.get('number_of_animals')
        unit_cost = data.get('cost_of_no_objection')
        
        if count is not None and unit_cost is not None:
            data['total_revenue_collected'] = count * unit_cost
            
        return data
class DiseaseReportMovsSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = DiseaseReportMov
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'date_of_record',
            'sub_county',
            'livestock_category',
            'number_of_reports',
            'suspected_disease',
            'proposed_intervention',
            'remarks',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']
        
class PractitionersSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    total_practitioners = serializers.ReadOnlyField()

    class Meta:
        model = Practitioners
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'date_of_record',
            'sub_county',
            'number_employed_by_county',
            'number_in_private_practice',
            'total_practitioners'
        ]
class SlaughterHousesSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    total_slaughterhouses = serializers.ReadOnlyField()

    class Meta:
        model = SlaughterHouses
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'date_of_record',
            'sub_county',
            'private_slaughterhouses',
            'county_slaughterhouses',
            'total_slaughterhouses',
            'employed_inspectors',
            'roller_markers'
        ]
        
class DailyKillsSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    total_revenue_collected = serializers.ReadOnlyField()

    class Meta:
        model = DailyKills
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'date_of_record',
            'sub_county',
            'livestock_category',
            'number_of_kills',
            'price_per_kill',
            'total_revenue_collected',
            'remarks'
        ]
        read_only_fields = ['id', 'total_revenue_collected','created_at']
class ArtificialInseminationsSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = ArtificialInseminations
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'date_of_record',
            'sub_county',
            'number_of_cows_served',
            'semen_type',
            'repeat_cases',
            'revenue_collected',
            'remarks',
        ]
class VaccinationsSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Vaccinations
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'date_of_record',
            'sub_county',
            'animal_species',
            'total_vaccinated',
            'vaccine_used',
            'vaccine_source',
            'batch_number',
            'expiry_date',
            'revenue_collected',
            'remarks',
        ]
class ExtensionServicesSerializer(serializers.ModelSerializer):
    assigned_to_official = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = ExtensionServices
        fields = [
            'id',
            'user',
            'assigned_to_official',
            'date_of_record',
            'sub_county',
            'number_of_extensions_done',
            'provider',
            'remarks',
        ]