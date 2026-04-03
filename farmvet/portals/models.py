from django.db import models
from django.contrib.auth.models import User
from user.models import *
from datetime import timedelta, date
from django.contrib import admin
import random

BOMET_SUBCOUNTY_CHOICES = [
('Bomet Central', 'Bomet Central'),
('Bomet East', 'Bomet East'),
('Chepalungu', 'Chepalungu'),
('Sotik', 'Sotik'),
('Konoin', 'Konoin'),
]
 
BREEDING_LEVEL_CHOICES = [
		('Purebred', 'Purebred'),
		('Crossbred', 'Crossbred'),
		('MixedBreed', 'MixedBreed'),
	]
VET_CATEGORY=[
	('surgeon', 'Surgeon'),
  ('technologist', 'Technologist'),
  ('technician', 'Technician')
  ]


SEX_CHOICES = (
 	('Male','Male'),
 	('Female','Female')
 )


farmers_list = []


class VaccinationRecord(models.Model):
    
	CATTLE = 'Cattle'
	SHEEP = 'Sheep'
	GOAT = 'Goat'
	DONKEY = 'Donkey'
	DOG = 'Dog'
	HORSE = 'Horse'
	POULTRY = 'Poultry'
	OTHER = 'Other'

	ANIMAL_SPECIES_CHOICES = [
		(CATTLE, 'Cattle'),
		(SHEEP, 'Sheep'),
		(GOAT, 'Goat'),
		(DONKEY, 'Donkey'),
		(DOG, 'Dog'),
		(HORSE, 'Horse'),
		(POULTRY, 'Poultry'),
		(OTHER, 'Other'),
	]

	PRIMARY = 'Primary'
	BOOSTER = 'Booster'

	VACCINATION_TYPE_CHOICES = [
		(PRIMARY, 'Primary'),
		(BOOSTER, 'Booster'),
	]

	MASS = 'Mass'
	INDIVIDUAL = 'Individual'

	NATURE_OF_VACCINATION_PROGRAM_CHOICES = [
		(MASS, 'Mass'),
		(INDIVIDUAL, 'Individual'),
	]
	VACCINATION_SEX=[
		('Male','Male'),
		('Female','Female'),
		('All','All')

	]

	DISEASE_CHOICES = [
	('anthrax', 'Anthrax'),
	('fmd', 'FMD'),
	('lumpy_skin_disease', 'Lumpy Skin Disease'),
	('rift_valley_fever', 'Rift Valley Fever'),
	('rabies', 'Rabies'),
	('cbpp', 'CBPP '),
	('ccpp', 'CCPP '),
	('ppr', 'PPR '),
	('newcastle_disease', 'Newcastle Disease'),
	('canine_distemper', 'Canine Distemper'),
	('none', 'None'),
	]

    # Fields
    
	user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	assigned_to = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='vaccination',
		limit_choices_to={'is_farmer': False},
		null=True,                 
		blank=True,               
							
	)
	assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='vaccination_official',
		limit_choices_to={'is_official': False},
		null=True,                 
		blank=True,               
							
	)
	assigned_by = models.ForeignKey( 
		User,
		on_delete=models.CASCADE,
		related_name="assigned_vaccination",
		null=True,
		blank=True
	)
	species_targeted = models.CharField(max_length=20,choices=ANIMAL_SPECIES_CHOICES)
	other_species = models.CharField(max_length=255, blank=True, null=True)
	number_of_animals_vaccinated = models.IntegerField()
	age_of_animal = models.CharField(max_length=50)
	sex_of_animal = models.CharField(max_length=10,choices=VACCINATION_SEX)
	breed_of_animal = models.CharField(max_length=100)
	color_of_animal = models.CharField(max_length=100)
	other_description = models.TextField(blank=True, null=True)
	vaccination_of = models.CharField(max_length=20,choices=DISEASE_CHOICES)
	other_disease=models.CharField(max_length=255)
	vaccines_used = models.CharField(max_length=255)
	batch_number = models.CharField(max_length=255)
	dosage = models.CharField(max_length=255)
	expiry_date = models.DateField()
	date_of_vaccination = models.DateField()
	vaccination_type = models.CharField(max_length=10,choices=VACCINATION_TYPE_CHOICES)
	next_date_of_vaccination = models.DateField()
	name_of_rash = models.CharField(max_length=255, blank=True, null=True)
	village_vaccination_done = models.CharField(max_length=255, blank=True, null=True)
	nature_of_vaccination_program = models.CharField(max_length=10,choices=NATURE_OF_VACCINATION_PROGRAM_CHOICES)
	name_of_owner = models.CharField(max_length=255)
	sub_county=models.CharField(max_length=255)
	ward=models.CharField(max_length=255)
	village = models.CharField(max_length=255)
	contact = models.CharField(max_length=50)
	name_of_vet_incharge = models.CharField(max_length=255)
	vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
	registration_number = models.CharField(max_length=255)
	mobile_number = models.CharField(max_length=20)
	signature = models.TextField(blank=True,null=True)

    
	def __str__(self):
		return f"Vaccination Record for {self.user} - {self.species_targeted}"
	def save(self, *args, **kwargs):
		if not self.pk and 'request' in kwargs:  # Ensure it's a new instance
			self.assigned_by = kwargs.pop('request').user
		super().save(*args, **kwargs)


