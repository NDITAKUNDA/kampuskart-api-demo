from django.db import models


class Product(models.Model):
    class Category(models.TextChoices):
        ELECTRONICS = "Electronics", "Electronics"
        FURNITURE = "Furniture", "Furniture"
        TEXTBOOKS = "Textbooks", "Textbooks"
        CLOTHING = "Clothing", "Clothing"
        HOSTEL_ESSENTIALS = "Hostel Essentials", "Hostel Essentials"
        KITCHEN_APPLIANCES = "Kitchen Appliances", "Kitchen Appliances"
        ACCESSORIES = "Accessories", "Accessories"
        STATIONERY = "Stationery", "Stationery"
        SPORTS = "Sports", "Sports"

    class Condition(models.TextChoices):
        NEW = "New", "New"
        USED = "Used", "Used"

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=Category.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(
        max_length=10, choices=Condition.choices, default=Condition.USED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
