
rare_diseases = [
    "Huntington's Disease",
    "Fibrodysplasia Ossificans Progressiva (FOP)",
    "Adenylosuccinate Lyase Deficiency",
    "Progeria (Hutchinson-Gilford Progeria Syndrome)",
    "Ehlers-Danlos Syndrome",
    "Stiff Person Syndrome",
    "Niemann-Pick Disease",
    "Pulmonary Hypertension",
    "Gaucher's Disease",
    "Tay-Sachs Disease"
]
rare_diseases_africa = [
    "Sickle Cell Disease",
    "Burkitt Lymphoma",
    "African Trypanosomiasis (Sleeping Sickness)",
    "Nodding Syndrome",
    "Chronic Wasting Disease",
    "Onchocerciasis (River Blindness)",
    "Lymphatic Filariasis",
    "Kuru",
    "Albinism-related Complications",
    "Osteogenesis Imperfecta",
    "Phenylketonuria (PKU)",
    "Neurofibromatosis",
    "Fibrodysplasia Ossificans Progressiva",
    "Hyper IgM Syndrome",
    "Gaucher's Disease",
    "Marfan Syndrome",
    "Myasthenia Gravis",
    "Ataxia Telangiectasia",
    "Apert Syndrome",
    "Ehlers-Danlos Syndrome",
    "Usher Syndrome",
    "Cystic Fibrosis",
    "Wilson’s Disease",
    "Tay-Sachs Disease",
    "Mucopolysaccharidosis",
    "Congenital Adrenal Hyperplasia",
    "Xeroderma Pigmentosum",
    "Syringomyelia",
    "Alzheimer’s Disease",
    "Duchenne Muscular Dystrophy",
    "Maple Syrup Urine Disease",
    "Hypophosphatasia",
    "Syndrome of Inappropriate Antidiuretic Hormone (SIADH)",
    "Chronic Granulomatous Disease",
    "Lipoid Proteinosis",
    "Progeria",
    "Cutaneous T-cell Lymphoma",
    "Hereditary Hemorrhagic Telangiectasia",
    "Cerebrotendinous Xanthomatosis",
    "Cyclic Vomiting Syndrome",
    "Adenosine Deaminase Deficiency",
    "Glycogen Storage Disease",
    "Hypotrichosis",
    "Bardet-Biedl Syndrome",
    "Chorea-Acanthocytosis",
    "Familial Mediterranean Fever",
    "Kallmann Syndrome",
    "Maffucci Syndrome",
    "Niemann-Pick Disease",
    "Alkaptonuria",
    "Pyridoxine-Dependent Epilepsy",
    "Spinal Muscular Atrophy",
    "Congenital Disorders of Glycosylation",
    "Long QT Syndrome",
    "Brittle Bone Disease",
    "Oculocutaneous Albinism",
    "Sturge-Weber Syndrome",
    "Ectodermal Dysplasia",
    "Lynch Syndrome",
    "Ornithine Transcarbamylase Deficiency",
    "Episodic Ataxia",
    "Severe Combined Immunodeficiency (SCID)",
    "Hyper IgE Syndrome",
    "Hereditary Spherocytosis",
    "Andersen's Disease",
    "Congenital Myopathy",
    "Cohen Syndrome",
    "Gitelman Syndrome",
    "Isovaleric Acidemia",
    "Maple Syrup Urine Disease",
    "Syndrome X",
    "Epidermolysis Bullosa",
    "Fanconi Anemia",
    "Familial Hypercholesterolemia",
    "Thalassemia",
    "Mitochondrial Myopathy",
    "Congenital Lactic Acidosis",
    "Diamond-Blackfan Anemia",
    "Fraser Syndrome",
    "Hyperlipoproteinemia",
    "Hypophosphatemic Rickets",
    "Joubert Syndrome",
    "Myotonic Dystrophy",
    "Pachyonychia Congenita",
    "Primary Biliary Cholangitis",
    "Retinitis Pigmentosa",
    "Seipinopathy",
    "Smith-Lemli-Opitz Syndrome",
    "Stiff Person Syndrome",
    "Subacute Sclerosing Panencephalitis",
    "Tuberous Sclerosis Complex",
    "Vascular Ehlers-Danlos Syndrome",
    "Wilms' Tumor",
    "Alpha-1 Antitrypsin Deficiency",
    "Batten Disease",
    "Brachydactyly",
    "Chronic Pain Syndrome",
    "Hypokalemic Periodic Paralysis",
    "Hypercalcemia",
    "X-linked Lymphoproliferative Syndrome"
]


class RareDisease(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    prevalence = models.CharField(max_length=100)  # e.g., "1 in 100,000"
    etiology = models.TextField(blank=True, null=True)  # Causes of the disease
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Symptom(models.Model):
    disease = models.ForeignKey(RareDisease, related_name='symptoms', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.disease.name} - {self.description}"


class Treatment(models.Model):
    disease = models.ForeignKey(RareDisease, related_name='treatments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    approved = models.BooleanField(default=False)  # If the treatment is approved by health authorities

    def __str__(self):
        return f"{self.name} for {self.disease.name}"


class PatientRegistry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease = models.ForeignKey(RareDisease, related_name='registries', on_delete=models.CASCADE)
    date_diagnosed = models.DateField()
    symptoms_present = models.TextField()
    treatment_currently = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.disease.name}"


class ClinicalTrial(models.Model):
    disease = models.ForeignKey(RareDisease, related_name='clinical_trials', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    eligibility_criteria = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.title} for {self.disease.name}"