class SurgicalRecord(models.Model):
	LIVESTOCK_CATEGORIES = [
		('Cattle', 'Cattle'),
		('Sheep', 'Sheep'),
		('Goat', 'Goat'),
		('Donkey', 'Donkey'),
		('Dog', 'Dog'),
		('Cat', 'Cat'),
		('Poultry', 'Poultry'),
		('None', 'None')
	]

	SEX_CHOICES = [
		('Male', 'Male'),
		('Female', 'Female')
	]

	AGE_CHOICES = [
		('Young', 'Young'),
		('Adult', 'Adult')
	]

	NATURE_OF_SURGERY = [
		('Emergency', 'Emergency'),
		('Elective', 'Elective')
	]

	TYPE_OF_SURGERY = [
		('C-section', 'C-section'),
		('Interstinal Torsion', 'Interstinal Torsion'),
		('Tumor Extraction', 'Tumor Extraction'),
		('Canine Spaying', 'Canine Spaying'),
		('Hernia', 'Hernia'),
		('Warts Extraction', 'Warts Extraction'),
		('Skin Repairs', 'Skin Repairs'),
		('Castration', 'Castration'),
		('Fracture Correction', 'Fracture Correction'),
		('Rumenotomy', 'Rumenotomy'),
		('None', 'None')
	]

	STATUS_CHOICES = [
		('Good', 'Good'),
		('Dehydrated', 'Dehydrated'),
		('Weak', 'Weak')
	]

	PROGNOSIS_CHOICES = [
		('Good', 'Good'),
		('Fair', 'Fair'),
		('Grave', 'Grave')
	]

	user = models.ForeignKey(User,on_delete=models.CASCADE,default=1,limit_choices_to={'is_vet_officer': True})
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='surgical_records', limit_choices_to={'is_farmer': True})
	livestock_category_affected = models.CharField(max_length=10, choices=LIVESTOCK_CATEGORIES)
	other_livestock_category = models.CharField(max_length=100, blank=True, null=True)
	name_of_animal = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=100)
	sex_of_animal = models.CharField(max_length=6, choices=SEX_CHOICES)
	age_of_animal = models.CharField(max_length=5, choices=AGE_CHOICES)
	nature_of_surgery = models.CharField(max_length=10, choices=NATURE_OF_SURGERY)
	type_of_surgery = models.CharField(max_length=50, choices=TYPE_OF_SURGERY)
	other_surgery = models.CharField(max_length=100, blank=True, null=True)
	status_before_operation = models.CharField(max_length=15, choices=STATUS_CHOICES)
	pre_operative_management = models.TextField(blank=True, null=True)
	date_of_operation = models.DateField()
	post_operation_management = models.TextField(blank=True, null=True)
	prognosis_of_patient = models.CharField(max_length=15, choices=PROGNOSIS_CHOICES)
	case_history = models.TextField(blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
	owner_name = models.CharField(max_length=100)
	owner_village = models.CharField(max_length=100)
	owner_mobile_number = models.CharField(max_length=15)

	practitioner= models.CharField(max_length=100)
	vet_category=models.CharField(max_length=20,choices=VET_CATEGORY)
	vet_mobile_number = models.CharField(max_length=15)
	signature = models.TextField(blank=True,null=True)
	#stamp = models.TextField(blank=True,null=True)


	def __str__(self):
		return f"Surgical Record of {self.name_of_animal} ({self.registration_number})"

class SampleCollection(models.Model):
	LIVESTOCK_CATEGORY_CHOICES = [
		('cattle', 'Cattle'),
		('sheep', 'Sheep'),
		('goat', 'Goat'),
		('dog', 'Dog'),
		('cat', 'Cat'),
		('horse', 'Horse'),
		('poultry', 'Poultry'),
		('none', 'None'),
	]

	SEX_CHOICES = [
		('male', 'Male'),
		('female', 'Female'),
	]

	AGE_CHOICES = [
		('young', 'Young'),
		('adult', 'Adult'),
	]

	SAMPLE_TYPE_CHOICES = [
		('milk', 'Milk'),
		('blood_smear', 'Blood Smear'),
		('lymph_node_smear', 'Lymph Node Smear'),
		('urine', 'Urine'),
		('faeces', 'Faeces'),
		('ear_notching', 'Ear Notching'),
		('biopsy', 'Biopsy'),
		('skin_scraping', 'Skin Scraping'),
		('vaginal_swap', 'Vaginal Swap'),
		('head', 'Head'),
	]

	SAMPLE_RATING_CHOICES = [
		('highly_infectious', 'Highly Infectious'),
		('not_infectious', 'Not Infectious'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection_records', limit_choices_to={'is_farmer': True})
	livestock_category = models.CharField(max_length=10, choices=LIVESTOCK_CATEGORY_CHOICES)
	other_livestock = models.CharField(max_length=100, blank=True, null=True)
	name_of_animal = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=100)
	age_of_animal = models.CharField(max_length=10, choices=AGE_CHOICES)
	sex_of_animal = models.CharField(max_length=6, choices=SEX_CHOICES)
	history_of_animal = models.TextField()
	clinical_signs_of_animal = models.TextField()
	type_of_sample_collected = models.CharField(max_length=20, choices=SAMPLE_TYPE_CHOICES)
	date_of_sampling = models.DateField()
	sample_storage_condition = models.CharField(max_length=100)
	means_of_transportation = models.CharField(max_length=100)
	sample_rating = models.CharField(max_length=20, choices=SAMPLE_RATING_CHOICES)
	owner_name = models.CharField(max_length=100)
	owner_village = models.CharField(max_length=100)
	owner_mobile_number = models.CharField(max_length=15)
	vet_in_charge_name = models.CharField(max_length=100)
	vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
	vet_in_charge_registration_number = models.CharField(max_length=100)
	vet_in_charge_mobile_number = models.CharField(max_length=15)
	signature = models.TextField(blank=True,null=True)
	#stamp = models.TextField(blank=True,null=True)

	def __str__(self):
		return f"{self.name_of_animal} - {self.livestock_category} ({self.date_of_sampling})"



class SampleProcessing(models.Model):
	LIVESTOCK_CATEGORY_CHOICES = [
		('cattle', 'Cattle'),
		('sheep', 'Sheep'),
		('goat', 'Goat'),
		('dog', 'Dog'),
		('cat', 'Cat'),
		('horse', 'Horse'),
		('poultry', 'Poultry'),
		('none', 'None'),
	]

	SEX_CHOICES = [
		('male', 'Male'),
		('female', 'Female'),
	]

	AGE_CHOICES = [
		('young', 'Young'),
		('adult', 'Adult'),
	]

	SAMPLE_RATING_CHOICES = [
		('highly infectious', 'Highly Infectious'),
		('not infectious', 'Not Infectious'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='processing_records', limit_choices_to={'is_farmer': True})
	livestock_category = models.CharField(max_length=10, choices=LIVESTOCK_CATEGORY_CHOICES)
	type_of_sample_received = models.CharField(max_length=255)
	sample_rating = models.CharField(max_length=20, choices=SAMPLE_RATING_CHOICES)
	animal_name = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=100)
	sex_of_animal = models.CharField(max_length=6, choices=SEX_CHOICES)
	age_of_animal = models.CharField(max_length=10, choices=AGE_CHOICES)
	date_of_reception = models.DateField()
	date_of_sample_processing = models.DateField()
	number_of_days_for_processing = models.CharField(max_length=200)
	date_of_sample_results = models.DateField()
	laboratory_findings = models.TextField()
	comment = models.TextField(blank=True, null=True)
	owner_name = models.CharField(max_length=100)
	owner_village = models.CharField(max_length=100)
	owner_mobile_number = models.CharField(max_length=15)
	lab_technologist_name = models.CharField(max_length=100)
	lab_technologist_registration_number = models.CharField(max_length=100)
	lab_technologist_mobile_number = models.CharField(max_length=15)
	laboratory_name = models.CharField(max_length=100)
	signature = models.TextField(blank=True,null=True)
	#stamp = models.TextField(blank=True,null=True)
	def __str__(self):
		return f"{self.name_of_animal} - {self.livestock_category} ({self.date_of_reception})"


class LaboratoryRecord(models.Model):
    LIVESTOCK_CATEGORY_CHOICES = [
        ('cattle', 'Cattle'),
        ('sheep', 'Sheep'),
        ('goat', 'Goat'),
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('horse', 'Horse'),
        ('poultry', 'Poultry'),
        ('none', 'None'),
    ]

    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    AGE_CHOICES = [
        ('young', 'Young'),
        ('adult', 'Adult'),
    ]

    SAMPLE_TYPE_CHOICES = [
        ('milk', 'Milk'),
        ('blood_smear', 'Blood Smear'),
        ('lymph_node_smear', 'Lymph Node Smear'),
        ('urine', 'Urine'),
        ('faeces', 'Faeces'),
        ('cfs', 'CFS'),
        ('biopsy', 'Biopsy'),
        ('skin_scraping', 'Skin Scraping'),
        ('vaginal_swap', 'Vaginal Swap'),
        ('head', 'Head'),
    ]

    SAMPLE_RATING_CHOICES = [
        ('highly_infectious', 'Highly Infectious'),
        ('not_infectious', 'Not Infectious'),
    ]

    TRANSPORTATION_CHOICES = [
        ('vehicle', 'Vehicle'),
        ('motorbike', 'Motorbike'),
        ('footing', 'Footing'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lab_records', limit_choices_to={'is_farmer': True})
    livestock_category = models.CharField(max_length=10, choices=LIVESTOCK_CATEGORY_CHOICES)
    other_livestock = models.CharField(max_length=100, blank=True, null=True)
    name_of_animal = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    age_of_animal = models.CharField(max_length=10, choices=AGE_CHOICES)
    sex_of_animal = models.CharField(max_length=6, choices=SEX_CHOICES)
    history_of_animal = models.TextField()
    clinical_signs = models.TextField()
    type_of_sample_collected = models.CharField(max_length=20, choices=SAMPLE_TYPE_CHOICES)
    date_of_sampling = models.DateField()
    sample_storage_condition = models.CharField(max_length=255)
    means_of_transportation = models.CharField(max_length=10, choices=TRANSPORTATION_CHOICES)
    sample_rating = models.CharField(max_length=20, choices=SAMPLE_RATING_CHOICES)
    owner_name = models.CharField(max_length=100)
    owner_village = models.CharField(max_length=100)
    owner_mobile_number = models.CharField(max_length=15)
    vet_in_charge_name = models.CharField(max_length=100)
    vet_registration_number = models.CharField(max_length=100)
    vet_mobile_number = models.CharField(max_length=15)
    signature = models.CharField(max_length=255)
    stamp = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name_of_animal} - {self.livestock_category} ({self.date_of_sampling})"



class LivestockIncident(models.Model):
    LIVESTOCK_CATEGORY_CHOICES = [
        ('cattle', 'Cattle'),
        ('sheep', 'Sheep'),
        ('goat', 'Goat'),
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('horse', 'Horse'),
        ('poultry', 'Poultry'),
    ]

    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    DISPOSAL_WAY_CHOICES = [
        ('burial', 'Burial'),
        ('cremation', 'Cremation'),
    ]

    
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidence_records', limit_choices_to={'is_farmer': True})
    livestock_category = models.CharField(max_length=10, choices=LIVESTOCK_CATEGORY_CHOICES)
    animal_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    age = models.PositiveIntegerField()
    case_history = models.TextField()
    number_of_sick_animals = models.PositiveIntegerField()
    morbidity_rate = models.CharField(blank=True,max_length=40)
    incidence_date = models.DateField()
    incidence_time = models.TimeField()
    cadaver_signs = models.TextField()
    open_for_pm = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    no_pm_reason = models.TextField(blank=True, null=True)
    path_condition = models.TextField()
    sample_sent = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    cause_notifiable = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    cause_zoonotic = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    precaution = models.TextField()
    disposal_way = models.CharField(max_length=10, choices=DISPOSAL_WAY_CHOICES)

    def __str__(self):
        return f"{self.animal_name} - {self.livestock_category} ({self.incidence_date})"


class Referral(models.Model):
	PROGNOSIS = [
		('Good', 'Good'),
		('Fair', 'Fair'),
	]
	REFERRAL_CHOICE=[
		('farmer','Farmer'),
		('vet','Vet')
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referral_records', limit_choices_to={'is_farmer': True})
	species = models.CharField(max_length=255)  
	treatment_duration = models.CharField(max_length=255)  
	previous_treatment_state = models.TextField()  
	prognosis = models.CharField(max_length=30,choices=PROGNOSIS)  
	referral_date = models.DateField()  
	referral_choice = models.CharField(max_length=25,choices=REFERRAL_CHOICE)  
	r_vet_name = models.CharField(max_length=255)  
	r_vet_contact = models.CharField(max_length=15)  
	farmer_name = models.CharField(max_length=255)
	village = models.CharField(max_length=255)
	contact = models.CharField(max_length=15) 
	vet_name = models.CharField(max_length=255)
	vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
	vet_reg_no = models.CharField(max_length=255)  
	vet_contact = models.CharField(max_length=15)  
	signature = models.TextField(blank=True,null=True)
	stamp = models.TextField(blank=True,null=True)
	comment = models.TextField(blank=True, null=True)  

	def __str__(self):
		return f"Referral for {self.species} by {self.vet_name} on {self.referral_date}"

class FarmConsultation(models.Model):
    DAIRY = 'Dairy'
    BEEF_PRODUCTION = 'Beef Production'
    POULTRY_PRODUCTION = 'Poultry Production'
    GOAT_PRODUCTION = 'Goat Production'
    PETS = 'Pets'
    OTHER = 'Other'

    AREA_OF_INTEREST_CHOICES = [
        (DAIRY, 'Dairy'),
        (BEEF_PRODUCTION, 'Beef Production'),
        (POULTRY_PRODUCTION, 'Poultry Production'),
        (GOAT_PRODUCTION, 'Goat Production'),
        (PETS, 'Pets'),
        (OTHER, 'Other'),
    ]
    FARM_MANAGER_CATEGORY=[
		('veterinary officer','Veterinary Officer'),
	('livestock officer','Livestock Officer'),
	('none','None')
	]
    

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultation_records', limit_choices_to={'is_farmer': True})
    visit_date=models.DateField()
    area_of_interest = models.CharField(max_length=20, choices=AREA_OF_INTEREST_CHOICES)
    other = models.CharField(max_length=255, blank=True, null=True) 
    recommendation = models.TextField(blank=True, null=True)  
    manager = models.CharField(max_length=30, choices=FARM_MANAGER_CATEGORY)   
    farmer_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)  
    village = models.CharField(max_length=255)
    vet_name = models.CharField(max_length=255)
    vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
    vet_reg_no = models.CharField(max_length=255) 
    vet_contact = models.CharField(max_length=15)  
    signature = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.farmer_name} - {self.area_of_interest} - {self.vet_name}"

class PregnancyDiagnosis(models.Model):
    ADULT = 'Adult'
    HEIFER = 'Heifer'
    CATEGORY_CHOICES = [
        (ADULT, 'Adult'),
        (HEIFER, 'Heifer'),
    ]

    POSITIVE = 'Positive'
    NEGATIVE = 'Negative'
    NOT_CONFIRMED = 'Not Confirmed'
    PD_RESULTS_CHOICES = [
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative'),
        (NOT_CONFIRMED, 'Not Confirmed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pregdiagnosis_records', limit_choices_to={'is_farmer': True})
    cow_name = models.CharField(max_length=255)
    reg_no = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    date_of_ai = models.DateField()  # Date of Artificial Insemination
    pg_diag_date = models.DateField()  # Pregnancy diagnosis date
    pd_results = models.CharField(max_length=15, choices=PD_RESULTS_CHOICES)
    pd_method = models.CharField(max_length=255)  # Method used for pregnancy diagnosis
    positive_pd_months = models.DecimalField(max_digits=5, decimal_places=2)  # Number of months if positive
    negative_pd_comment = models.TextField(blank=True, null=True)  # Comments if negative
    pd_nxt_date = models.DateField(blank=True, null=True)  # Next pregnancy diagnosis date
    expctd_delivery_date = models.DateField(blank=True, null=True)  # Expected delivery date
    comment = models.TextField(blank=True, null=True)  # Additional comments
    owners_name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    vet_name = models.CharField(max_length=255)
    vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
    vet_reg_no = models.CharField(max_length=255)  # Vet's registration number
    vet_contact = models.CharField(max_length=15)  # Adjust max_length as necessary
    signature = models.TextField(blank=True,null=True)
    #stamp = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.cow_name} - {self.reg_no} - {self.pd_results}"

class PostMortemRecord(models.Model):
    LIVESTOCK_CATEGORY_CHOICES = [
        ('cattle', 'Cattle'),
        ('sheep', 'Sheep'),
        ('goat', 'Goat'),
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('horse', 'Horse'),
        ('poultry', 'Poultry'),
        ('none', 'None'),
    ]

    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    DISPOSAL_CHOICES = [
        ('burial', 'Burial'),
        ('burning', 'Burning'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postmortem_records', limit_choices_to={'is_farmer': True})
    livestock_category = models.CharField(max_length=10, choices=LIVESTOCK_CATEGORY_CHOICES)
    other_livestock = models.CharField(max_length=100, blank=True, null=True)
    name_of_animal = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    age = models.CharField(max_length=100)
    case_history = models.TextField()
    number_of_sick_animals = models.IntegerField()
    number_of_dead = models.IntegerField()
    morbidity_rate = models.CharField(max_length=100)
    date_of_incidence = models.DateField()
    time_of_incidence = models.TimeField()
    signs_of_cadaver = models.TextField()
    cadaver_open_for_pm = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    reasons_for_not_opening = models.TextField(blank=True, null=True)
    major_pathological_conditions = models.TextField(blank=True, null=True)
    cause_of_death=models.CharField(max_length=100)
    sample_sent_to_lab = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    cause_of_death_notifiable = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    cause_of_death_zoonotic = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    precautions_if_zoonotic = models.TextField(blank=True, null=True)
    cadaver_disposed_by = models.CharField(max_length=7, choices=DISPOSAL_CHOICES)
    owner_name = models.CharField(max_length=100)
    owner_village = models.CharField(max_length=100)
    owner_mobile_number = models.CharField(max_length=15)
    vet_in_charge_name = models.CharField(max_length=100)
    vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
    vet_in_charge_registration_number = models.CharField(max_length=100)
    vet_in_charge_mobile_number = models.CharField(max_length=15)
    signature = models.TextField(blank=True,null=True)
    stamp = models.TextField(blank=True,null=True)


    def __str__(self):
        return f"Post Mortem Record - {self.name_of_animal} ({self.date_of_incidence})"

class VeterinaryBilling(models.Model):
    DEWORMING = 'Deworming'
    SURGERY = 'Surgery'
    AI = 'AI'
    CLINICAL = 'Clinical'
    VACCINATION = 'Vaccination'
    POST_MORTEM = 'Post Mortem'
    PREGNANCY_DIAGNOSIS = 'Pregnancy Diagnosis'
    LAB_CHARGES = 'Lab Charges'

    BILLING_CATEGORY_CHOICES = [
        (DEWORMING, 'Deworming'),
        (SURGERY, 'Surgery'),
        (AI, 'AI'),
        (CLINICAL, 'Clinical'),
        (VACCINATION, 'Vaccination'),
        (POST_MORTEM, 'Post Mortem'),
        (PREGNANCY_DIAGNOSIS, 'Pregnancy Diagnosis'),
        (LAB_CHARGES, 'Lab Charges'),
        ('Uterine Irrigation', 'Uterine Irrigation'),
  ('Emergency Care', 'Emergency Care'),
  ('Livestock Examination', 'Livestock Examination'),
   ('Farm Consultation', 'Farm Consultation'),
  ('None', 'None'),
        
    ]

    CASH = 'Cash'
    CHEQUE = 'Cheque'
    MOBILE_MONEY = 'Mobile Money'
    BANK_TRANSFER = 'Bank Transfer'
    OTHER = 'Other'

    MODE_OF_PAYMENT_CHOICES = [
        (CASH, 'Cash'),
        (CHEQUE, 'Cheque'),
        (MOBILE_MONEY, 'Mobile Money'),
        (BANK_TRANSFER, 'Bank Transfer'),
        (OTHER, 'Other'),
    ]
    
    PLAN_CHOICES=[
		('full payment','Full Payment'),
		('partial payment','Partial Payment'),
		
	]
    PAYMENT_STATUS_CHOICES=[
		('in arrears','In Arreas'),
		('paid','Paid'),
	]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vet_billing_records', limit_choices_to={'is_farmer': True})
    billing_category = models.CharField(max_length=100, choices=BILLING_CATEGORY_CHOICES)
    other_billing_category=models.CharField(max_length=50)
    total_amount_billed = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2) 
    mode_of_payment = models.CharField(max_length=20, choices=MODE_OF_PAYMENT_CHOICES)
    agreed_date = models.DateField() 
    payment_plan = models.CharField(max_length=50,choices=PLAN_CHOICES)  
    payment_status=models.CharField(max_length=50,choices=PAYMENT_STATUS_CHOICES)
    farmer_name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    vet_to_be_paid = models.CharField(max_length=255) 
    vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
    reg_no = models.CharField(max_length=255)  
    vet_contact = models.CharField(max_length=15)  
    signature = models.TextField(blank=True, null=True)
    

    def save(self, *args, **kwargs):
      
        self.balance = self.total_amount_billed - self.total_paid
        super(VeterinaryBilling, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.farmer_name} - {self.billing_category} - {self.agreed_date}"
    
class Deworming(models.Model):
	CATTLE = 'Cattle'
	SHEEP = 'Sheep'
	GOAT = 'Goat'
	DONKEY = 'Donkey'
	DOG = 'Dog'
	HORSE = 'Horse'
	POULTRY = 'Poultry'
	OTHER = 'Other'

	SPECIES_TARGETED_CHOICES = [
		(CATTLE, 'Cattle'),
		(SHEEP, 'Sheep'),
		(GOAT, 'Goat'),
		(DONKEY, 'Donkey'),
		(DOG, 'Dog'),
		(HORSE, 'Horse'),
		(POULTRY, 'Poultry'),
		(OTHER, 'Other'),
	]
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deworming_records', limit_choices_to={'is_farmer': True})
	species_targeted = models.CharField(max_length=10, choices=SPECIES_TARGETED_CHOICES)
	other = models.CharField(max_length=255, blank=True, null=True)
	animal_name=models.CharField(max_length=100)
	no_of_adults = models.IntegerField()
	no_of_young_ones = models.IntegerField()
	body_conditions = models.TextField()  # Description of the body condition of animals
	deworming_date = models.DateField()
	drug_of_choice = models.CharField(max_length=255)
	parasites = models.CharField(max_length=255)
	withdrawal_period = models.CharField(max_length=255)  # e.g., "7 days", "14 days"
	side_effects = models.TextField(blank=True, null=True)
	nxt_deworming_date = models.DateField()  # Next deworming date
	farmer_name = models.CharField(max_length=255)
	village = models.CharField(max_length=255)
	contact = models.CharField(max_length=15) 
	vet_name = models.CharField(max_length=255)
	vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
	reg_no = models.CharField(max_length=255)  # Vet registration number
	vet_contact = models.CharField(max_length=15)  # Adjust max_length as necessary
	signature = models.TextField(blank=True,null=True)
	#stamp = models.TextField(blank=True,null=True)

	def __str__(self):
		return f"{self.farmer_name} - {self.deworming_date}"    

FARMERS = tuple(farmers_list)

class ArtificialInsemination(models.Model):
	VET_CATEGORY=[
	('surgeon', 'Surgeon'),
	('technologist', 'Technologist'),
	('technician', 'Technician')
	]

	SERVED_BY_CHOICES = [
	('AI', 'AI'),
	('BULL', 'Bull'),
	]
	ABORTION_STATUS_CHOICES = [
	('YES', 'Yes'),
	('NO', 'No'),
	]
	INSEMINATION_STATUS_CHOICES=[
		('First','First'),
		('Repeat','Repeat'),
	]
	SEMEN_TYPE=[
		('Conventional','Conventional'),
		('Sexed','Sexed'),
	]
	CATTLE = 'Cattle'
	SHEEP = 'Sheep'
	GOAT = 'Goat'
	DONKEY = 'Donkey'
	DOG = 'Dog'
	HORSE = 'Horse'
	POULTRY = 'Poultry'
	OTHER = 'Other'

	ANIMAL_SPECIES = [
		(CATTLE, 'Cattle'),
		(SHEEP, 'Sheep'),
		(GOAT, 'Goat'),
		(DONKEY, 'Donkey'),
		(DOG, 'Dog'),
		(HORSE, 'Horse'),
		(POULTRY, 'Poultry'),
		(OTHER, 'Other'),
	]
	RAB=[
		('Manual Removal', 'Manual Removal'),
		('Natural Expulsion', 'Natural Expulsion'),
		('None', 'None'),
	]
	COW_BREEDS = [
    ('Holstein', 'Holstein'),
    ('Jersey', 'Jersey'),
    ('Angus', 'Angus'),
    ('Hereford', 'Hereford'),
    ('Simmental', 'Simmental'),
    ('Brahman', 'Brahman'),
    ('Charolais', 'Charolais'),
    ('Limousin', 'Limousin'),
    ('Guernsey', 'Guernsey'),
    ('Ayrshire', 'Ayrshire'),
    ('Brown Swiss', 'Brown Swiss'),
    ('Shorthorn', 'Shorthorn'),
    ('Other', 'Other'),
]
 
	SEMEN_SOURCE=[
		('KAGRC','KAGRC'),
	('ADC','ADC'),
 ('CRV','CRV'),
 ('WW Sires','WW Sires'),
 ('Semex Alliance','Semex Alliance'),
 ('Alta Genetic','Alta Genetic'),
 ('CRI','CRI'),
 ('Other','Other')
	]
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='ai_assign',
		limit_choices_to={'is_farmer': True},
		null=True,                 
		blank=True,
		editable=True,
	                 
	)
	assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='ai_official',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,
		editable=True,               
		                 
	)
	assigned_to_cooperative = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='ai_cooperative',
		limit_choices_to={'is_cooperative': True},
		null=True,                 
		blank=True,
		editable=True,               
		                 
	)
	assigned_by = models.ForeignKey(  
		User,
		on_delete=models.CASCADE,
		related_name="assigned_ai",
		null=True,
		blank=True
	)
	farm_name = models.CharField(max_length=255,default="")
	species=models.CharField(max_length=10,choices=ANIMAL_SPECIES,default="")
	cow_name = models.CharField(max_length=255,default="")
	reg_no = models.CharField(max_length=255,default="")
	animal_status=models.CharField(max_length=20,default="")
	dam_details = models.TextField(default="")
	sire_details = models.TextField(default="")
	no_of_repeats = models.IntegerField(default="")
	rab_status = models.CharField(max_length=20, choices=RAB, null=True, blank=True)
	abortion_status = models.CharField(max_length=3, choices=ABORTION_STATUS_CHOICES,default="")
	time_of_heat_sign = models.TimeField()
	date_of_heat_sign = models.DateField()
	insemination_date=models.DateField()
	insemination_time = models.TimeField()
	insemination_status=models.CharField(max_length=20,choices=INSEMINATION_STATUS_CHOICES,default="")
	semen_type=models.CharField(max_length=20 ,choices=SEMEN_TYPE,default="")
	breed_used = models.CharField(max_length=25,choices=COW_BREEDS,default="")
	other_breed=models.CharField(max_length=255, null=True, blank=True)
	bull_name = models.CharField(max_length=255,default="")
	bull_reg_no = models.CharField(max_length=255,default="")
	semen_source = models.CharField(max_length=25,choices=SEMEN_SOURCE,default="")
	other_source = models.CharField(max_length=255,default="")
	heat_sign_mtr_date = models.DateField()  
	repeat_heat_date = models.DateField()
	first_pd_date = models.DateField()  
	expected_delivery_date = models.DateField()
	owners_name = models.CharField(max_length=255,default="")
	sub_county = models.CharField(max_length=25,default="")
	ward = models.CharField(max_length=25,default="")
	village = models.CharField(max_length=255,default="")
	contact = models.CharField(max_length=15,default="") 
	vet_name = models.CharField(max_length=255,default="",blank=True,null=True)
	vet_category=models.CharField(max_length=30,choices=VET_CATEGORY,default="")
	vet_reg_no = models.CharField(max_length=254,default="",blank=True,null=True)
	vet_contact = models.CharField(max_length=15,default="",blank=True,null=True)  
	signature_stamp = models.TextField(blank=True,null=True)


	def __str__(self):
		return f"{self.cow_name} - {self.reg_no}"
	def save(self, *args, **kwargs):
		if not self.pk and 'request' in kwargs:  # Ensure it's a new instance
			self.assigned_by = kwargs.pop('request').user

		if self.insemination_date:
			self.first_pd_date = self.insemination_date + timedelta(days=90)
			self.heat_sign_mtr_date = self.insemination_date + timedelta(days=15)
			self.expected_delivery_date = self.insemination_date + timedelta(days=9 * 30)
			self.repeat_heat_date = self.insemination_date + timedelta(days=21)

		super().save(*args, **kwargs)
	
class Calf(models.Model):
	
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	name_given = models.CharField(max_length=100, default='')
	registration_number = models.CharField(max_length=100, unique=True, default='')
	dam_details=models.CharField(max_length=100, default='')
	birth_date = models.DateField()
	breed = models.CharField(max_length=100, default='')
	gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], default='')
	sire_details = models.CharField(max_length=100, default='')
	color = models.CharField(max_length=100, default='')
	birth_weight = models.FloatField()
	medical_conditions = models.CharField(max_length=100, blank=True, default='')
	registration_date = models.DateField(null=True, blank=True)
	expected_weaning = models.DateField(null=True, blank=True)
	breeding_level = models.CharField(max_length=100, default="Purebreed", choices=BREEDING_LEVEL_CHOICES)
	comments = models.CharField(max_length=100, blank=True, default='')

	def __str__(self):
		return self.name +'-'+ str(self.id)

