# KampusKart API

A backend API for **KampusKart**, an online marketplace for students, lecturers and staff at the
University of Zimbabwe (UZ) to buy and sell products around campus — laptops, textbooks,
furniture, hostel essentials, clothing and stationery.

## Features

- Product listing endpoint with search, category/condition filtering, ordering and pagination
- 32 realistic seeded products across 9 categories, priced in USD
- Django admin panel for managing products
- Consistent JSON error responses (400/404/500)
- CORS enabled for cross-origin frontend/API consumption
- SQLite for local development; PostgreSQL in production for persistent data
- Ready to deploy on Render via `render.yaml`

## Tech Stack

- Django 5
- Django REST Framework
- SQLite (development) / PostgreSQL (production)
- django-filter
- django-cors-headers
- gunicorn + whitenoise (production serving)

## Project Structure

```
kampuskart-api/
│
├── kampuskart/              # Project config: settings, root urls, error handlers, WSGI/ASGI
│   ├── settings.py
│   ├── urls.py
│   ├── views.py             # custom 404 / 500 JSON handlers
│   └── wsgi.py
│
├── products/                # Products app
│   ├── migrations/
│   ├── models.py            # Product model
│   ├── serializers.py       # ProductSerializer
│   ├── views.py             # ProductListAPIView
│   ├── urls.py
│   ├── admin.py
│   ├── exceptions.py        # DRF custom exception handler
│   ├── tests.py
│   └── management/
│       └── commands/
│           └── seed_products.py
│
├── requirements.txt
├── render.yaml
├── README.md
├── .gitignore
└── manage.py
```

## Installation

### 1. Clone the repository and enter the project folder

```bash
git clone <repository-url>
cd kampuskart-api
```

### 2. Create and activate a virtual environment

macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database (optional)

By default the app uses a local `db.sqlite3` file — no configuration needed. To point it at
PostgreSQL instead (e.g. to match production), set a `DATABASE_URL` environment variable:

```bash
export DATABASE_URL=postgresql://user:password@host:5432/dbname
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Seed the database

```bash
python manage.py seed_products
```

This populates the database with 32 realistic UZ marketplace products. It is safe to run more
than once — existing products are not duplicated.

### 7. (Optional) Create an admin superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

The API is now available at `http://127.0.0.1:8000/api/products/`.

## API Endpoints

### List products

```
GET /api/products/
```

Returns a paginated list of products (10 per page).

### Search

Searches product name and description:

```
GET /api/products/?search=laptop
```

### Filter by category

```
GET /api/products/?category=Electronics
```

Also supports filtering by condition:

```
GET /api/products/?condition=New
```

### Ordering

```
GET /api/products/?ordering=price
GET /api/products/?ordering=-price
GET /api/products/?ordering=name
```

### Combined example

```
GET /api/products/?category=Electronics&search=laptop&ordering=-price&page=1
```

### Example response

```json
{
  "count": 8,
  "next": "http://127.0.0.1:8000/api/products/?page=2",
  "previous": null,
  "results": [
    {
      "id": 2,
      "name": "HP EliteBook 840 G6",
      "description": "HP EliteBook 840 G6 in excellent condition. Perfect for Computer Science students. Battery lasts over six hours and includes original charger.",
      "category": "Electronics",
      "price": "380.00",
      "condition": "Used",
      "created_at": "2026-07-28T13:54:38.346297Z",
      "updated_at": "2026-07-28T13:54:38.346323Z"
    }
  ]
}
```

### Error response format

```json
{
  "error": {
    "status": 404,
    "message": "Not found."
  }
}
```

## Running Tests

```bash
python manage.py test products
```

## Deployment (Render)

This project deploys as a Render **Web Service** using `render.yaml`, backed by a **PostgreSQL**
database for persistent data.

1. Push the repository to GitHub.
2. Create a PostgreSQL database on Render (or another provider) if you haven't already.
3. In Render, choose **New > Blueprint** and point it at the repository — Render reads
   `render.yaml` automatically.
4. On the web service, set the `DATABASE_URL` environment variable to your database's connection
   string (add `?sslmode=require` for Render Postgres). This is not set automatically by
   `render.yaml` (`sync: false`), so it must be added manually in the dashboard.
5. Render will:
   - Install dependencies (`pip install -r requirements.txt`)
   - Collect static files (`collectstatic`)
   - On every boot, via `start.sh`: apply migrations (`migrate`) and seed the database
     (`seed_products`), then start the app with `gunicorn kampuskart.wsgi:application`
6. Other environment variables (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`) are configured in
   `render.yaml`; `SECRET_KEY` is auto-generated by Render.

Locally, the app defaults to SQLite (`db.sqlite3`) when `DATABASE_URL` is not set, so no extra
setup is needed for development. In production, PostgreSQL is used so data persists across
deploys and restarts — unlike SQLite, which lived on Render's ephemeral filesystem and was wiped
on every restart.

## Postman Collection

A ready-to-import Postman collection is included at
[`kampuskart.postman_collection.json`](kampuskart.postman_collection.json), covering:

- List all products
- Search products
- Filter by category
- Filter by condition
- Order by price
- Paginated request
