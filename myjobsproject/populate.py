import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myjobsproject.settings")
import django
django.setup()

from testapp.models import HydJobs,VizagJobs,BngJobs
from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
	d1 = randint(6,9)
	num = '' + str(d1)
	for i in range(9):
		num += str(randint(0,9))
	return int(num)
def populate(n):
	for i in range(n):
		fdate = fake.date()
		fcompany = fake.company()
		ftittle = fake.random_element(elements=('Project manager','Team Lead','Software Engineer','Associate Engineer',))
		feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd','Msc','Mahesh Sir Student'))
		faddress = fake.address()
		femail = fake.email()
		fphonenumber = phonenumbergen()
		hyd_jobs_record = HydJobs.objects.get_or_create(
		date = fdate,
		company = fcompany,
		tittle = ftittle,
		eligibility = feligibility,
		address = faddress,
		email = femail,
		phonenumber = fphonenumber,
		)
		vizag_jobs_record = VizagJobs.objects.get_or_create(
		date = fdate,
		company = fcompany,
		tittle = ftittle,
		eligibility = feligibility,
		address = faddress,
		email = femail,
		phonenumber = fphonenumber,
		)
		bng_jobs_record = BngJobs.objects.get_or_create(
		date = fdate,
		company = fcompany,
		tittle = ftittle,
		eligibility = feligibility,
		address = faddress,
		email = femail,
		phonenumber = fphonenumber,
		)
n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Records inserted Successfully....')