class DeadAnimal(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	name = models.CharField(max_length=30, default='')
	farm_name = models.CharField(max_length=100, default='')
	no_of_affected = models.FloatField(default=0)
	gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], default='')
	breed = models.CharField(max_length=100, default='')
	sickness_period = models.CharField(max_length=30, default='')
	cause_of_death = models.CharField(max_length=30, default='')
	death_date = models.DateField(null=True, blank=True)
	death_time = models.TimeField(null=True, blank=True)
	signs_before_death = models.CharField(max_length=200, null=True, blank=True, default='')
	postmortem_by_vet = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='')
	safety_precaution = models.CharField(max_length=30, choices=[('Burying', 'Burying'), ('Cremation', 'Cremation')], default='')
	comment = models.CharField(max_length=300, null=True, blank=True, verbose_name='comment', default='')

	def __str__(self):
		return self.name +'-'+ str(self.id)

class Culling(models.Model):
	CULLING_REASONS = [
		('Disease', 'Disease'),
		('Old age', 'Old age'),
		('Poor performance', 'Poor performance'),
		('Genetic defects', 'Genetic defects'),
		('Other', 'Other'),
	]
	CULLING_METHOD = [
		('Killing', 'Killing'),
		('Selling', 'Selling'),
	]

	ANIMAL_TYPE=[
		('Cow','Cow'),
		('Sheep','Sheep'),
		('Goat','Goat')
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	name = models.CharField(max_length=100, default='')
	reg_no = models.CharField(max_length=100, unique=True, default='')
	age = models.CharField(max_length=100, default='')
	gender = models.CharField(max_length=100, default='')
	animal_type=models.CharField(max_length=100, choices=ANIMAL_TYPE, default='')
	breed = models.CharField(max_length=100, default='')
	culling_method = models.CharField(max_length=100, choices=CULLING_METHOD, default='')
	no_of_culled = models.FloatField(default=0)
	culling_reason = models.CharField(max_length=100, choices=CULLING_REASONS, default='')
	culling_date = models.DateField()
	culling_price = models.DecimalField(max_digits=10, decimal_places=2)
	comment = models.TextField(blank=True, null=True, default='')

	def __str__(self):
		return self.name +'-'+ str(self.id)

class Livestock(models.Model):
	ANIMAL_TYPES = [
		('Cow', 'Cow'),
		('Goat', 'Goat'),
		('Sheep', 'Sheep'),
		('Pig', 'Pig'),
		('Chicken', 'Chicken'),
		# Add more types as needed
	]
	BREED_CHOICES = [
		('Dog', [
			('Labrador Retriever', 'Labrador Retriever'),
			('German Shepherd', 'German Shepherd'),
			('Golden Retriever', 'Golden Retriever'),
			('Bulldog', 'Bulldog'),
			('Beagle', 'Beagle'),
			('Poodle', 'Poodle'),
			('Boxer', 'Boxer'),
			('Dachshund', 'Dachshund'),
			('Yorkshire Terrier', 'Yorkshire Terrier'),
			('Rottweiler', 'Rottweiler'),
		]),
		('Cat', [
			('Siamese', 'Siamese'),
			('Persian', 'Persian'),
			('Maine Coon', 'Maine Coon'),
			('Ragdoll', 'Ragdoll'),
			('British Shorthair', 'British Shorthair'),
			('Sphynx', 'Sphynx'),
			('Bengal', 'Bengal'),
			('Abyssinian', 'Abyssinian'),
			('Scottish Fold', 'Scottish Fold'),
			('Burmese', 'Burmese'),
		]),
		('Horse', [
			('Thoroughbred', 'Thoroughbred'),
			('Quarter Horse', 'Quarter Horse'),
			('Arabian', 'Arabian'),
			('Appaloosa', 'Appaloosa'),
			('Paint Horse', 'Paint Horse'),
			('Morgan', 'Morgan'),
			('Tennessee Walking Horse', 'Tennessee Walking Horse'),
			('Friesian', 'Friesian'),
			('Pony of the Americas', 'Pony of the Americas'),
			('Miniature Horse', 'Miniature Horse'),
		]),
		('Cattle', [
			('Angus', 'Angus'),
			('Hereford', 'Hereford'),
			('Charolais', 'Charolais'),
			('Simmental', 'Simmental'),
			('Limousin', 'Limousin'),
			('Texas Longhorn', 'Texas Longhorn'),
			('Holstein', 'Holstein'),
			('Jersey', 'Jersey'),
			('Gelbvieh', 'Gelbvieh'),
			('Brahman', 'Brahman'),
		]),
		('Sheep', [
			('Merino', 'Merino'),
			('Dorper', 'Dorper'),
			('Suffolk', 'Suffolk'),
			('Rambouillet', 'Rambouillet'),
			('Hampshire', 'Hampshire'),
			('Shropshire', 'Shropshire'),
			('Dorset', 'Dorset'),
			('Cotswold', 'Cotswold'),
			('Lincoln', 'Lincoln'),
			('Targhee', 'Targhee'),
		]),
		('Goat', [
			('Boer', 'Boer'),
			('Nubian', 'Nubian'),
			('Saanen', 'Saanen'),
			('Angora', 'Angora'),
			('LaMancha', 'LaMancha'),
			('Alpine', 'Alpine'),
			('Toggenburg', 'Toggenburg'),
			('Kiko', 'Kiko'),
			('Spanish', 'Spanish'),
			('Pygmy', 'Pygmy'),
		]),
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	animal_type = models.CharField(max_length=50, choices=ANIMAL_TYPES, default='')
	breed_category = models.CharField(max_length=50, choices=BREED_CHOICES, default='')
	date_added = models.DateField()
	no_of_animals = models.FloatField(default=0)
	no_of_males = models.FloatField(default=0)
	no_of_females = models.FloatField(default=0)
	no_of_adults = models.FloatField(default=0)
	no_of_young = models.FloatField(default=0)
	no_of_dead = models.FloatField(default=0)
	reason_for_death = models.CharField(max_length=100, default='')
	comment = models.TextField(blank=True, null=True, default='')

	def __str__(self):
		return self.name + ' - ' + str(self.id)

class NewAnimal(models.Model):
	SOURCE_CHOICES = [
		('Market', 'Market'),
		('Farmer', 'Farmer'),
	]

	BREEDING_LEVEL_CHOICES = [
		('Purebred', 'Purebred'),
		('Crossbred', 'Crossbred'),
		('Mixed Breed', 'Mixed Breed'),
	]
    
	DEFECT_CHOICES = [
		('Yes', 'Yes'),
		('No', 'No'),
	]

	MEDICAL_HISTORY_CHOICES = [
		('Yes', 'Yes'),
		('No', 'No'),
	]

	ASSESSED_BY_VET_CHOICES = [
		('Yes', 'Yes'),
		('No', 'No'),
	]

	INSURED_CHOICES = [
		('Yes', 'Yes'),
		('No', 'No'),
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	name = models.CharField(max_length=100, default='')
	reg_no = models.CharField(max_length=100, default='')
	source = models.CharField(max_length=50, choices=SOURCE_CHOICES, default='')
	farmer_name = models.CharField(max_length=100, default='')
	animal_type = models.CharField(max_length=100, default='')
	breed = models.CharField(max_length=100, default='')
	breeding_level = models.CharField(max_length=100, choices=BREEDING_LEVEL_CHOICES, default='')
	defect = models.CharField(max_length=3, choices=DEFECT_CHOICES, default='')
	defect_reason = models.TextField(default='')
	animal_color = models.CharField(max_length=100, default='')
	market_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	medical_history = models.CharField(max_length=3, choices=MEDICAL_HISTORY_CHOICES, default='')
	assessed_by_vet = models.CharField(max_length=3, choices=ASSESSED_BY_VET_CHOICES, default='')
	insured = models.CharField(max_length=3, choices=INSURED_CHOICES, default='')
	insuring_company = models.CharField(max_length=100, default='')
	date_added = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.name + '-' + str(self.id)


class AnimalSale(models.Model):
		BREED_CHOICES = [
		('Cattle', 'Cattle'),
		('Sheep', 'Sheep'),
		('Goat', 'Goat'),
		('Poultry', 'Poultry'),
		('Other', 'Other'),
		]
		AGE=[
		('Adult', 'Adult'),
		('Young One', 'Young One'),	
		]
		user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
		number_sold = models.IntegerField()
		name = models.CharField(max_length=100)
		reg_no = models.CharField(max_length=100)
		date_sold=models.DateField()
		breed = models.CharField(max_length=100,choices=BREED_CHOICES, default='')
		age = models.CharField(max_length=100,choices=AGE, default='')
		sex = models.CharField(max_length=10,choices=SEX_CHOICES)
		weight = models.DecimalField(max_digits=10, decimal_places=2)
		selling_price = models.DecimalField(max_digits=10, decimal_places=2)
		reason = models.TextField()
		comment = models.TextField()

		def __str__(self):
			return self.name + ' - ' + str(self.id)

class HeatSignMonitoring(models.Model):
    STATUS_CHOICES = [
        ('Adult', 'Adult'),
        ('Heifer', 'Heifer'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_of_heat_sign = models.DateField()
    date_of_repeat_monitoring = models.DateField(blank=True, null=True)
    exp_date_of_repeated_heat = models.DateField(blank=True, null=True)
    reason_skip_monitoring = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.date_of_heat_sign:
            # Always calculate based on date_of_heat_sign
            self.date_of_repeat_monitoring = self.date_of_heat_sign + timedelta(days=15)
            self.exp_date_of_repeated_heat = self.date_of_heat_sign + timedelta(days=21)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + ' - ' + str(self.id)


class PregnancyMonitoring(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	name = models.CharField(max_length=100)
	reg_no = models.CharField(max_length=50)
	date_of_ai = models.DateField()
	exp_heat_date = models.DateField(null=True, blank=True)
	repeat_heat_date=models.DateField(null=True,blank=True)
	first_preg_diag_date = models.DateField(null=True, blank=True)
	# PD_STATUS_CHOICES = (
	#     ('positive', 'Positive'),
	#     ('negative', 'Negative'),
	# )
	#pd_status = models.CharField(max_length=20, choices=PD_STATUS_CHOICES)
	#approximate_preg_months = models.IntegerField()
	#vet_recommendation = models.TextField()
	#date_of_second_diag = models.DateField(null=True, blank=True)
	# FOETUS_STATUS_CHOICES = (
	#     ('progressive', 'Progressive'),
	#     ('non-progressive', 'Non-Progressive'),
	# )
	#foetus_status = models.CharField(max_length=20, choices=FOETUS_STATUS_CHOICES)
	#non_prog_reason = models.CharField(max_length=255, null=True, blank=True, default="")
	#action_to_take = models.CharField(max_length=255, null=True, blank=True, default="")
	steaming_up_date = models.DateField(null=True, blank=True)
	expected_dob = models.DateField(null=True, blank=True)
	#actual_date_of_delivery = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.name + ' - ' + str(self.id)

	def save(self, *args, **kwargs):
		if self.date_of_ai:
			
			self.first_preg_diag_date = self.date_of_ai + timedelta(days=90)
			self.steaming_up_date = self.date_of_ai + timedelta(days=7 * 30)
			self.expected_dob = self.date_of_ai + timedelta(days=9 * 30)
			self.exp_heat_date = self.date_of_ai + timedelta(days=21)
			self.repeat_heat_date = self.date_of_ai + timedelta(days=15)
		super().save(*args, **kwargs)

class GestationMonitoring(models.Model):
    gestation_date = models.DateField()
    repeat_date = models.DateField(blank=True, null=True)
    expected_delivery_date = models.DateField(blank=True, null=True)


class Feeds(models.Model):
		FEED_TYPE_CHOICES = [
			('Dairy Meal', 'Dairy Meal'),
			('Wheat Bran', 'Wheat Bran'),
			('Maize Chaff', 'Maize Chaff'),
			('Sunflower', 'Sunflower'),
		]
		user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
		date_of_purchase = models.DateField('Date of Purchase')
		feed_type = models.CharField('Feed Type', max_length=15, choices=FEED_TYPE_CHOICES)
		company = models.CharField('Company', max_length=255)
		expiry_date = models.DateField('Expiry Date')
		quantity_purchased= models.CharField('Quantity purchased', max_length=255)
		trade_name= models.CharField('Trade Name', max_length=255)
		weight=models.CharField('Weight', max_length=255)
		cost = models.DecimalField('Cost', max_digits=10, decimal_places=2)
		comment = models.TextField('Comment', blank=True)

		def __str__(self):
			return self.date_of_purchase + ' - ' + str(self.id)
class Minerals(models.Model):
		MINERAL_TYPE_CHOICES = [
			('Dairy Lick', 'Dairy Lick'),
			('Stock Lick', 'Stock Lick'),
			('Dry Cow', 'Dry Cow'),
			('Joto', 'Joto'),
			('Calves Mineral', 'Calves Mineral')
		]
		user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
		date_of_purchase = models.DateField('Date of Purchase')
		mineral_type = models.CharField('Feed Type', max_length=15, choices=MINERAL_TYPE_CHOICES)
		quantity=models.CharField('Company', max_length=255)
		company = models.CharField('Company', max_length=255)
		expiry_date = models.DateField('Expiry Date')
		cost = models.DecimalField('Cost', max_digits=10, decimal_places=2)
		comment = models.TextField('Comment', blank=True)

		def __str__(self):
			return self.date_of_purchase + ' - ' + str(self.id)
		
class VeterinaryBills(models.Model):
		user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
		date_of_billing = models.DateField('Date of Billing')
		bill_category = models.CharField('Bill Category', max_length=20)
		amount = models.DecimalField('Amount', max_digits=10, decimal_places=2)
		amount_billed = models.DecimalField('Amount', max_digits=10, decimal_places=2)
		balance = models.DecimalField('Balance', max_digits=10, decimal_places=2)
		billing_details=models.CharField('Company', max_length=255)
		comment = models.TextField('Comment', blank=True)

		def save(self, *args, **kwargs):
		# Calculate the balance before saving
			self.balance = self.amount_billed - self.amount
			super(VeterinaryBills, self).save(*args, **kwargs)

		def __str__(self):
				return f"{self.amount_billed} - {self.id}"
class OtherExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date = models.DateField()
    description = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.description} - {self.cost}"
	
class Archaricides(models.Model):
		user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
		date_of_purchase = models.DateField('Date of Purchase')
		chemical_name = models.CharField('Chemical Name', max_length=50)
		trade_name = models.CharField('Chemical Name', max_length=50)
		quantity=models.CharField('Quantity', max_length=255)
		company = models.CharField('Company', max_length=255)
		application_rate = models.CharField('Rate', max_length=255)
		expiry_date = models.DateField('Expiry Date')
		times_used=models.CharField('Frequency', max_length=255)
		cost = models.DecimalField('Cost', max_digits=10, decimal_places=2)
		comment = models.TextField('Comment', blank=True)

		def __str__(self):
			return self.date_of_purchase + ' - ' + str(self.id)
		
class DairyEquipment(models.Model):
		user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
		name=models.CharField('Name', max_length=40)
		date_of_purchase = models.DateField('Date of Purchase')
		quantity=models.CharField('quantity', max_length=255)
		equipment_type = models.CharField('Type', max_length=255)
		model_number=models.CharField('Model Number', max_length=255)
		company = models.CharField('Company', max_length=255)
		cost = models.DecimalField('Cost', max_digits=10, decimal_places=2)
		source=models.CharField('Source', max_length=255)
		comment = models.TextField('Comment', blank=True)

		def __str__(self):
			return self.date_of_purchase + ' - ' + str(self.id)

class DairyHygiene(models.Model):
		user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
		chemical_name=models.CharField('Chemical Name', max_length=255)
		trade_name=models.CharField('Trade Name', max_length=255)
		date_of_purchase = models.DateField('Date of Purchase')
		item_purchased = models.CharField('Item', max_length=255)
		company = models.CharField('Company', max_length=255)
		quantity=models.CharField('quantity', max_length=255)
		cost = models.DecimalField('Cost', max_digits=10, decimal_places=2)
		expiry_date = models.DateField('Expiry Date')
		comment = models.TextField('Comment', blank=True)

		def __str__(self):
			return self.chemical_name + ' - ' + str(self.id)
		

	
class LivestockInsurance(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	number_insured=models.DecimalField('Number Insured', max_digits=10, decimal_places=2)
	breed = models.CharField(max_length=50)
	animal_species=models.CharField(max_length=50)
	company=models.CharField('Company', max_length=255)
	mode_of_payment=models.CharField('Mode Of payment', max_length=255)
	payment_date= models.DateField('Payment Date')
	total=models.DecimalField('Total', max_digits=10, decimal_places=2)
	comment=models.TextField('Comment', blank=True)

	def __str__(self):
			return self.company + ' - ' + str(self.id)
	
class VeterinaryDrugs(models.Model):
	DRUG_TYPE_CHOICES = [
			('Antibiotics', 'Antibiotics '),
			('Vaccines', 'Vaccines'),
			('Hormones', 'Hormones'),
			('Metabolics', 'Metabolics'),
			
		]
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	date_of_purchase=models.DateField('Date of purchase',max_length=40)
	name=models.CharField('Name', max_length=255)
	category=models.CharField('Category', max_length=15,choices=DRUG_TYPE_CHOICES)
	company=models.CharField('company', max_length=50)
	expiry_date=models.DateField('Expiry Date')
	strange_condition=models.CharField('Strange Condition', max_length=255)
	vet_reg=models.CharField('Vet Registration', max_length=255)
	cost=models.DecimalField('Number Insured', max_digits=10, decimal_places=2)
	comment=models.TextField('Comment', blank=True)

	def __str__(self):
			return self.name + ' - ' + str(self.id)
	
class Employees(models.Model):
	EMPLOYMENT_MODES = [
	('Full-Time', 'Full-Time'),
	('Part-Time', 'Part-Time'),
	('Contract', 'Contract'),
	('Internship', 'Internship'),
	]
	POSITION_CHOICES = [
        ('Milker', 'Milker'),
        ('Cleaner', 'Cleaner'),
        ('Animal caretaker', 'Animal caretaker'),
        ('Driver', 'Driver'),
        ('Veterinary officer', 'Veterinary officer'),
        ('Manager', 'Manager')
    ]
    

	PAYMENT_METHODS = [
	('Bank Transfer', 'Bank Transfer'),
	('Cash', 'Cash'),
	('Cheque', 'Cheque'),
	('Mobile Banking', 'Mobile Banking'),
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	enrollment_date=models.DateField()
	employee_name = models.CharField(max_length=100)
	id_no = models.CharField(max_length=20, unique=True)
	phone_no = models.CharField(max_length=15)
	county = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	village = models.CharField(max_length=50)
	next_of_kin = models.CharField(max_length=100)
	next_of_kin_phone_no = models.CharField(max_length=15)
	chief_name = models.CharField(max_length=50)
	chief_phone_no = models.CharField(max_length=15)
	employee_position = models.CharField(max_length=50, choices=POSITION_CHOICES)
	salary = models.DecimalField(max_digits=10, decimal_places=2)
	payment_method = models.CharField(max_length=30, choices=PAYMENT_METHODS)
	bank_account = models.CharField(max_length=30, blank=True, null=True)
	mode_of_employment = models.CharField(max_length=20, choices=EMPLOYMENT_MODES)
	contract_rewal_period = models.IntegerField(help_text='Contract renewal period in months')

	def __str__(self):
		return self.employee_name
	

class Salaries(models.Model):
	PAYMENT_TYPE = [
		('Salary', 'Salary'),
		('Advance', 'Advance'),
		('Emergency', 'Emergency'),
		('Other', 'Other'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	employee_name = models.ForeignKey(Employees, related_name='salaries_by_name', on_delete=models.CASCADE)
	employee_position = models.CharField(max_length=50, choices=Employees.POSITION_CHOICES)
	identification = models.CharField('identification', unique=True, max_length=255)
	mode_of_payment = models.CharField('Mode', max_length=255, choices=Employees.PAYMENT_METHODS)
	bank_account = models.CharField('Bank Account', max_length=255) 
	salary_amount = models.DecimalField('Amount', max_digits=10, decimal_places=2) # Change to CharField to store account number
	amount = models.DecimalField('Amount', max_digits=10, decimal_places=2)
	balance = models.DecimalField('Balance', max_digits=10, decimal_places=2)
	payment_date = models.DateField('Payment Date')
	payment_type = models.CharField('Type', max_length=255, choices=PAYMENT_TYPE)
	comment = models.TextField('Comment', blank=True)

	def __str__(self):
		return f"{self.employee_name} - {self.employee_position}"

	def save(self, *args, **kwargs):
		if self.employee_name_id:
			employee = Employees.objects.get(pk=self.employee_name_id)
			self.bank_account = employee.bank_account 

		self.balance=self.salary_amount - self.amount
		
		super().save(*args, **kwargs)	

class LactatingCow(models.Model):
	LACTATION_STAGE_CHOICES = [
		('early', 'Early'),
		('mid', 'Mid'),
		('late', 'Late'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	cow_name = models.CharField(max_length=100,unique=True)
	reg_no = models.CharField(max_length=50)
	sire_details = models.CharField(max_length=100)
	breed = models.CharField(max_length=50)
	breeding_level = models.CharField(max_length=50,choices=BREEDING_LEVEL_CHOICES)
	age = models.PositiveIntegerField(help_text="Age in years")
	calving_down_date = models.DateField()
	no_of_calves = models.PositiveIntegerField()
	average_daily_milk = models.FloatField(help_text="Average daily milk production in liters")
	lactation_stage = models.CharField(max_length=10, choices=LACTATION_STAGE_CHOICES)
	expected_date_of_drying_off = models.DateField()

	def __str__(self):
		return f"{self.cow_name} ({self.reg_no})"

class MilkRecord(models.Model):
	TIME_OF_MILKING_CHOICES = [
	('Morning', 'Morning'),
	('Noon', 'Noon'),
	('Evening', 'Evening'),
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	cow_name = models.ForeignKey(LactatingCow, on_delete=models.CASCADE,default=1)
	employee_name = models.ForeignKey(Employees, on_delete=models.CASCADE,default=2)
	date = models.DateField()
	time_of_milking = models.CharField(max_length=10, choices=TIME_OF_MILKING_CHOICES)
	quantity = models.FloatField(help_text="Amount of milk in liters")

	def __str__(self):
		return f"{self.date} - {self.cow_name} - {self.time_of_milking}"
	
	
class DailyMilkRecord(models.Model):
    cow_name = models.ForeignKey(LactatingCow, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    total_quantity = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)  
	

    def __str__(self):
        return f"{self.cow_name} - {self.date} {self.time}"

class WeeklyMilkRecord(models.Model):
	
	cow_name = models.ForeignKey(LactatingCow, on_delete=models.CASCADE)
	week_start_date = models.DateField()
	total_quantity = models.FloatField(help_text="Total milk in liters for the week")
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
	

	def __str__(self):
		return f"Week starting {self.week_start_date} - {self.cow_name}"

class MonthlyMilkRecord(models.Model):
	
	cow_name = models.ForeignKey(LactatingCow, on_delete=models.CASCADE)
	month = models.DateField()
	total_quantity = models.FloatField(help_text="Total milk in liters for the month")
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

	class Meta:
		unique_together = ('cow_name', 'month')

	def __str__(self):
		return f"Month of {self.month.strftime('%B %Y')} - {self.cow_name}"
	
class DailyCheck(models.Model):
    CHECKED_BY_CHOICES = [
        ('manager', 'Manager'),
        ('assistant manager', 'Assistant Manager'),
        ('owner', 'Owner'),
        ('consultant', 'Farm Consultant'),
    ]

    SECTION_CHOICES = [
        ('healthy status', 'Healthy Status'),
        ('feeds and feeding', 'Feeds and Feeding'),
        ('heat signs', 'Heat Signs'),
        ('steaming up', 'Steaming Up'),
        ('biosecurity system', 'Biosecurity System'),
        ('milk hygiene', 'Milk Hygiene'),
        ('calves section', 'Calves Section'),
        ('dairy equipment', 'Dairy Equipment'),
        ('farm records', 'Farm Records'),
        ('pregnant cows', 'Pregnant Cows'),
    ]

    # STATUS_CHOICES = [
    #     ('yes', 'Yes'),
    #     ('no', 'No'),
    # ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date_of_check = models.DateField()
    time_of_check = models.TimeField()
    check_section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    #section_status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    remarks = models.TextField(blank=True)
    checked_by = models.CharField(max_length=20, choices=CHECKED_BY_CHOICES)
    contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.get_check_section_display()} - {self.get_section_status_display()} on {self.date_of_check}"

class Buyer(models.Model):
    PAYMENT_MODES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('biweekly', 'Every Two Weeks'),
        ('monthly', 'Monthly'),
        ('other', 'Other'),
    ]
    BUYER_CATEGORIES = [
        ('Neighbour', 'Neighbour'),
        ('Hotel', 'Hotel'),
        ('Cooperative', 'Cooperative'),
         ('Institution', 'Institution'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=BUYER_CATEGORIES)
    contact = models.CharField(max_length=50)
    date_of_enrollment = models.DateField()
    duration_of_supply = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODES)
    agreed_price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.category})"
class Payments(models.Model):
    PAYMENT_METHODS = [
        ('Cash', 'Cash'),
        ('Mobile Money', 'Mobile Money'),
        ('Cheque', 'Cheque'),
    ]

    CATEGORIES = [
        ('Neighbour', 'Neighbour'),
        ('Hotel', 'Hotel'),
        ('Cooperative', 'Cooperative'),
        ('Institution', 'Institution'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=20, choices=CATEGORIES) 
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)# new field
    date_of_payment = models.DateField()
    total_kg_supplied = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_to_receive = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    previous_balance = models.DecimalField(max_digits=12, decimal_places=2)
    grand_total = models.DecimalField(max_digits=12, decimal_places=2)
    amount_received = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    payment_received_by = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    contracts = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.total_kg_supplied and self.price_per_kg:
            self.total_amount_to_receive = self.total_kg_supplied * self.price_per_kg
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.buyer.name} - {self.date_of_payment}"


class SalesOfMilk(models.Model):
    MILK_SALES_TO = [
        ('Neighbour', 'Neighbour'),
        ('Hotel', 'Hotel'),
        ('Cooperative', 'Cooperative'),
        ('Institution', 'Institution'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date_of_sales = models.DateField()
    milk_sales_to = models.CharField(max_length=12, choices=MILK_SALES_TO)
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True)
    balance = models.CharField(max_length=12 ,blank=True, null=True)
    total_cash_received = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Sales on {self.date_of_sales} to {self.milk_sales_to}"

class ClinicalRecord(models.Model):
	ANIMAL_SPECIES_CHOICES = [
		('Cattle', 'Cattle'),
		('Sheep', 'Sheep'),
		('Goat', 'Goat'),
		('Donkey', 'Donkey'),
		('Dog', 'Dog'),
		('Cat', 'Cat'),
		('Horse', 'Horse'),
		('Poultry', 'Poultry'),
		('Other', 'Other'),
	]

	DISEASE_NATURE_CHOICES = [
		('Acute', 'Acute'),
		('Sub-acute', 'Sub-acute'),
		('Chronic', 'Chronic'),
	]

	YES_NO_CHOICES = [
		('Yes', 'Yes'),
		('No', 'No'),
	]
	PROGNOSIS=[
		('good','Good'),
		('poor','Poor'),
		('fair','Fair'),
		('grave','Grave'),
	]

	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clinical_records', limit_choices_to={'is_farmer': True})
	animal_species_affected = models.CharField(max_length=20, choices=ANIMAL_SPECIES_CHOICES)
	other_species = models.CharField(max_length=100, blank=True, null=True)
	#number_of_animals_sick = models.PositiveIntegerField()
	name_of_animal_affected = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=100)
	age_of_animal = models.CharField(max_length=20)
	breed_of_animal = models.CharField(max_length=100)
	nature_of_disease = models.CharField(max_length=20, choices=DISEASE_NATURE_CHOICES)
	case_history = models.TextField()
	refer_case_to_other_vet = models.CharField(max_length=3, choices=YES_NO_CHOICES)
	clinical_signs = models.TextField()
	prognosis = models.CharField(max_length=20,choices=PROGNOSIS)
	differential_diagnosis = models.TextField()
	final_diagnosis = models.TextField()
	treatment_plan = models.TextField()
	drugs_of_choice = models.TextField()
	date_of_start_dose = models.DateField()
	final_treatment_date = models.DateField(blank=True, null=True)
	is_zoonotic = models.CharField(max_length=3, choices=YES_NO_CHOICES)
	precautions = models.TextField(blank=True, null=True)
	is_disease_notifiable = models.CharField(max_length=3, choices=YES_NO_CHOICES)
	notified_authority = models.CharField(max_length=3, choices=YES_NO_CHOICES)
	comment = models.TextField(blank=True, null=True)
	owner_name = models.CharField(max_length=100)
	owner_village = models.CharField(max_length=100)
	owner_contact = models.CharField(max_length=15)
	vet_in_charge_name = models.CharField(max_length=100)
	vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
	vet_registration_number = models.CharField(max_length=100)
	vet_contact = models.CharField(max_length=15)
	vet_signature = models.TextField(blank=True,null=True)
	#rubber_stamp = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return f"{self.farmer_username} - {self.name_of_animal_affected}"

class Client(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date_of_enrollment = models.DateField()
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    livestock_interest = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
    
    
    
class Diary(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date = models.DateField()
    time_of_event=models.TimeField()
    main_activity = models.CharField(max_length=255)
    client_contact = models.CharField(max_length=15)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Diary Entry on {self.date} - {self.main_activity}"


class DiseaseReport(models.Model):
	LIVESTOCK_CATEGORY_CHOICES = [
		('Cattle', 'Cattle'),
		('Sheep', 'Sheep'),
		('Goat', 'Goat'),
		('Donkey', 'Donkey'),
		('Dog', 'Dog'),
		('Cat', 'Cat'),
		('Poultry', 'Poultry'),
		('None', 'None'),
	]

	SEX_CHOICES = [
		('female', 'Female'),
		('male', 'Male'),
		('both', 'Both Female and Male'),
	]

	AGE_CHOICES = [
		('adult', 'Adult'),
		('young', 'Young'),
		('all', 'All'),
	]

	YES_NO_CHOICES = [
		('yes', 'Yes'),
		('no', 'No'),
	]
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to_official = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disease_report', limit_choices_to={'is_official': True})
	date=models.DateField()
	livestock_category = models.CharField(max_length=20, choices=LIVESTOCK_CATEGORY_CHOICES)
	other_livestock_category = models.CharField(max_length=50, blank=True, null=True)
	number_of_animals_affected = models.IntegerField()
	sex_of_animals_affected = models.CharField(max_length=10, choices=SEX_CHOICES)
	age_of_animals_affected = models.CharField(max_length=10, choices=AGE_CHOICES)
	clinical_signs = models.TextField()
	number_of_dead_animals = models.IntegerField()
	propose_control_measures = models.TextField()
	sample_taken_to_lab = models.CharField(max_length=3, choices=YES_NO_CHOICES)
	tentative_diagnosis = models.TextField()
	village_disease_occurred = models.CharField(max_length=100)
	sub_county = models.CharField(max_length=100)
	county = models.CharField(max_length=100)
	owner_name = models.CharField(max_length=100)
	owner_mobile_number = models.CharField(max_length=20) 
	vet_in_charge_name = models.CharField(max_length=100)
	vet_registration_number = models.CharField(max_length=50)
	vet_mobile_number = models.CharField(max_length=20)
	signature=models.TextField(blank=True,null=True)
	#stamp = models.TextField(blank=True, null=True)

	def __str__(self):
		return f"Disease Report by {self.owner_name} on {self.village_disease_occurred}"

class Slaughterhouse(models.Model):
	CATEGORY_CHOICES = [
		('small_scale', 'Small Scale'),
		('large_scale', 'Large Scale'),
		# Add other categories if needed
	]
	
	SL_STATUS=[
		('private','Private'),
		('municipal','Municipal')
	]
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to_official = models.ForeignKey(User, on_delete=models.CASCADE, related_name='slaughter_house', limit_choices_to={'is_official': True})
	assigned_to_vet = models.ForeignKey(User, on_delete=models.CASCADE, related_name='slaughter_house_vet', limit_choices_to={'is_vet': True})
	reg_date=models.DateField()
	name = models.CharField(max_length=255)
	county = models.CharField(max_length=255)
	sub_county = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	slaughterhouse_status=models.CharField(max_length=50, choices=SL_STATUS)
	slaughterhouse_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
	livestock_slaughtered = models.CharField(max_length=255)  # Number of livestock slaughtered
	number_of_employees = models.IntegerField()
	roller_mark_number = models.CharField(max_length=50)
	inspector_name = models.CharField(max_length=255)
	inspector_registration_number = models.CharField(max_length=100)
	inspector_employment_number = models.CharField(max_length=100)
	inspector_mobile_number = models.CharField(max_length=15)

	def __str__(self):
		return self.name

# Employee Model
class Employee(models.Model):
    POSITION_CHOICES = [
        ('flager', 'Flager'),
        ('cleaner', 'Cleaner'),
        ('supervisor', 'Supervisor'),
        ('security_officer', 'Security Officer'),
    ]
    
    ML_LICENSE_CHOICES=[
		('updated','Updated'),
		('not_updated','Not Updated'),
	]
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    assigned_to_vet=models.ForeignKey(User, on_delete=models.CASCADE , related_name='employee_vet',default=1)
    enrollment_date=models.DateField()
    slaughterhouse = models.CharField(max_length=60)
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    medical_license_status = models.CharField(max_length=50,choices=ML_LICENSE_CHOICES)  
    
    def __str__(self):
        return self.name

# Butcher Details Model
class Butcher(models.Model):
    TRANSPORT_CHOICES = [
        ('motorbike', 'Motorbike'),
        ('vehicle', 'Vehicle'),
    ]
    LICENSE_CHOICES=[
		('updated','Updated'),
		('not_updated','Not Updated'),
	]
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    enrollment_date=models.DateField()
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    medical_license_status = models.CharField(max_length=50,choices=LICENSE_CHOICES)  # True for Updated, False for Not Updated
    livestock_slaughtered = models.CharField(max_length=50)  # Number of livestock slaughtered
    meat_container_number = models.CharField(max_length=50)
    meat_carrier_number = models.CharField(max_length=50)
    means_of_transport = models.CharField(max_length=50, choices=TRANSPORT_CHOICES)
    
    def __str__(self):
        return self.name

class Invoice(models.Model):
	ASSIGN_TO_CHOICES = [
		('farmer', 'Farmer'),
		('company', 'Company'),
	]

	INVOICE_CATEGORY_CHOICES = [
		('Deworming', 'Deworming'),
		('Surgery', 'Surgery'),
		('AI', 'Artificial Insemination'),
		('Clinical', 'Clinical'),
		('Vaccination', 'Vaccination'),
		('Post Mortem', 'Post Mortem'),
		('Pregnancy Diagnosis', 'Pregnancy Diagnosis'),
		('Lab Charges', 'Lab Charges'),
		('Farm Consultation', 'Farm Consultation'),
		('Telemedicine Services','Telemedicine Services'),
		('Uterine Irrigation', 'Uterine Irrigation'),
		('Emergency Care', 'Emergency Care'),
		('Livestock Examination', 'Livestock Examination'),
		('None', 'None'),
	]
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)	
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoice_report', limit_choices_to={'is_farmer': True})
	invoice_category = models.CharField(max_length=50, choices=INVOICE_CATEGORY_CHOICES)
	other_invoice_category=models.CharField(max_length=100)
	invoice_particulars=models.CharField(max_length=200)
	date_of_invoice = models.DateField()
	total_amount_due = models.DecimalField(max_digits=10, decimal_places=2)
	payment_method=models.CharField(max_length=30)
	farmer_name = models.CharField(max_length=100)
	village = models.CharField(max_length=100)
	contact = models.CharField(max_length=15)
	vet_in_charge_of_invoice = models.CharField(max_length=100)
	vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
	vet_registration_number = models.CharField(max_length=100)
	vet_contact = models.CharField(max_length=15)
	signature = models.CharField(max_length=100, blank=True, null=True)
	#stamp = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return f"Invoice {self.id} - {self.farmer_name}"

class DailyKill(models.Model):
	MEAT_CATEGORY_CHOICES = [
		('Bovine', 'Bovine'),
		('Caprine', 'Caprine'),
		('Ovine', 'Ovine'),
		('Porcine', 'Porcine'),
		('Camel', 'Camel'),
		('Poultry', 'Poultry'),
	]

	CONDEMNATION_STATUS_CHOICES = [
		('Local Condemnation', 'Local Condemnation'),
		('Carcass Condemnation', 'Carcass Condemnation'),
		('Passed For Consumption', 'Passed For Consumption'),
		('none', 'None')
	]

	INSPECTOR_STATUS_CHOICES = [
		('Employed', 'Employed'),
		('Delegated', 'Delegated'),
		('Intern/Student', 'Intern/Student'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Creator of the record
	assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='kills_official',
		limit_choices_to={'is_official': True},  # Ensure only officials can be assigned
		null=True,                 
		blank=True
	)
	
	assigned_by = models.ForeignKey(  # NEW FIELD to track who assigned the official
		User,
		on_delete=models.SET_NULL,
		related_name="assigned_kills",
		null=True,
		blank=True
	)
	date = models.DateField()
	livestock_category = models.CharField(max_length=50, choices=MEAT_CATEGORY_CHOICES)
	total_kills_per_day = models.PositiveIntegerField()
	condemnation_done = models.CharField(max_length=30)
	condemnation_status = models.CharField(max_length=50, choices=CONDEMNATION_STATUS_CHOICES, blank=True, null=True)
	comment_by_inspector = models.TextField(blank=True, null=True)
	inspector_name = models.CharField(max_length=100)
	inspector_reg_number = models.CharField(max_length=50)
	inspector_status = models.CharField(max_length=50, choices=INSPECTOR_STATUS_CHOICES)

	

	def __str__(self):
		return f"Daily Kill Record for {self.date} - {self.livestock_category}"
	def save(self, *args, **kwargs):
		"""Ensure assigned_by is set to the same user by default."""
		if not self.assigned_by:
			self.assigned_by = self.user  # Assign the authenticated user
		super().save(*args, **kwargs)

  
class ClientRequest(models.Model):
	REQUEST_TYPES = [
		('Emergency', 'Emergency'),
		('Non Emergency', 'Non Emergency'),
	]

	STATUS_CHOICES = [
		('Pending', 'Pending'),
		('Accepted', 'Accepted'),
		('Declined', 'Declined'),
	]

	EMERGENCY_CONDITIONS = [
		('severe_bleeding', 'Severe Bleeding'),
		('dystocia', 'Dystocia'),
		('bloat', 'Bloat'),
		('snake bite', 'Snake Bite'),
		('fracture', 'Fracture'),
		('uterine prolapse', 'Uterine Prolapse'),
		('choking', 'Choking'),
		('milk fever', 'Milk Fever'),
		('none', 'None'),
	]

	NON_EMERGENCY_CONDITIONS = [
		('Chronic Condition', 'Chronic Condition'),
		('Farm Visit', 'Farm Visit'),
		('None', 'None'),
	]

	LIVESTOCK_CATEGORIES = [
		('Cattle', 'Cattle'),
		('Sheep', 'Sheep'),
		('Goat', 'Goat'),
		('Donkey', 'Donkey'),
		('Dog', 'Dog'),
		('Cat', 'Cat'),
		('Poultry', 'Poultry'),
		('Horse', 'Horse'),
		('None', 'None'),
	]
	COMMUNICATION=[
			('Audio Call', 'Audio Call'),
		('Video Calls', 'Video Calls'),
		('Sms', 'Sms'),
	]
	TELEMEDICINE_CATEGORIES = [
		('Teletriage', 'Teletriage'),
		('Teleconsultation', 'Teleconsultation'),
		('Telemonitoring', 'Telemonitoring'),
		('Teleadvice', 'Teleadvice'),
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	assigned_to = models.ForeignKey(
		User, 
		on_delete=models.CASCADE, 
		related_name='request_report', 
		limit_choices_to={'is_vet_officer': True}
	)
	assigned_by = models.ForeignKey( 
		User,
		on_delete=models.CASCADE,
		related_name="assigned_request",
		null=True,
		blank=True
	)
	farmer_name = models.CharField(max_length=100)  
	contact = models.CharField(max_length=13)  
	location = models.CharField(max_length=100)  
	date_of_request = models.DateField(null=True, blank=True)
	time_of_request = models.TimeField(null=True, blank=True)
	telemedicine_category = models.CharField(max_length=20, choices=TELEMEDICINE_CATEGORIES)
	request_type = models.CharField(max_length=15, choices=REQUEST_TYPES)
	communication_methods=models.CharField(max_length=15, choices=COMMUNICATION)
	emergency_condition = models.CharField(max_length=50, choices=EMERGENCY_CONDITIONS, blank=True, null=True)
	non_emergency_condition = models.CharField(max_length=50, choices=NON_EMERGENCY_CONDITIONS, blank=True, null=True)
	case_history=models.TextField(blank=True,null=True)
	livestock_category = models.CharField(max_length=20, choices=LIVESTOCK_CATEGORIES)
	other_livestock_category = models.CharField(max_length=255, blank=True, null=True)
	consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
	photo = models.ImageField(upload_to='livestock_photos/',null=True,blank=True)
	consent = models.BooleanField(default=False)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending' ,null=True,blank=True)
	judgement=models.BooleanField(default=False)
	def save(self, *args, **kwargs):
		if not self.assigned_by and self.assigned_to:  # Ensure assigned_by is only set when assigned_to exists
			self.assigned_by = self.user  # Set the authenticated user as assigned_by
			
		if self.user:
			self.farmer_name = self.user.first_name
			self.contact = self.user.phone_number
			self.location = self.user.location

		super().save(*args, **kwargs)
class VetJudgment(models.Model):
    TELEMEDICINE_CATEGORIES = [
        ('Teletriage', 'Teletriage'),
        ('Teleconsultation', 'Teleconsultation'),
        ('Telemonitoring', 'Telemonitoring'),
        ('Teleadvice', 'Teleadvice'),
    ]

    REQUEST_TYPES = [
        ('Emergency', 'Emergency'),
        ('Non Emergency', 'Non Emergency'),
    ]

    EMERGENCY_CONDITIONS = [
        ('severe_bleeding', 'Severe Bleeding'),
        ('dystocia', 'Dystocia'),
        ('bloat', 'Bloat'),
        ('snake bite', 'Snake Bite'),
        ('fracture', 'Fracture'),
        ('uterine prolapse', 'Uterine Prolapse'),
        ('choking', 'Choking'),
        ('milk fever', 'Milk Fever'),
        ('none', 'None'),
    ]

    NON_EMERGENCY_CONDITIONS = [
        ('Chronic Condition', 'Chronic Condition'),
        ('Farm Visit', 'Farm Visit'),
        ('None', 'None'),
    ]

    LIVESTOCK_CATEGORIES = [
        ('Cattle', 'Cattle'),
        ('Sheep', 'Sheep'),
        ('Goat', 'Goat'),
        ('Donkey', 'Donkey'),
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Poultry', 'Poultry'),
        ('Horse', 'Horse'),
        ('None', 'None'),
    ]

    PROGNOSIS_CHOICES = [
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
        ('Grave', 'Grave'),
    ]

    PRACTITIONER_JUDGMENT = [
        ('Manageable', 'Manageable'),
        ('Culling', 'Culling'),
        ('Emergency Slaughter', 'Emergency Slaughter'),
        ('Referred Case', 'Referred Case'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Farmer making the request
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vet_judgments', limit_choices_to={'is_farmer': True})  # Vet officer handling the request
    date_of_judgment = models.DateField()
    telemedicine_category = models.CharField(max_length=20, choices=TELEMEDICINE_CATEGORIES)
    request_type = models.CharField(max_length=15, choices=REQUEST_TYPES)
    emergency_condition = models.CharField(max_length=50, choices=EMERGENCY_CONDITIONS, blank=True, null=True)
    non_emergency_condition = models.CharField(max_length=50, choices=NON_EMERGENCY_CONDITIONS, blank=True, null=True)
    livestock_category = models.CharField(max_length=20, choices=LIVESTOCK_CATEGORIES)
    other_livestock_category = models.CharField(max_length=255, blank=True, null=True)
    tentative_diagnosis = models.TextField()
    prognosis = models.CharField(max_length=10, choices=PROGNOSIS_CHOICES)
    practitioner_judgment = models.CharField(max_length=25, choices=PRACTITIONER_JUDGMENT)
    prescription_details = models.TextField(blank=True, null=True)
    # Changed from ForeignKey to CharField
    vet_name = models.CharField(max_length=100)  # Vet officer's name
    kvb_no = models.CharField(max_length=100, blank=True, null=True)  # Vet officer's registration number
    vet_category = models.CharField(max_length=100, blank=True, null=True)  # Vet officer's specialization
    vet_contact = models.CharField(max_length=13, blank=True, null=True)  # Vet officer's phone number
    referral_details = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.user:  # Ensure the vet officer exists before assigning values
            self.vet_name = self.user.get_full_name()  # Get full name
            self.kvb_no = self.user.registration_number
            self.vet_category = self.user.vet_category
            self.vet_contact = self.user.phone_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Judgment for {self.user.username} on {self.date_of_judgment}"

# class Question(models.Model):
#     text = models.CharField(max_length=255)

#     def __str__(self):
#         return self.text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, related_name='choice', on_delete=models.CASCADE)
#     text = models.CharField(max_length=100)
#     is_correct = models.BooleanField(default=False)

#     def __str__(self):
#         return self.text

# class UserAnswer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,default=1) 
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user} - {self.question.text}"
    
    #tuutorials
 
 
  
class Tutorial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    lesson = models.CharField(max_length=255)
    cpd_number = models.CharField(max_length=30)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    points = models.IntegerField()
    presented_by=models.CharField(max_length=100)
    contact_hours = models.CharField(max_length=50, default="0")
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson
class Section(models.Model):
    lesson = models.ForeignKey(Tutorial, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    file = models.FileField(upload_to='uploads/')
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lesson.lesson}"
    
class Comment(models.Model):
    section = models.ForeignKey(Section, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.section.title}"

class CpdQuestions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="questions")
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text


class CpdChoices(models.Model):
    question = models.ForeignKey(CpdQuestions, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.choice_text} - {'Correct' if self.is_correct else 'Incorrect'}"

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="results")
    score = models.FloatField()
    passed = models.CharField(
        max_length=10, 
        choices=[('pass', 'Pass'), ('fail', 'Fail')], 
        default='fail'
    )
    failed_attempts=models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.passed} - {self.score}%"
# class Questions(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question_text = models.CharField(max_length=255)

#     def __str__(self):
#         return self.question_text
# class QuestionResult(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     score = models.FloatField()
#     passed = models.CharField(
#         max_length=10, 
#         choices=[('pass', 'Pass'), ('fail', 'Fail')], 
#         default='fail'
#     )
#     failed_attempts=models.IntegerField()
#     timestamp = models.DateTimeField(auto_now_add=True)
# class QuestionsChoices(models.Model):
#     question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='qchoices')
#     choice_text = models.CharField(max_length=255)
#     is_correct = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.choice_text} - {'Correct' if self.is_correct else 'Incorrect'}"

    
# class UserAnswers(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user.username} - {self.question.text} - {self.choice.text}"


class Moderator(models.Model):
    name = models.CharField(max_length=255)  # Or any other fields you need

    def __str__(self):
        return self.name  
class Question(models.Model):
    TARGET_GROUPS = [
        ('farmer', 'Farmer'),
        ('vet', 'Vet Officer'),
    ]

    moderator = models.ForeignKey(Moderator, on_delete=models.CASCADE)
    text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(
        max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]
    )
    target_group = models.CharField(max_length=10, choices=TARGET_GROUPS)

    def __str__(self):
        return self.text

class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    attempt_number = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class UserRetake(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    retakes_left = models.IntegerField(default=3)

    def reset_retakes(self):
        self.retakes_left = 3
        self.save()
    
    
def get_random_questions_for_user(user):
    if user.is_farmer:
        target_group = 'farmer'
    elif user.is_vet_officer:
        target_group = 'vet'
    else:
        return []  # Skip if not authorized

    questions = Question.objects.filter(target_group=target_group)

    num_questions = min(10, questions.count())
    return random.sample(list(questions), num_questions)
   
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.section.title} - Score: {self.score}"
    
class LivestockExaminationRecord(models.Model):
	LIVESTOCK_CATEGORIES = [
		('Cattle', 'Cattle'),
		('Sheep', 'Sheep'),
		('Goat', 'Goat'),
		('Poultry', 'Poultry'),
		('None', 'None'),
	]

	REASONS_FOR_EXAMINATION = [
		('Slaughter', 'Slaughter'),
		('Breeding', 'Breeding'),
		('Culling', 'Culling'),
		('Disease Control', 'Disease Control'),
		('For Sale', 'For Sale'),
	]
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	assigned_to_official = models.ForeignKey(User, on_delete=models.CASCADE, related_name='examination_report', limit_choices_to={'is_official': True})
	livestock_category = models.CharField(max_length=50, choices=LIVESTOCK_CATEGORIES)
	other_category = models.CharField(max_length=100, blank=True, null=True)
	age_of_animal = models.PositiveIntegerField()
	breed = models.CharField(max_length=100)
	sex_of_animal = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
	number_of_animals = models.PositiveIntegerField()
	origin_of_animal = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	reason_for_examination = models.CharField(max_length=50, choices=REASONS_FOR_EXAMINATION)
	recommendation = models.TextField()
	owner_name = models.CharField(max_length=100)
	owner_mobile_number = models.CharField(max_length=15)
	veterinary_officer_in_charge = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=50)
	veterinary_officer_mobile_number = models.CharField(max_length=15)
	veterinary_officer_signature = models.TextField()

	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.livestock_category} Examination Record - {self.owner_name}"
class CalvingRecord(models.Model):
    CALVING_PROCEDURES = [
        ('Normal', 'Normal'),
        ('Assisted', 'Assisted'),
        ('C-Section', 'C-Section'),
    ]

    RAB_STATUSES = [
        ('Natural Expulsion', 'Natural Expulsion'),
        ('Manual Removal', 'Manual Removal'),
    ]

    CALF_STATUS = [
        ('Live', 'Live'),
        ('Dead', 'Dead'),
    ]

    REASONS_FOR_DEAD_FOETUS = [
        ('Delayed Labour', 'Delayed Labour'),
        ('Breech Presentation', 'Breech Presentation'),
        ('None', 'None'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date_of_calving = models.DateField()
    insemination_date = models.DateField(blank=True, null=True)
    days_to_calving_down = models.PositiveIntegerField(help_text="Number of days to calving down", blank=True, null=True)
    cow_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50, blank=True, null=True)
    calving_procedure = models.CharField(max_length=20, choices=CALVING_PROCEDURES)
    rab_status = models.CharField(max_length=20, choices=RAB_STATUSES)
    hours_for_natural_expulsion = models.CharField(max_length=100, blank=True, null=True)
    calf_sex = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')])
    calf_status = models.CharField(max_length=10, choices=CALF_STATUS)
    reason_for_dead_foetus = models.CharField(max_length=50, choices=REASONS_FOR_DEAD_FOETUS, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.date_of_calving and self.insemination_date:
            self.days_to_calving_down = (self.date_of_calving - self.insemination_date).days
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Calving Record for {self.cow_name} - {self.date_of_calving}"
    
class AssessmentRecord(models.Model):
	LIVESTOCK_CATEGORIES = [
		('Cattle', 'Cattle'),
		('Sheep', 'Sheep'),
		('Goat', 'Goat'),
		('Dog', 'Dog'),
		('Cat', 'Cat'),
		('Horse', 'Horse'),
		('None', 'None'),
	]

	SEX_CHOICES = [
		('Male', 'Male'),
		('Female', 'Female'),
	]

	PLACE_OF_ASSESSMENT_CHOICES = [
		('Farm', 'Farm'),
		('Market', 'Market'),
	]

	REASON_FOR_ASSESSMENT_CHOICES = [
		('Slaughter', 'Slaughter'),
		('Breeding', 'Breeding'),
		('Culling', 'Culling'),
		('Disease Control', 'Disease Control'),
		('Sales', 'Sales'),
		('For Complaint', 'For Complaint'),
		('Theft Cases', 'Theft Cases'),
		('For Export', 'For Export'),
 		 ('Elective Surgery', 'Elective Surgery'),
	]
	COW_BREEDS = [
    ('Holstein', 'Holstein'),
    ('Jersey', 'Jersey'),
    ('Angus', 'Angus'),
    ('Hereford', 'Hereford'),
    ('Simmental', 'Simmental'),
    ('Brahman', 'Brahman'),
    ('Charolais', 'Charolais'),
    ('Limousin', 'Limousin'),
    ('Guernsey', 'Guernsey'),
    ('Ayrshire', 'Ayrshire'),
    ('Brown Swiss', 'Brown Swiss'),
    ('Shorthorn', 'Shorthorn'),
    ('Other', 'Other'),
]
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)	
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assesment_report', limit_choices_to={'is_farmer': True})
	livestock_category = models.CharField(max_length=20, choices=LIVESTOCK_CATEGORIES)
	other_category = models.CharField(max_length=50, blank=True, null=True)
	breed=models.CharField(max_length=50,choices=COW_BREEDS)
	date_of_assessment = models.DateField()
	name_of_animal = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=50)
	color_of_animal = models.CharField(max_length=50)
	age_of_animal = models.PositiveIntegerField()  # Assuming age is in years
	sex_of_animal = models.CharField(max_length=10, choices=SEX_CHOICES)
	number_of_animals = models.PositiveIntegerField()
	origin_of_animal = models.CharField(max_length=100)
	place_of_assessment = models.CharField(max_length=20, choices=PLACE_OF_ASSESSMENT_CHOICES)
	destination = models.CharField(max_length=100)
	reason_for_assessment = models.CharField(max_length=50, choices=REASON_FOR_ASSESSMENT_CHOICES)
	recommendation = models.TextField(blank=True, null=True)
	owner_of_animal = models.CharField(max_length=100)
	owner_mobile_number = models.CharField(max_length=15)
	veterinary_practitioner_in_charge = models.CharField(max_length=100)
	practitioner_registration_number = models.CharField(max_length=50)
	practitioner_contact = models.CharField(max_length=15)
	signature_and_stamp = models.TextField(blank=True, null=True)  # Assuming signature and stamp will be an image

	def __str__(self):
		return f"{self.livestock_category} - {self.name_of_animal} ({self.date_of_assessment})"

class MovementPermit(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)	
	assigned_to_official = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movement_permit', limit_choices_to={'is_official': True}, default=1)
	date_of_permit = models.DateField()
	sub_county_district = models.CharField(max_length=100)
	ward_level = models.CharField(max_length=100)
	authorized_by = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=15)
	uploaded_permit = models.FileField(upload_to='movement_permits/')

	def __str__(self):
		return f"Permit {self.registration_number} - {self.date_of_permit}"

class NoObjection(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)	
	assigned_to_official = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noobjection_form', limit_choices_to={'is_official': True}, default=1)
	date_of_confirmation = models.DateField()
	sub_county_district = models.CharField(max_length=100)
	ward_level = models.CharField(max_length=100)
	confirmed_by = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=15)
	uploaded_no_objection_form = models.FileField(upload_to='no_objection_forms/')

	def __str__(self):
		return f"No Objection {self.registration_number} - {self.date_of_confirmation}"
class MonthlyReport(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)	
	assigned_to_official = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  
        related_name='monthly_reports_official',
        limit_choices_to={'is_official': True},
        null=True,                 
        blank=True,               
        default=1                  
    )
	date_of_submission = models.DateField()
	sub_county = models.CharField(max_length=100)
	ward_level = models.CharField(max_length=100)
	submitted_by = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=15)
	uploaded_report = models.FileField(upload_to='monthly_reports/')

	def __str__(self):
		return f"Monthly Report - {self.date_of_submission} by {self.submitted_by}"

class QuarterlyReport(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)	
	assigned_to_official = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  
        related_name='quartely_reports_official',
        limit_choices_to={'is_official': True},
        null=True,                 
        blank=True,               
        default=1                  
    )
	date_of_submission = models.DateField()
	sub_county = models.CharField(max_length=100)
	ward_level = models.CharField(max_length=100)
	submitted_by = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=15)
	uploaded_report = models.FileField(upload_to='monthly_reports/')

	def __str__(self):
		return f"Monthly Report - {self.date_of_submission} by {self.submitted_by}"
