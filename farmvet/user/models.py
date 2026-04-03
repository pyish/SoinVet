from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    is_vet_officer = models.BooleanField(default=False)
    is_farmer = models.BooleanField(default=False)
    is_official = models.BooleanField(default=False)
    is_cooperative = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=13)
    specialization = models.CharField(max_length=100,null=True)
    county=models.CharField(max_length=100,null=True)
    subcounty=models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    vet_category = models.CharField(max_length=100,null=True)
    supervisor=models.CharField(max_length=100,null=True)
    registration_number = models.CharField(max_length=100,null=True)
    licence_number=models.CharField(max_length=100,null=True)
    business_name=models.CharField(max_length=100,default="SOIN VETERINARY SERVICES")
    cooperative_name=models.CharField(max_length=100,default="DAIRY COOPERATIVE SERVICES")
    farm_name = models.CharField(max_length=100,default="SOINFARM")
    #agree_to_privacy = models.BooleanField(default=False)
    
    

class Vet_Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return f'Name: {self.user.username}'
	
class Farmer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	county = models.CharField(max_length=100,default='Unknown')
	location = models.CharField(max_length=100, default='My location')

	def __str__(self):
		return f'Name: {self.user.username} Phone number {self.user.phone_number}'
	
class Official(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    county = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=100)
    employment_number=models.CharField(max_length=100)
    designation=models.CharField(max_length=50)


    def __str__(self):
        return f'Name: {self.user.username}'
    
class DairyCooperative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    county = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=100)
    #cooperative_name=models.CharField(max_length=100)
    reg_no=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)


    def __str__(self):
        return f'Name: {self.user.username}'

class Farm(models.Model):
	#farm_name = models.CharField(max_length=100)
	farm_owner = models.ForeignKey(Farmer, on_delete=models.CASCADE)
	location = models.CharField(max_length=100)

	def __str__(self):
		return f'Farm Name: {self.farm_name}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='user_pics')

    def __str__(self):
        return self.user.username     

def post_save_profile_create(sender, instance, created,*args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)                                       
        
post_save.connect(post_save_profile_create, sender=User)            


class ShopProductType(models.Model):

	name = models.CharField(max_length=45)

	def __str__(self):
		return u'%s %s' % (self.id, self.name)




class ProductItem(models.Model):
	name = models.CharField(max_length=45)
	description = models.CharField(max_length=200, null=True, blank=True)
	product_type = models.ForeignKey(ShopProductType, on_delete=models.CASCADE)
	#institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
	def __str__(self):
		return u'%s %s' % (self.id, self.name)	



# class ProductItem(models.Model):
#     name = models.CharField(max_length=64)
#     unit_cost = models.FloatField()

#     def __str__(self) -> str:
#         return super().__str__(f'Product Item{self.name}')


class SupplierProduct(models.Model):
    supplier = models.CharField(max_length=64)
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)

    def __str__(self):
        return f'Supplier Product: {self.product.name}' 		