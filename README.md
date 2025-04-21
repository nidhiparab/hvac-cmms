# HVAC Maintenance Management System


## Overview

This system helps HVAC teams track essential equipment, perform and log scheduled maintenance activities, and ensure basic compliance with ASHRAE 180 standards. It is designed to be lightweight and fast to set up, with minimal UI for quick adoption by technicians.

## Technology Stack

- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: Vue.js
- **CI/CD**: CircleCI (for automated testing and deployment)

## Core Focus

- Simplified for **HVAC maintenance workflows**
- Minimal interface for field technicians
- Captures **core ASHRAE 180** compliance data
- Scalable and modular REST API for future expansion

## Features

- **Equipment Management**: Register HVAC units with location and installation details
- **Core Maintenance Tasks**:
  - Filter inspection
  - Coil cleaning
  - Refrigerant checks
  - System testing
    ![image](https://github.com/user-attachments/assets/a4ad2396-cdb1-492c-9785-89789804356f)

- **Maintenance Logging**: Record results of performed tasks and report issues
  ![image](https://github.com/user-attachments/assets/de940423-0073-4032-88c7-30fc8eea8e1c)

- **Dashboard Statistics**: Quick summaries including:
  - Total equipment count
  - Tasks due in the next week
  - Recently completed maintenance
  - Maintenance tasks with reported issues
    ![image](https://github.com/user-attachments/assets/a038e1f7-e92d-42c3-a49d-55168b500efa)


## RESTful API Endpoints

### Equipment
- `GET /api/equipment/`
- `POST /api/equipment/`
- `GET /api/equipment/{id}/`
- `PUT /api/equipment/{id}/`
- `DELETE /api/equipment/{id}/`

### Maintenance Tasks
- `GET /api/maintenance-tasks/`
- `POST /api/maintenance-tasks/`
- `GET /api/maintenance-tasks/{id}/`
- `PUT /api/maintenance-tasks/{id}/`
- `DELETE /api/maintenance-tasks/{id}/`

### Maintenance Logs
- `GET /api/maintenance-logs/`
- `POST /api/maintenance-logs/`
- `GET /api/maintenance-logs/{id}/`
- `PUT /api/maintenance-logs/{id}/`
- `DELETE /api/maintenance-logs/{id}/`

### Dashboard
- `GET /api/dashboard-summary/`

## Database Schema

Minimal schema with 3 primary tables:

- `Equipment`: Stores HVAC unit data
- `MaintenanceTask`: Predefined core tasks and scheduling
- `MaintenanceLog`: Captures completion data and issues

## Installation

1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/hvac-maintenance-system.git
    cd hvac-maintenance-system
    ```

2. Set up a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations
    ```bash
    python manage.py migrate
    ```

5. Start development server
    ```bash
    python manage.py runserver
    ```

## Frontend (Vue.js)

Set up separately in `/frontend` directory:
```bash
cd frontend
npm install
npm run serve