class YearlyReport(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)	
	assigned_to_official = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  
        related_name='yearly_reports_official',
        limit_choices_to={'is_official': True},
        null=True,                 
        blank=True,               
        default=1                  
    )
	date_of_submission = models.DateField()
	sub_county = models.CharField(max_length=100)
	ward_level = models.CharField(max_length=100)
	submitted_by = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=15)
	uploaded_report = models.FileField(upload_to='monthly_reports/')

	def __str__(self):
		return f"Monthly Report - {self.date_of_submission} by {self.submitted_by}"



class Practitioner(models.Model):
	SPECIALIZATION_CHOICES = [
		('large_animals', 'Large Animals'),
		('small_animals', 'Small Animals'),
	]

	VET_CATEGORY_CHOICES = [
		('surgeon', 'Surgeon'),
		('technologist', 'Technologist'),
		('technician', 'Technician'),
	]
 
	EMP_STATUS_CHOICES=[
		('employed','Employed'),
		('private_practitioner','Private Practitioneer ')
	]





	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	assigned_to_official = models.ForeignKey(
		User, on_delete=models.CASCADE, related_name='practitioner_record',
		limit_choices_to={'is_official': True}, default=1
	)
	assigned_by = models.ForeignKey(  
		User,
		on_delete=models.CASCADE,
		related_name="assigned_prac",
		null=True,
		blank=True
	)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	reg_date=models.DateField()
	phone_number = models.CharField(max_length=20)
	email = models.CharField(max_length=100)
	county = models.CharField(max_length=30)
	subcounty = models.CharField(max_length=30)
	ward = models.CharField(max_length=30)
	area_of_operation = models.CharField(max_length=30)
	specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
	vet_category = models.CharField(max_length=50, choices=VET_CATEGORY_CHOICES)
	registration_number = models.CharField(max_length=50)
	employment_status=models.CharField(max_length=50,choices=EMP_STATUS_CHOICES)

	def __str__(self):
		return f"{self.first_name} {self.last_name} - {self.specialization}"

