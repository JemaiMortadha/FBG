# Product Feedback REST API

A simple RESTful API built with Flask and SQLite to manage feedback on digital products.

## 🛠️ Features

- Create users
- Create products
- Submit feedback
- Retrieve all feedback
- Filter feedback by product or user
- Delete feedback

## 📦 Endpoints

| Method | Endpoint                 | Description                     |
|--------|--------------------------|---------------------------------|
| POST   | `/users`                 | Add a new user                  |
| POST   | `/products`              | Add a new product               |
| POST   | `/feedback`              | Submit product feedback         |
| GET    | `/feedback`              | Get all feedback                |
| GET    | `/products/{id}/feedback`| Get feedback for a specific product |
| GET    | `/users/{id}/feedback`   | Get feedback left by a user     |
| DELETE | `/feedback/{id}`         | Delete a specific feedback      |

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy
