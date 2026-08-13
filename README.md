# FastAPI Demo

A simple full-stack product management app with a FastAPI backend and a React frontend.

## Stack

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: React, Axios

## Project structure

```
FastAPIdemo/
├── main.py               # FastAPI app and API routes
├── database.py           # SQLAlchemy engine/session setup
├── database_models.py    # SQLAlchemy ORM models
├── models.py             # Pydantic schemas
└── frontend/              # React app
    ├── public/
    └── src/
```

## Prerequisites

- Python 3.12+
- Node.js and npm
- PostgreSQL running locally

## Backend setup

1. Create and activate a virtual environment:
   ```zsh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```zsh
   pip install fastapi uvicorn sqlalchemy psycopg2-binary
   ```

3. Configure the database connection in `database.py`. It currently points to:
   ```
   postgresql://admin@localhost:5432/fastdemo
   ```
   Update the username, password, host, or database name to match your local PostgreSQL setup.

4. Run the API server:
   ```zsh
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`. On startup, it creates the `product` table if it doesn't exist and seeds it with sample products if the table is empty.

## Frontend setup

1. Install dependencies:
   ```zsh
   cd frontend
   npm install
   ```

2. Start the dev server:
   ```zsh
   npm start
   ```
   The app runs at `http://localhost:3000` and talks to the API at `http://localhost:8000`.

## API endpoints

| Method | Path            | Description           |
|--------|-----------------|------------------------|
| GET    | `/greet/`       | Health check greeting |
| GET    | `/products/`    | List all products     |
| GET    | `/products/{id}`| Get a product by ID   |
| POST   | `/products/`    | Create a product      |
| PUT    | `/products/{id}`| Update a product      |
| DELETE | `/products/{id}`| Delete a product      |

## Notes

- CORS is currently open to all origins (`allow_origins=["*"]`); restrict this before deploying anywhere public.
- The database URL in `database.py` is hard-coded; consider moving it to an environment variable for anything beyond local development.