class UterineIrrigationRecord(models.Model):
	LIVESTOCK_CATEGORIES = [
		('Cattle', 'Cattle'),
		('Goat', 'Goat'),
		('Sheep', 'Sheep'),
		('Horse', 'Horse'),
		('Dog', 'Dog'),
		('Pissi', 'Pissi'),
	]

	ASSIGNMENT_CHOICES = [
		('Bull', 'Bull'),
		('AI', 'Artificial Insemination (AI)'),
	]

	ABORTION_STATUS=[
		('Yes', 'Yes'),
		('No', 'No'),
		
	]
	RAB=[
		('Yes', 'Yes'),
		('No', 'No'),
	]
	REASONS=[
		('Repeat Breeding','Repeat Breeding'),
		('Metritis','Metritis'),
		('Abortion','Abortion'),
		('RAB','RAB'),
	]
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uterine', limit_choices_to={'is_farmer': True})
	livestock_category = models.CharField(max_length=20, choices=LIVESTOCK_CATEGORIES)
	name_of_animal = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=100)
	registration_date=models.DateField()
	reason=models.CharField(max_length=20, choices=REASONS)
	number_of_repeats = models.IntegerField(default=0)
	abortion_status_history = models.CharField(max_length=20, choices=ABORTION_STATUS)  # True for Yes, False for No
	rabies_status_history = models.CharField(max_length=20, choices=RAB)
	exp_ex_date=models.DateField()# True for Yes, False for No
	previous_insemination_by = models.CharField(max_length=100)
	treatment_plan = models.TextField(blank=True, null=True)
	drugs_of_choice = models.CharField(max_length=200, blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
	owner_name = models.CharField(max_length=100)
	village = models.CharField(max_length=100)
	contact = models.CharField(max_length=15)
	vet_in_charge = models.CharField(max_length=100, blank=True, null=True)
	vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
	registration_number_vet = models.CharField(max_length=100, blank=True, null=True)
	contact_vet = models.CharField(max_length=15, blank=True, null=True)
	sign_and_stamp = models.TextField(blank=True, null=True)

	def __str__(self):
		return f"{self.name_of_animal} - {self.registration_number}"


class EmergencyCare(models.Model):
	LIVESTOCK_CATEGORY_CHOICES = [
		('Cattle', 'Cattle'),
		('Sheep', 'Sheep'),
		('Goat', 'Goat'),
		('Donkey', 'Donkey'),
		('Dog', 'Dog'),
		('Cat', 'Cat'),
		('Horse', 'Horse'),
		('Other', 'Other'),
	]

	EMERGENCY_CATEGORY_CHOICES = [
		('Dystocia', 'Dystocia'),
		('Poisoning', 'Poisoning'),
		('Fracture', 'Fracture'),
		('Uterine Prolapse', 'Uterine Prolapse'),
		('Arsini', 'Arsini'),
		('Milk Fever', 'Milk Fever'),
		('Severe Bleeding', 'Severe Bleeding'),
		('Bloat', 'Bloat'),
		('Heatstroke', 'Heatstroke'),
		('Choking', 'Choking'),
		('Injury', 'Injury'),
	]

	CONDITION_CHOICES = [
		('Severe', 'Severe'),
		('Moderate', 'Moderate'),
	]

	PROGNOSIS_DIAGNOSIS_CHOICES = [
		('Good', 'Good'),
		('Fair', 'Fair'),
		('Poor', 'Poor'),
		('Grave', 'Grave'),
	]

	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE,related_name='emergency', limit_choices_to={'is_farmer': True})
	date=models.DateField(null=True, blank=True)
	livestock_category = models.CharField(max_length=20, choices=LIVESTOCK_CATEGORY_CHOICES)
	other_category = models.CharField(max_length=100, blank=True, null=True)
	number_of_animals_affected = models.IntegerField()
	name_of_affected_animal = models.CharField(max_length=100)
	registration_number = models.CharField(max_length=50, blank=True, null=True)
	emergency_category = models.CharField(max_length=50, choices=EMERGENCY_CATEGORY_CHOICES)
	condition_of_emergency = models.CharField(max_length=20, choices=CONDITION_CHOICES)
	case_history = models.CharField(max_length=100,blank=True, null=True)
	clinical_signs = models.CharField(max_length=100,blank=True, null=True)
	prognosis = models.CharField(max_length=100,choices=PROGNOSIS_DIAGNOSIS_CHOICES)
	differential_diagnosis = models.CharField(max_length=200)
	final_diagnosis = models.CharField(max_length=100,blank=True, null=True)
	referral_status = models.BooleanField()
	treatment_plan = models.CharField(max_length=100,blank=True, null=True)
	drugs_of_choice = models.CharField(max_length=100,blank=True, null=True)
	#comment=models.TextField()
	owner_name = models.CharField(max_length=100)
	village = models.CharField(max_length=100)
	contact = models.CharField(max_length=15)
	vet_category=models.CharField(max_length=30,choices=VET_CATEGORY)
	vet_registration_number = models.CharField(max_length=50, blank=True, null=True)
	vet_contact = models.CharField(max_length=15, blank=True, null=True)
	signature_and_stamp = models.TextField(blank=True, null=True)

	def __str__(self):
		return f"Emergency Care for {self.name_of_affected_animal} ({self.livestock_category})"

