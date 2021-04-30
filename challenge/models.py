from django.db import models


# These models correspond to the CSV files.
# column names are taken directly from the CSV.
# Depending on company convention, these might also be underscored.

class Tracking(models.Model):
    orderNo = models.CharField(max_length=200)
    tracking_number = models.IntegerField(unique=True, primary_key=True)
    courier = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    destination_country_iso3 = models.CharField(max_length=3)
    email = models.CharField(max_length=200)
    articleNo = models.CharField(max_length=200)
    articleImageUrl = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)

    def __str__(self):
        return self.orderNo


class Checkpoint(models.Model):
    # this should probably be converted to an int key, eventually.
    tracking_number = models.ForeignKey(
        Tracking, on_delete=models.CASCADE, to_field='tracking_number')
    # should be changed to
    # tracking_number = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    timestamp = models.DateTimeField('date recorded')
    status = models.CharField(max_length=200)
    status_text = models.CharField(max_length=200)
    status_details = models.CharField(max_length=200)

    def __str__(self):
        return str(self.timestamp) + self.status_text
