# RGJ Solutions - Backend (Flask)

This is the Flask backend for **RGJ Solutions**, a full-stack web application for a car detailing business. It handles API routes for customer inquiries submitted from the frontend, validates input, and stores data in a PostgreSQL database hosted on Render.

---

## 🌐 Live API

Base URL: [https://rgjcs.onrender.com](https://rgjcs.onrender.com)

---

## 🧰 Tech Stack

- **Flask** – Lightweight Python web framework  
- **Flask-CORS** – Handles Cross-Origin Resource Sharing for frontend/backend interaction  
- **SQLAlchemy** – ORM for PostgreSQL database access  
- **Render** – Hosting for both backend and PostgreSQL instance  
- **dotenv** – For managing secret keys and configs  

---

## 📦 Features

- RESTful API for handling contact form submissions  
- Input validation and clean error handling  
- Secure handling of form data (name, email, message)  
- Hosted PostgreSQL database with persistent storage  
- CORS enabled to allow communication with deployed frontend  