class PriceList(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date_of_purchase = models.DateField()
    product_name = models.CharField(max_length=100)
    manufacturing_company = models.CharField(max_length=100)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=10, decimal_places=2)
    expiring_date = models.DateField()

    def __str__(self):
        return self.product_name
    
class Supplier(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	date_of_enrollment = models.DateField()
	supply_number=models.CharField(max_length=100, unique=True)
	name = models.CharField(max_length=100)
	mobile_number = models.CharField(max_length=15)
	location = models.CharField(max_length=100)
	business_name = models.CharField(max_length=100)
	MODE_OF_PAYMENT_CHOICES = [
		('CASH', 'Cash'),
		('MOBILE_MONEY', 'Mobile Money'),
		('CHEQUES', 'Cheques'),
	]
	mode_of_payment = models.CharField(max_length=20, choices=MODE_OF_PAYMENT_CHOICES)
	account_details = models.TextField()

	def __str__(self):
		return self.name

class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date_of_enrollment = models.DateField()
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    remarks = models.TextField()

    def __str__(self):
        return self.name
    
class Creditor(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date_of_transaction = models.DateField()
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    total_amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance_to_pay = models.DecimalField(max_digits=10, decimal_places=2)
    agreed_date_of_balance_payment = models.DateField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Debtor(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date_of_transaction = models.DateField()
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    invoice_no=models.CharField(max_length=40)
    total_invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)
    correction_done=models.CharField(max_length=20)
    amount_of_correction=models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2)
    previous_balance=models.DecimalField(max_digits=10, decimal_places=2)
    grand_total=models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance_to_pay = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class ManagementCommittee(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    POSITION_CHOICES = [
        ('Chairman', 'Chairman'),
        ('Secretary', 'Secretary'),
        ('Treasurer', 'Treasurer'),
    ]
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    date_of_enrolment = models.DateField()
    date_of_election = models.DateField()
    time_period = models.CharField(max_length=50)
    next_election_date = models.DateField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class HidesAndSkinsRecord(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date_of_kills = models.DateField()
    CATEGORY_CHOICES = [
        ('Hides', 'Hides'),
        ('Skins', 'Skins'),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    number_collected = models.PositiveIntegerField()
    date_of_transportation = models.DateField()
    MEANS_CHOICES = [
        ('Vehicle', 'Vehicle'),
        ('Motorbike', 'Motorbike'),
    ]
    means_of_transportation = models.CharField(max_length=10, choices=MEANS_CHOICES)
    reg_no_of_vehicle = models.CharField(max_length=50)
    taken_by = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.date_of_kills}"
    
#payment 

class ZoomToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.TextField()
    refresh_token = models.TextField()
    expires_at = models.DateTimeField()

class ZoomMeeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facilitator = models.CharField(max_length=100)
    meeting_id = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Changed to DecimalField for currency
    is_paid = models.BooleanField(default=False)  # Added the new field
    start_time = models.DateTimeField()
    join_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic
class Payment(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	merchant_request_id = models.CharField(max_length=255)
	checkout_request_id = models.CharField(max_length=255)
	amount = models.FloatField()
	phone_number = models.CharField(max_length=15)
	mpesa_receipt = models.CharField(max_length=255, unique=True, null=True, blank=True)
	status = models.CharField(max_length=50, default="Pending")
	timestamp = models.DateTimeField(auto_now_add=True)
	lesson = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="lesson_payments", null=True, blank=True)
	zoom_meeting = models.ForeignKey(ZoomMeeting, on_delete=models.CASCADE,related_name="meeting_payments", null=True, blank=True)


	def __str__(self):
		return f"{self.phone_number} - {self.amount} KES"
		
# models.py

class LessonAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'lesson')  # each user-lesson pair is unique

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title} - Paid: {self.is_paid}"


class ApprovedDairyFarm(models.Model):

	DESIGNATION_CHOICES = [
		('CDVS', 'CDVS'),
		('DLPO', 'DLPO'),
		('Ward Veterinary Officer', 'Ward Veterinary Officer'),
		('Ward Production Officer', 'Ward Production Officer'),
	]
	#user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	date_of_approval = models.DateField()
	name_of_farm = models.CharField(max_length=100)
	county = models.CharField(max_length=100)
	sub_county = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	name_of_owner = models.CharField(max_length=100)
	contact = models.CharField(max_length=20)
	farm_breeding_level = models.CharField(max_length=100)
	average_milk_per_cow = models.DecimalField(max_digits=6, decimal_places=2)
	highest_milk_producer = models.CharField(max_length=100)
	approved_by = models.CharField(max_length=100)
	designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)
	officer_contact = models.CharField(max_length=20)
	comment = models.TextField(blank=True, null=True)
	
	def __str__(self):
		return self.name_of_farm

