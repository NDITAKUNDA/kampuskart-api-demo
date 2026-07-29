from django.core.management.base import BaseCommand

from products.models import Product

PRODUCTS = [
    {
        "name": "Dell Latitude 5420",
        "description": (
            "Dell Latitude 5420 in great working condition. Core i5 11th gen, "
            "8GB RAM, 256GB SSD. Ideal for Computer Science and Engineering "
            "students. Comes with original charger."
        ),
        "category": Product.Category.ELECTRONICS,
        "price": "350.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "HP EliteBook 840 G6",
        "description": (
            "HP EliteBook 840 G6 in excellent condition. Perfect for Computer "
            "Science students. Battery lasts over six hours and includes "
            "original charger."
        ),
        "category": Product.Category.ELECTRONICS,
        "price": "380.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Lenovo ThinkPad T480",
        "description": (
            "Reliable Lenovo ThinkPad T480, Core i5, 8GB RAM, 180GB SSD. "
            "Good for assignments, research and light programming work. "
            "Minor scratches on the lid but works perfectly."
        ),
        "category": Product.Category.ELECTRONICS,
        "price": "300.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Samsung Galaxy A55",
        "description": (
            "Samsung Galaxy A55, 128GB storage, dual SIM. Bought early this "
            "year, still under local warranty. Selling because I upgraded."
        ),
        "category": Product.Category.ELECTRONICS,
        "price": "280.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "iPhone 12",
        "description": (
            "iPhone 12, 64GB, battery health above 85%. No cracks, screen "
            "protector on since day one. Comes with box and cable."
        ),
        "category": Product.Category.ELECTRONICS,
        "price": "420.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "JBL Headphones",
        "description": (
            "JBL over-ear headphones, great bass, perfect for studying in "
            "the library or hostel. Barely used, still sounds crisp."
        ),
        "category": Product.Category.ELECTRONICS,
        "price": "25.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "TP-Link WiFi Router",
        "description": (
            "TP-Link dual-band WiFi router, good coverage for a hostel room "
            "or flat shared by several students. Easy to set up."
        ),
        "category": Product.Category.ELECTRONICS,
        "price": "20.00",
        "condition": Product.Condition.NEW,
    },
    {
        "name": "Xiaomi Power Bank 20000mAh",
        "description": (
            "Xiaomi 20000mAh power bank, fast charging, great for long days "
            "of lectures when load-shedding hits. Original box included."
        ),
        "category": Product.Category.ELECTRONICS,
        "price": "18.00",
        "condition": Product.Condition.NEW,
    },
    {
        "name": "Engineering Mathematics Textbook",
        "description": (
            "Engineering Mathematics textbook covering calculus, linear "
            "algebra and differential equations. Used for one semester, no "
            "missing pages, minor highlighting."
        ),
        "category": Product.Category.TEXTBOOKS,
        "price": "15.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Introduction to Programming with Python",
        "description": (
            "Beginner-friendly Python programming textbook, great for first "
            "year Computer Science and Informatics students. Clean copy."
        ),
        "category": Product.Category.TEXTBOOKS,
        "price": "12.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Accounting Principles",
        "description": (
            "Accounting Principles textbook used in first year Commerce "
            "courses. Well maintained, all pages intact."
        ),
        "category": Product.Category.TEXTBOOKS,
        "price": "14.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Organic Chemistry",
        "description": (
            "Organic Chemistry textbook for BSc Chemistry and Biochemistry "
            "students. Some notes in the margins that may actually help "
            "during revision."
        ),
        "category": Product.Category.TEXTBOOKS,
        "price": "16.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Financial Management",
        "description": (
            "Financial Management textbook for Business Studies and "
            "Commerce students. Good condition, no water damage."
        ),
        "category": Product.Category.TEXTBOOKS,
        "price": "13.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Database Systems",
        "description": (
            "Database Systems textbook covering SQL, normalization and ER "
            "modelling. Useful reference alongside practical coursework."
        ),
        "category": Product.Category.TEXTBOOKS,
        "price": "15.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Wooden Study Desk",
        "description": (
            "Sturdy wooden study desk, ideal for a hostel room. Some minor "
            "wear on the surface but very stable, no wobbling."
        ),
        "category": Product.Category.FURNITURE,
        "price": "45.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Office Chair",
        "description": (
            "Comfortable padded office chair with adjustable height. Great "
            "for long study sessions. Selling because I am moving out of "
            "res."
        ),
        "category": Product.Category.FURNITURE,
        "price": "35.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Single Bed",
        "description": (
            "Single bed frame with a firm mattress, perfect size for a "
            "hostel or lodgings room. Clean and structurally sound."
        ),
        "category": Product.Category.FURNITURE,
        "price": "90.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Wardrobe",
        "description": (
            "Two-door wardrobe with a hanging rail and shelf space. Good "
            "condition, easy to disassemble for moving."
        ),
        "category": Product.Category.FURNITURE,
        "price": "70.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Bookshelf",
        "description": (
            "Three-tier wooden bookshelf, enough space for textbooks and "
            "files. Light enough to move between rooms."
        ),
        "category": Product.Category.FURNITURE,
        "price": "30.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Electric Kettle",
        "description": (
            "Electric kettle, boils water fast, great for tea, coffee or "
            "instant noodles between lectures. Auto shut-off included."
        ),
        "category": Product.Category.HOSTEL_ESSENTIALS,
        "price": "15.00",
        "condition": Product.Condition.NEW,
    },
    {
        "name": "Microwave",
        "description": (
            "Compact microwave, ideal for warming up sadza and stew or "
            "leftovers in a hostel kitchenette. Works perfectly."
        ),
        "category": Product.Category.HOSTEL_ESSENTIALS,
        "price": "55.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Hisense Fridge",
        "description": (
            "Small Hisense fridge, perfect for keeping drinks and perishables "
            "cool in a hostel room. Quiet compressor, low power draw."
        ),
        "category": Product.Category.HOSTEL_ESSENTIALS,
        "price": "110.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Extension Cable",
        "description": (
            "4-way extension cable with surge protection, useful for "
            "charging multiple devices in a shared hostel room."
        ),
        "category": Product.Category.HOSTEL_ESSENTIALS,
        "price": "8.00",
        "condition": Product.Condition.NEW,
    },
    {
        "name": "Standing Fan",
        "description": (
            "Standing fan with adjustable height and speed settings, great "
            "for hot October nights before exams."
        ),
        "category": Product.Category.HOSTEL_ESSENTIALS,
        "price": "28.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Nike Sneakers",
        "description": (
            "Nike sneakers, size 9, worn a handful of times. Comfortable for "
            "walking around campus between lectures."
        ),
        "category": Product.Category.CLOTHING,
        "price": "30.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Adidas Backpack",
        "description": (
            "Adidas backpack with laptop compartment, great for carrying "
            "textbooks and a laptop around campus. Zips all working."
        ),
        "category": Product.Category.CLOTHING,
        "price": "22.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "University Hoodie",
        "description": (
            "University of Zimbabwe branded hoodie, size L. Warm and great "
            "for early morning lectures."
        ),
        "category": Product.Category.CLOTHING,
        "price": "18.00",
        "condition": Product.Condition.NEW,
    },
    {
        "name": "Dynamos FC Jersey",
        "description": (
            "Dynamos FC replica jersey, size M. Great for matchdays and "
            "casual wear around res."
        ),
        "category": Product.Category.CLOTHING,
        "price": "20.00",
        "condition": Product.Condition.NEW,
    },
    {
        "name": "Scientific Calculator",
        "description": (
            "Casio scientific calculator, supports all functions needed for "
            "Engineering and Science courses. Buttons all responsive."
        ),
        "category": Product.Category.STATIONERY,
        "price": "12.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Graph Books (Pack of 5)",
        "description": (
            "Pack of five graph books, useful for Mathematics, Physics and "
            "Engineering practicals and assignments."
        ),
        "category": Product.Category.STATIONERY,
        "price": "6.00",
        "condition": Product.Condition.NEW,
    },
    {
        "name": "Drawing Board",
        "description": (
            "A2 drawing board with clips, required for Architecture and "
            "Engineering Drawing courses. Flat surface, no warping."
        ),
        "category": Product.Category.STATIONERY,
        "price": "20.00",
        "condition": Product.Condition.USED,
    },
    {
        "name": "Lever Arch Files (Pack of 3)",
        "description": (
            "Pack of three lever arch files, ideal for organising handouts "
            "and assignments per module."
        ),
        "category": Product.Category.STATIONERY,
        "price": "9.00",
        "condition": Product.Condition.NEW,
    },
]


class Command(BaseCommand):
    help = (
        "Seed the database with realistic University of Zimbabwe marketplace products."
    )

    def handle(self, *args, **options):
        created_count = 0
        for product_data in PRODUCTS:
            _, created = Product.objects.get_or_create(
                name=product_data["name"],
                defaults=product_data,
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {created_count} new product(s). "
                f"{Product.objects.count()} total product(s) in the database."
            )
        )
