from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Product


class ProductListAPITests(APITestCase):
    def setUp(self):
        self.url = reverse("product-list")
        Product.objects.create(
            name="HP EliteBook 840 G6",
            description="Reliable laptop for Computer Science students.",
            category=Product.Category.ELECTRONICS,
            price="380.00",
            condition=Product.Condition.USED,
        )
        Product.objects.create(
            name="Engineering Mathematics Textbook",
            description="Covers calculus and linear algebra.",
            category=Product.Category.TEXTBOOKS,
            price="15.00",
            condition=Product.Condition.USED,
        )
        Product.objects.create(
            name="Electric Kettle",
            description="Boils water fast, great for tea and coffee.",
            category=Product.Category.HOSTEL_ESSENTIALS,
            price="15.00",
            condition=Product.Condition.NEW,
        )

    def test_list_products_returns_200_and_all_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 3)

    def test_search_by_name(self):
        response = self.client.get(self.url, {"search": "EliteBook"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["name"], "HP EliteBook 840 G6")

    def test_filter_by_category(self):
        response = self.client.get(self.url, {"category": "Textbooks"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["category"], "Textbooks")

    def test_ordering_by_price_ascending(self):
        response = self.client.get(self.url, {"ordering": "price"})
        prices = [item["price"] for item in response.data["results"]]
        self.assertEqual(prices, sorted(prices))

    def test_unknown_route_returns_404(self):
        response = self.client.get("/api/products/does-not-exist/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