class SlaughterhouseHygiene(models.Model):

	CLEANING_CATEGORY_CHOICES = [
		('Daily', 'Daily'),
		('Weekly', 'Weekly'),
	]

	CLEANING_PROCEDURE_CHOICES = [
		('Floor cleaning', 'Floor cleaning'),
		('Wall cleaning', 'Wall cleaning'),
		('Manure collection', 'Manure collection'),
		('Compound cleaning', 'Compound cleaning'),
		('Other', 'Other'),
	]
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	date_of_cleaning = models.DateField()
	cleaning_category = models.CharField(max_length=10, choices=CLEANING_CATEGORY_CHOICES)
	cleaning_procedure = models.CharField(max_length=30, choices=CLEANING_PROCEDURE_CHOICES)
	state_other_cleaning = models.CharField(max_length=100, blank=True, null=True)
	cleaning_done_by = models.CharField(max_length=100)
	contact_of_cleaner = models.CharField(max_length=20)
	supervised_by = models.CharField(max_length=100)
	supervisor_contact = models.CharField(max_length=20)
	remarks = models.TextField(blank=True, null=True)
	

	def __str__(self):
		return f"Hygiene on {self.date_of_cleaning}"


class SlaughterhouseAsset(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    ASSET_TYPE_CHOICES = [
        ('Land', 'Land'),
        ('Vehicle', 'Vehicle'),
        ('Knives', 'Knives'),
        ('Motorbike', 'Motorbike'),
        ('Other', 'Other'),
    ]

    date_of_entry = models.DateField()
    type_of_asset = models.CharField(max_length=20, choices=ASSET_TYPE_CHOICES)
    other_asset = models.CharField(max_length=100, blank=True, null=True)
    model_number = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    original_cost = models.DecimalField(max_digits=10, decimal_places=2)
    appossession_value = models.DecimalField(max_digits=10, decimal_places=2)
    depossession_value = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.type_of_asset} - {self.model_number}"
    
class LivestockRegistration(models.Model):
	LIVESTOCK_TYPES = [
		('dairy_cow', 'Dairy Cow'),
		('beef', 'Beef'),
		('sheep', 'Sheep'),
		('goat', 'Goat'),
	]

	SEX_CHOICES = [
		('male', 'Male'),
		('female', 'Female'),
	]

	ORIGIN_CHOICES = [
		('kenya', 'Kenya'),
		('imported', 'Imported'),
	]

	SOURCE_CHOICES = [
		('farm', 'Farm'),
		('market', 'Market'),
	]
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	livestock_type = models.CharField(max_length=20, choices=LIVESTOCK_TYPES)
	date_of_registration = models.DateField()
	breed = models.CharField(max_length=100)
	sex = models.CharField(max_length=6, choices=SEX_CHOICES)
	age = models.PositiveIntegerField(help_text="Age in months/years")
	body_weight = models.DecimalField(max_digits=6, decimal_places=2, help_text="Weight in KG")
	colour = models.CharField(max_length=50)
	number_of_births = models.PositiveIntegerField(default=0)
	given_name = models.CharField(max_length=100, blank=True, null=True)
	registration_number = models.CharField(max_length=100)
	breeding_level = models.CharField(max_length=100, blank=True, null=True)
	dam_details = models.CharField(max_length=255, blank=True, null=True)
	sire_details = models.CharField(max_length=255, blank=True, null=True)
	origin = models.CharField(max_length=10, choices=ORIGIN_CHOICES)
	country_of_importation = models.CharField(max_length=100, blank=True, null=True)
	source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
	farm_name = models.CharField(max_length=150)
	owner_name = models.CharField(max_length=150)
	owner_phone = models.CharField(max_length=20)
	owner_id_number = models.CharField(max_length=50)
	county = models.CharField(max_length=100)
	sub_county = models.CharField(max_length=100)
	village = models.CharField(max_length=100)
	practitioner_name = models.CharField(max_length=150)
	reg_number = models.CharField(max_length=100)
	contact = models.CharField(max_length=20)
	signature_and_stamp = models.CharField(max_length=255, blank=True, null=True)
	photo = models.ImageField(upload_to="livestock_photos/", blank=True, null=True)


	def __str__(self):
		return f"{self.livestock_type} - {self.registration_number}"

