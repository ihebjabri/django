# Recipe Meal Planner

A Django-based web application for managing recipes and planning meals. This application supports multiple user roles including administrators, chefs, and regular users.

## Features

- **User Authentication**: Secure login and signup system with role-based access control
- **Recipe Management**: Create, view, and manage recipes with detailed information
- **Meal Planning**: Calendar view for planning meals throughout the week
- **Role-Based Dashboards**:
  - Admin Dashboard: Administrative controls and oversight
  - Chef Dashboard: Recipe creation and management
  - User Dashboard: Personal meal planning and recipe viewing
- **Recipe Details**: Track preparation time, servings, ingredients, and instructions
- **PDF Export**: Generate PDF documents for recipes

## Technologies Used

- **Backend**: Django (Python)
- **Database**: SQLite3
- **Frontend**: HTML templates with Django template engine
- **User Management**: Django authentication system

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/ihebjabri/django.git
cd recipe_meal_planner
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
# Add other dependencies as needed
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application at `http://127.0.0.1:8000/`

## Project Structure

```
recipe_meal_planner/
├── core/               # Main project settings
├── home/               # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View logic
│   ├── forms.py        # Form definitions
│   ├── urls.py         # URL routing
│   └── migrations/     # Database migrations
├── templates/          # HTML templates
│   ├── dashboards/     # Role-specific dashboards
│   ├── recipes/        # Recipe-related templates
│   └── registration/   # Authentication templates
└── manage.py           # Django management script
```

## Usage

### For Users
- Sign up for an account or log in
- Browse available recipes
- Plan meals using the calendar view
- View recipe details including preparation time and servings

### For Chefs
- Access the chef dashboard
- Create and manage recipes
- Add ingredients and cooking instructions
- Specify preparation times and serving sizes

### For Administrators
- Access the admin dashboard
- Manage users and permissions
- Oversee all recipes and meal plans

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or support, please open an issue on GitHub.
