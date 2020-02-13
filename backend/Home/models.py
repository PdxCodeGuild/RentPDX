from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Home(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_addr = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    max_occupancy = models.IntegerField()
    housing_type = models.CharField(max_length=10)
    rent_amt = models.IntegerField()
    sq_ft = model.models.IntegerField()
    no_bdr = models.IntegerField()
    no_bath = models.IntegerField()
    pkg_type = models.CharField(max_length=20)
    term_mo = models.IntegerField()
    ada = models.CharField(max_length=100, null=True, blank=True)
    pets = models.CharField(max_length=10)
    furnished = models.BooleanField()
    smoking = models.BooleanField()
    no_app_fee = models.BooleanField()
    no_broker_fee = models.BooleanField()
    img = models.ImageField(default='default.jpg', upload_to='home_pics')

    def __str__(self):
        return self

    def __save__(self, *args, **kwargs):
        super().save(*args, **kwargs)

    img = Image.open(self.img.path)

    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.img.path)