class VeterinaryEPrescription(models.Model):
    # --- Choice constants ---
	DRUG_CATEGORIES = [
		('I', 'I'),
		('II', 'II'),
		('III', 'III'),
		('IV', 'IV'),
	]

	PRESCRIPTION_TARGETS = [
		('vet practitioner', 'Vet Practitioner'),
		('farmer', 'Farmer'),
	]

	LIVESTOCK_TYPES = [
		('dairy cow', 'Dairy Cow'),
		('beef', 'Beef'),
		('sheep', 'Sheep'),
		('goat', 'Goat'),
	]

	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	pharmacy_name = models.CharField(max_length=150)
	location = models.CharField(max_length=200, blank=True)
	vet_practitioner_incharge = models.CharField(max_length=120)
	kvb_no = models.CharField("K.V.B No", max_length=50, blank=True)
	licence_no = models.CharField(max_length=50, blank=True)
	contact = models.CharField(max_length=120, blank=True)
	sign = models.CharField(max_length=120, blank=True)
	signed_on = models.DateField(blank=True, null=True)
	drug_category = models.CharField(max_length=3, choices=DRUG_CATEGORIES, blank=True)
	prescription_target = models.CharField(max_length=20, choices=PRESCRIPTION_TARGETS, blank=True)
	date_of_prescription = models.DateField()
	livestock_type = models.CharField(max_length=20, choices=LIVESTOCK_TYPES)
	breed = models.CharField(max_length=80, blank=True)
	age = models.CharField(max_length=40, blank=True, help_text="e.g., 2 years, 8 months")
	drug_trade_name = models.CharField(max_length=120)
	manufacturing_company = models.CharField(max_length=150, blank=True)
	batch_number = models.CharField(max_length=60, blank=True)
	drug_dosage = models.CharField(max_length=120, blank=True, help_text="e.g., 10 mg/kg BID")
	route_of_administration = models.CharField(max_length=80, blank=True, help_text="e.g., IM, IV, PO")
	drug_volume = models.CharField(max_length=60, blank=True, help_text="e.g., 10 ml, 1 vial")
	clinical_use = models.CharField(max_length=200, blank=True)
	duration_of_treatment = models.CharField(max_length=80, blank=True)
	withdrawal_period = models.CharField(max_length=80, blank=True)
	quantity_purchased = models.CharField(max_length=60, blank=True)
	storage_condition = models.CharField(max_length=150, blank=True)
	side_effect = models.CharField(max_length=200, blank=True)
	expiry_date = models.DateField(blank=True, null=True)
	vets_comments = models.TextField(blank=True)
	buyer_name = models.CharField(max_length=120, blank=True)
	buyer_category = models.CharField(max_length=20, choices=PRESCRIPTION_TARGETS, blank=True)
	buyer_kvb_no = models.CharField("Buyer K.V.B No", max_length=50, blank=True)
	buyer_licence_no = models.CharField(max_length=50, blank=True)
	buyer_signature = models.CharField(max_length=120, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-date_of_prescription", "-id"]
		verbose_name = "Veterinary e-Prescription"
		verbose_name_plural = "Veterinary e-Prescriptions"

	def __str__(self):
		return f"{self.drug_trade_name} for {self.livestock_type} on {self.date_of_prescription:%Y-%m-%d}"

class RoutineManagement(models.Model):
    LIVESTOCK_CATEGORIES = [
        ('dairy cow', 'Dairy Cow'),
        ('beef', 'Beef'),
        ('sheep', 'Sheep'),
        ('goat', 'Goat'),
        ('pig', 'Pig'),
        ('poultry', 'Poultry'),
        ('other', 'Other'),
    ]

    ROUTINE_MANAGEMENT_CHOICES = [
        ('dehorning', 'Dehorning'),
        ('castration', 'Castration'),
        ('hoof trimming', 'Hoof Trimming'),
        ('iron injection', 'Iron Injection'),
        ('debeaking', 'Debeaking'),
        ('shearing', 'Shearing'),
        ('other', 'Other'),
    ]

    VET_CATEGORIES = [
        ('surgeon', 'Surgeon'),
        ('technologist', 'Technologist'),
        ('technician', 'Technician'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_service = models.DateField()
    livestock_category = models.CharField(max_length=20, choices=LIVESTOCK_CATEGORIES)
    number_of_animals = models.PositiveIntegerField()
    animal_name = models.CharField(max_length=100, blank=True)
    reg_no = models.CharField("Registration No", max_length=50, blank=True)
    age = models.CharField(max_length=50, blank=True)
    routine_management = models.CharField(max_length=30, choices=ROUTINE_MANAGEMENT_CHOICES)
    other_management_practice = models.CharField(max_length=150, blank=True)
    owner_name = models.CharField(max_length=120)
    village = models.CharField(max_length=120, blank=True)
    contact = models.CharField(max_length=120, blank=True)
    vet_practitioner_incharge = models.CharField(max_length=120, blank=True)
    vet_category = models.CharField(max_length=20, choices=VET_CATEGORIES, blank=True)
    vet_reg_no = models.CharField("Vet Reg No", max_length=50, blank=True)
    signature_and_stamp = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_of_service", "-id"]
        verbose_name = "Routine Management"
        verbose_name_plural = "Routine Management Records"

    def __str__(self):
        return f"{self.livestock_category} - {self.date_of_service}"
    
class AbortionRecord(models.Model):
    LIVESTOCK_CATEGORIES = [
        ('dairy cow', 'Dairy Cow'),
        ('beef', 'Beef'),
        ('sheep', 'Sheep'),
        ('goat', 'Goat'),
        ('pig', 'Pig'),
        ('poultry', 'Poultry'),
        ('other', 'Other'),
    ]

    REASONS_FOR_ABORTION = [
        ('infection', 'Infection'),
        ('deworming', 'Deworming'),
        ('injuries', 'Injuries'),
        ('shock', 'Shock'),
        ('bull mounting', 'Bull Mounting'),
        ('other', 'Other'),
    ]

    VET_CATEGORIES = [
        ('surgeon', 'Surgeon'),
        ('technologist', 'Technologist'),
        ('technician', 'Technician'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    livestock_category = models.CharField(max_length=20, choices=LIVESTOCK_CATEGORIES)
    number_of_animals_aborted = models.PositiveIntegerField()
    animal_name = models.CharField(max_length=100, blank=True)
    reg_no = models.CharField("Registration No", max_length=50, blank=True)
    date_of_insemination = models.DateField(blank=True, null=True)
    date_of_abortion = models.DateField()
    reason_for_abortion = models.CharField(max_length=30, choices=REASONS_FOR_ABORTION)
    other_reason = models.CharField(max_length=150, blank=True)
    treatment_given = models.CharField(max_length=200, blank=True)
    remarks = models.TextField(blank=True)
    owner_name = models.CharField(max_length=120)
    contact = models.CharField(max_length=120, blank=True)
    village = models.CharField(max_length=120, blank=True)
    vet_practitioner_name = models.CharField(max_length=120, blank=True)
    vet_category = models.CharField(max_length=20, choices=VET_CATEGORIES, blank=True)
    vet_reg_no = models.CharField("Vet Reg No", max_length=50, blank=True)
    vet_contact = models.CharField(max_length=120, blank=True)
    signature_and_stamp = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_of_abortion", "-id"]
        verbose_name = "Abortion Record"
        verbose_name_plural = "Abortion Records"

    def __str__(self):
        return f"{self.livestock_category} - Abortion on {self.date_of_abortion}"
    
class ExtensionService(models.Model):
    TARGET_GROUP_CHOICES = [
        ("self_help_group", "Self Help Group"),
        ("cbo", "CBO"),
        ("community", "Community"),
        ("institution", "Institution"),
        ("field_day", "Field Day"),
    ]

    GROUP_PROJECT_CHOICES = [
        ("dairy", "Dairy"),
        ("beef", "Beef"),
        ("sheep", "Sheep"),
        ("goats", "Goats"),
        ("poultry", "Poultry"),
        ("other", "Other"),
    ]

    date_of_extension = models.DateField()
    venue = models.CharField(max_length=255)
    target_group = models.CharField(max_length=50, choices=TARGET_GROUP_CHOICES)
    topic_covered = models.CharField(max_length=255)

    number_of_participants = models.PositiveIntegerField()
    female_attendance = models.PositiveIntegerField(default=0)
    male_attendance = models.PositiveIntegerField(default=0)
    children_attendance = models.PositiveIntegerField(default=0)

    name_of_group = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    group_project = models.CharField(max_length=50, choices=GROUP_PROJECT_CHOICES, blank=True, null=True)
    village = models.CharField(max_length=255, blank=True, null=True)
    sub_county = models.CharField(max_length=255)

    # Group officials
    chairperson = models.CharField(max_length=255, blank=True, null=True)
    secretary = models.CharField(max_length=255, blank=True, null=True)
    treasurer = models.CharField(max_length=255, blank=True, null=True)
    member = models.CharField(max_length=255, blank=True, null=True)

    facilitator_name = models.CharField(max_length=255)
    facilitator_contact = models.CharField(max_length=100, blank=True, null=True)

    gps_token = models.CharField(max_length=255, blank=True, null=True)
    extension_organized_by = models.CharField(max_length=255)
    remarks = models.TextField(blank=True, null=True)

    group_photo = models.ImageField(upload_to="extension_photos/", blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="extensions")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.topic_covered} - {self.date_of_extension}"
    
    
class FieldQuotation(models.Model):

	# --- Quotation Details ---
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	assigned_to = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='quotation',
		limit_choices_to={'is_farmer': False},
		null=True,                 
		blank=True,               
							
	)
	date_of_quotation = models.DateField()

	QUOTATION_CATEGORIES = [
		("deworming", "Deworming"),
		("surgery", "Surgery"),
		("clinical", "Clinical"),
		("ai", "Artificial Insemination"),
		("vaccination", "Vaccination"),
		("post_mortem", "Post Mortem"),
		("pregnancy_diagnosis", "Pregnancy Diagnosis"),
		("lab_charges", "Lab Charges"),
		("farm_consultation", "Farm Consultation"),
		("telemedicine", "Telemedicine Services"),
		("uterine_irrigation", "Uterine Irrigation"),
		("emergency", "Emergency Care"),
		("livestock_exam", "Livestock Examination"),
		("routine_mgmt", "Routine Management"),
	]

	quotation_category = models.CharField(
		max_length=50,
		choices=QUOTATION_CATEGORIES
	)

	# --- Payment / Animal Details ---
	number_of_animals = models.PositiveIntegerField(blank=True, null=True)

	payment_description = models.TextField(blank=True, null=True)
	amount_to_payment = models.DecimalField(
		max_digits=10, decimal_places=2, blank=True, null=True
	)

	# --- Farm Details ---
	name_of_farm = models.CharField(max_length=255, blank=True, null=True)
	owner_name = models.CharField(max_length=255, blank=True, null=True)
	owner_contact = models.CharField(max_length=50, blank=True, null=True)

	# --- Practitioner / Service Provider Details ---
	services_provided_by = models.CharField(max_length=255, blank=True, null=True)
	practitioner_name = models.CharField(max_length=255, blank=True, null=True)
	kvb_registration_number = models.CharField(max_length=50, blank=True, null=True)
	practitioner_contact = models.CharField(max_length=50, blank=True, null=True)

	# --- Signature ---
	signature_and_stamp = models.TextField( blank=True, null=True)

	def __str__(self):
		return f"Quotation - {self.date_of_quotation} - {self.owner_name}"

class ZoomAttendance(models.Model):
    meeting = models.ForeignKey(ZoomMeeting, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    join_time = models.DateTimeField()
    leave_time = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(default=0)  # in minutes
    points = models.FloatField(default=0)  # 1 point per hour

    def __str__(self):
        return f"{self.user_name} - {self.meeting.topic}"
    
class DairyFarmerRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Added user field
    date_of_registration = models.DateField()
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    total_number_of_dairy_cows = models.PositiveIntegerField()
    number_of_lactating_cows = models.PositiveIntegerField()
    
    BREEDS = (
        ("AI", "AI"),
        ("Bull", "Bull"),
        
    )
    breeds_used = models.CharField(max_length=20, choices=BREEDS)
    
    location = models.CharField(max_length=255)
    milk_supply_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.full_name} - {self.milk_supply_number}"

class MilkCollectionCenter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Added user field
    date_of_enrollment = models.DateField()
    name_of_collection_centre = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    agent_incharge = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    approximate_number_of_farmers = models.PositiveIntegerField()

    MEANS_OF_TRANSFER = (
        ("Motorbike", "Motorbike"),
        ("Vehicle", "Vehicle"),
        ("Lorry", "Lorry"),
    )
    means_of_transfer = models.CharField(max_length=20, choices=MEANS_OF_TRANSFER)

    transporter_name = models.CharField(max_length=255)
    transporter_mobile = models.CharField(max_length=20)
    time_of_milk_collection = models.TimeField()

    def __str__(self):
        return self.name_of_collection_centre


# 3. Current Milk Price
class CurrentMilkPrice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Added user field
    date_of_amendment = models.DateField()
    last_milk_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_milk_price = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Current Price: {self.current_milk_price}"


# 4. Farmer Milk Payments
class FarmerMilkPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Added user field
    date_of_payment = models.DateField()
    milk_supply_number = models.CharField(max_length=50)
    name_in_full = models.CharField(max_length=255)
    total_milk_supplied = models.DecimalField(max_digits=10, decimal_places=2)
    amount_to_be_paid = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payment for {self.name_in_full} - {self.date_of_payment}"
class MilkCollectionClerk(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	location = models.CharField(max_length=255)
	date = models.DateField()
	supply_number = models.CharField(max_length=100)
	total_kg_supplied = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return f"{self.supply_number} - {self.total_kg_supplied} kg"

class MilkCollectionCooler(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	clerk_record = models.OneToOneField(
		MilkCollectionClerk,
		on_delete=models.CASCADE,
		related_name="cooler_record",
		null=True,
		blank=True
	)
	date = models.DateField()
	location=models.CharField(max_length=100)
	supply_number = models.CharField(max_length=100)
	collection_status = models.CharField(max_length=20,choices=[('Accepted','Accepted'),('Rejected',('Rejected'))])
	reason = models.CharField(max_length=100,blank=True,default="N/A")
	total_kg_supplied = models.DecimalField(max_digits=10, decimal_places=2)
	name_of_supplier = models.CharField(max_length=255)
	remarks = models.TextField(blank=True, null=True)

	def __str__(self):
		return f"{self.supply_number} - {self.name_of_supplier}"

class MilkCollectionCenterRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date = models.DateField()
    supply_number = models.CharField(max_length=100)
    collection_status = models.CharField(max_length=20,choices=[('Accepted','Accepted'),('Rejected',('Rejected'))])
    reason = models.CharField(max_length=100,blank=True,default="N/A")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    name_of_center = models.CharField(max_length=255)
    name_of_agent = models.CharField(max_length=255)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name_of_center} - {self.supply_number}"
    
class DailyRevenueCollection(models.Model):
    REVENUE_SOURCES = [
        ('Vaccination', 'Vaccination'),
        ('Daily Levies', 'Daily Levies'),
        ('Movement Permits', 'Movement Permits'),
        ('A.I', 'Artificial Insemination'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='rev_official',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,               
							
	)
    date_of_record = models.DateField()
    sub_county = models.CharField(max_length=100)
    source_of_revenue = models.CharField(
        max_length=50,
        choices=REVENUE_SOURCES
    )
    total_collection = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date_of_record} - {self.sub_county} - {self.source_of_revenue}"


class LeaveRequest(models.Model):
    LEAVE_REASON_CHOICES = [
        ('Sick Leave', 'Sick Leave'),
        ('Maternity Leave', 'Maternity Leave'),
        ('Normal Leave', 'Normal Leave'),
    ]

    LEAVE_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='leav_official',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,               
							
	)
    date_of_leave_request = models.DateField()
    sub_county = models.CharField(max_length=100)

    total_annual_leave_days = models.PositiveIntegerField()
    days_of_leave_taken = models.PositiveIntegerField()
    remaining_days = models.PositiveIntegerField()

    reason_for_leave = models.CharField(
        max_length=50,
        choices=LEAVE_REASON_CHOICES
    )

    name_of_officer = models.CharField(max_length=150)
    employment_number = models.CharField(max_length=50)
    working_station = models.CharField(max_length=150)

    leave_status = models.CharField(
        max_length=20,
        choices=LEAVE_STATUS_CHOICES,
        default='Pending'
    )

    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_of_officer} - {self.date_of_leave_request}"


class MovementPermits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='mov_official',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,               
							
	)
    date_of_record = models.DateField()
    sub_county = models.CharField(max_length=100)
    livestock_category = models.CharField(max_length=100)
    total_animals = models.PositiveIntegerField()
    price_per_animal = models.DecimalField(max_digits=10, decimal_places=2)
    total_revenue_collected = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Movement Permits - {self.date_of_record}"

class NoObjections(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='nobs_official',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,               
							
	)
    date_of_record = models.DateField()
    sub_county = models.CharField(max_length=100)
    livestock_category = models.CharField(max_length=100)
    number_of_animals = models.PositiveIntegerField()
    cost_of_no_objection = models.DecimalField(max_digits=10, decimal_places=2)
    total_revenue_collected = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"No Objections - {self.date_of_record}"

class DiseaseReportMov(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='des_official',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,               
							
	)
    date_of_record = models.DateField()
    sub_county = models.CharField(max_length=100)
    livestock_category = models.CharField(max_length=100)
    number_of_reports = models.PositiveIntegerField()
    suspected_disease = models.CharField(max_length=150)
    proposed_intervention = models.TextField()
    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Disease Report - {self.date_of_record} - {self.sub_county}"
    
class Practitioners(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='pracs_official',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,               
							
	)

	date_of_record = models.DateField()
	sub_county =models.CharField(max_length=100)


	number_employed_by_county = models.PositiveIntegerField()
	number_in_private_practice = models.PositiveIntegerField()


	@property
	def total_practitioners(self):
		return self.number_employed_by_county + self.number_in_private_practice


	def __str__(self):
		return f"Practitioners - {self.sub_county} ({self.date_of_record})"
class DailyKills(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='dailyk_official',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,               
							
	)

	LIVESTOCK_CHOICES = (
		('cattle', 'Cattle'),
		('goat', 'Goat'),
		('sheep', 'Sheep'),
		('camel', 'Camel'),
		('pig', 'Pig'),
	)

	date_of_record = models.DateField()
	sub_county = models.CharField(max_length=100)

	livestock_category = models.CharField(max_length=20, choices=LIVESTOCK_CHOICES)
	number_of_kills = models.PositiveIntegerField()

	price_per_kill = models.DecimalField(max_digits=10, decimal_places=2)

	remarks = models.TextField(blank=True, null=True)

	@property
	def total_revenue_collected(self):
		return self.number_of_kills * self.price_per_kill

	def __str__(self):
		return f"{self.livestock_category} - {self.sub_county} ({self.date_of_record})"

class SlaughterHouses(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='slaugh_official',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,               
							
	)

	date_of_record = models.DateField()
	sub_county = models.CharField(max_length=100)

	private_slaughterhouses = models.PositiveIntegerField()
	county_slaughterhouses = models.PositiveIntegerField()

	employed_inspectors = models.PositiveIntegerField()
	roller_markers = models.PositiveIntegerField()

	@property
	def total_slaughterhouses(self):
		return self.private_slaughterhouses + self.county_slaughterhouses

	def __str__(self):
		return f"Slaughterhouses - {self.sub_county} ({self.date_of_record})"



class ArtificialInseminations(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='art_official',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,               
							
	)

	SEMEN_TYPE_CHOICES = (
		('Sexed', 'Sexed'),
		('Conventional', 'Conventional'),
		('Ai', 'AI'),
	)

	date_of_record = models.DateField()
	sub_county = models.CharField(max_length=100)

	number_of_cows_served = models.PositiveIntegerField()
	semen_type = models.CharField(max_length=20, choices=SEMEN_TYPE_CHOICES)

	repeat_cases = models.PositiveIntegerField(default=0)
	revenue_collected = models.DecimalField(max_digits=12, decimal_places=2)

	remarks = models.TextField(blank=True, null=True)

	def __str__(self):
		return f"AI - {self.sub_county} ({self.date_of_record})"

class Vaccinations(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='vacc_official',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,               
							
	)

	date_of_record = models.DateField()
	sub_county = models.CharField(max_length=100)

	animal_species = models.CharField(max_length=100)
	total_vaccinated = models.PositiveIntegerField()

	vaccine_used = models.CharField(max_length=150)
	vaccine_source = models.CharField(max_length=150)

	batch_number = models.CharField(max_length=100)
	expiry_date = models.DateField()

	revenue_collected = models.DecimalField(max_digits=12, decimal_places=2)

	remarks = models.TextField(blank=True, null=True)

	def __str__(self):
		return f"Vaccination - {self.animal_species} ({self.date_of_record})" 

class ExtensionServices(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	assigned_to_official = models.ForeignKey(
		User,
		on_delete=models.CASCADE,  
		related_name='ext',
		limit_choices_to={'is_official': True},
		null=True,                 
		blank=True,               
							
	)

	PROVIDER_CHOICES = (
		('private', 'Private'),
		('county', 'County Government'),
		('pharma', 'Pharmaceutical Companies'),
		('dairy', 'Dairy Cooperatives'),
	)

	date_of_record = models.DateField()
	sub_county = models.CharField(max_length=100)

	number_of_extensions_done = models.PositiveIntegerField()
	provider = models.CharField(max_length=20, choices=PROVIDER_CHOICES)

	remarks = models.TextField(blank=True, null=True)

	def __str__(self):
		return f"Extension Service - {self.sub_county} ({self.date_of_record})" 
