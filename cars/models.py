from django.db import models
from tomlkit import datetime
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.
class Car(models.Model):

    state_choice = (
        ('PU','Punjab'),
        ('SN','Sindh'),
        ('KPK','Khaibr'),
        ('BL','Blochistan'),
    )
    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choice = (
        ('Cruise Control' , 'Cruise Control'),
        ('Audio Interface' , 'Audio Interface'),
        ('Airbags' , 'Airbags'),
        ('Air Conditioning' , 'Air Conditioning'),
        ('Seat Heating' , 'Seat Heating'),

    )

    door_choice = (
        ('2' , '2'),
        ('3' , '3'),
        ('4' , '4'),
        ('5' , '5'),
        ('6' , '6'),

    )

    title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo =  models.ImageField(upload_to='photos')
    car_photo1 = models.ImageField(upload_to='photos',blank=True)
    car_photo2 = models.ImageField(upload_to='photos',blank=True)
    car_photo3 = models.ImageField(upload_to='photos',blank=True)
    car_photo4 = models.ImageField(upload_to='photos',blank=True)
    features = MultiSelectField(choices=features_choice)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choice,max_length=100)
    passenger = models.CharField(max_length=100)
    vin_no = models.CharField(max_length=100)
    milage = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    np_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(max_length=100)
    created_date = models.DateTimeField(default=datetime.now, blank=True)


def __str__(self):
    return self.title



    