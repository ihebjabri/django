# CookMaster Pro

<div align="center">
  <h3>🔥 Professional Cooking Platform</h3>
  <p>A modern, elegant recipe management and meal planning platform built with Django</p>
</div>

---

## 📖 About

**CookMaster Pro** is a professional-grade recipe management and meal planning platform designed for food enthusiasts, home cooks, and culinary professionals. With its elegant purple-blue gradient theme and comprehensive feature set, CookMaster Pro transforms the way you organize, plan, and share your culinary creations.

## ✨ Features

### 🍳 Recipe Management
- **Comprehensive Recipe Cards**: Store recipes with detailed information including preparation time, servings, difficulty levels, and beautiful images
- **Category Organization**: Tag recipes with multiple categories (Breakfast, Lunch, Dinner, Desserts, Italian, Vegetarian, etc.)
- **Difficulty Levels**: Easy, Medium, Hard classification for skill-appropriate cooking
- **Image Uploads**: Showcase your dishes with high-quality recipe photos

### 🥗 Nutrition Tracking
- **Nutrition Calculator**: Track calories, protein, carbohydrates, and fats per serving
- **Health-Conscious Cooking**: Make informed dietary decisions with detailed nutritional information

### 👨‍🍳 Step-by-Step Cooking
- **Cooking Instructions**: Break down recipes into numbered, detailed steps
- **Step Timers**: Each step can include duration in minutes for precise timing
- **Step Images**: Visual guides for complex cooking techniques
- **Progressive Cooking**: Follow along with clear, organized instructions

### ⭐ Social Features
- **Recipe Ratings**: 5-star rating system with written reviews
- **Recipe Likes**: Quick appreciation system to mark favorite recipes
- **User Engagement**: Build a community around shared culinary passion

### 📅 Meal Planning
- **Interactive Calendar**: Visual meal planning with FullCalendar integration
- **Weekly/Monthly Views**: Plan meals across different time horizons
- **Meal Organization**: Organize breakfast, lunch, dinner, and snacks
- **Planner Dashboard**: Dedicated interface for meal scheduling

### 🔐 User Roles & Permissions
- **Admin**: Full platform management and user oversight
- **Chef**: Create, edit, and manage recipes
- **User**: Browse recipes, create meal plans, rate and like recipes

### 🎨 Modern UI/UX
- **Elegant Design**: Professional purple-blue gradient theme with premium aesthetics
- **Responsive Layout**: Seamless experience across desktop, tablet, and mobile devices
- **Bootstrap 5**: Modern, accessible interface components
- **Bootstrap Icons**: Beautiful iconography throughout
- **Smooth Animations**: Polished transitions and hover effects

---

## 🛠️ Technology Stack

### Backend
- **Django 6.0.2**: High-level Python web framework
- **SQLite**: Development database (PostgreSQL-ready for production)
- **Pillow 12.1.0**: Image processing and upload handling
- **Python 3.x**: Core programming language

### Frontend
- **Bootstrap 5.3.3**: Responsive CSS framework
- **Bootstrap Icons 1.11.3**: Icon library
- **FullCalendar 6.1.11**: Interactive calendar component
- **Custom CSS**: Elegant purple-blue gradient theme with CSS variables

### Architecture
- **Django ORM**: Database abstraction and management
- **Class-Based Views (CBV)**: Reusable view components
- **Function-Based Views (FBV)**: Flexible endpoint handling
- **Django Admin**: Powerful administrative interface
- **Group-Based Authentication**: Role-based access control

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (venv)

### Step 1: Clone the Repository
```bash
git clone https://github.com/ihebjabri/django.git
cd recipe_meal_planner
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### Step 6: Create Static and Media Directories
```bash
mkdir -p static/css static/js static/images
mkdir -p media/recipes media/steps
```

### Step 7: Run Development Server
```bash
python manage.py runserver 8080
```

Visit `http://localhost:8080` to access CookMaster Pro!

---

## 📁 Project Structure

```
recipe_meal_planner/
├── core/                       # Project settings and configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL routing
│   └── wsgi.py                # WSGI deployment configuration
├── home/                       # Main application
│   ├── models.py              # Database models (Recipe, Category, Rating, etc.)
│   ├── views.py               # View logic
│   ├── forms.py               # Form definitions
│   ├── admin.py               # Admin panel customization
│   ├── urls.py                # App URL routing
│   └── utils.py               # Utility functions
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navigation
│   ├── recipes/               # Recipe-related templates
│   │   ├── list.html          # Recipe collection
│   │   ├── detail.html        # Recipe detail view
│   │   └── form.html          # Recipe creation/editing
│   ├── dashboards/            # Dashboard templates
│   │   ├── admin.html         # Admin dashboard
│   │   ├── chef.html          # Chef dashboard
│   │   ├── user.html          # User dashboard
│   │   └── calendar.html      # Meal planner
│   └── registration/          # Authentication templates
│       ├── login.html         # Login page
│       └── signup.html        # Registration page
├── static/                     # Static files (CSS, JS, images)
│   ├── css/
│   │   └── style.css          # Custom styling
│   ├── js/                    # JavaScript files
│   └── images/                # Static images
├── media/                      # User uploads
│   ├── recipes/               # Recipe images
│   └── steps/                 # Cooking step images
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
└── requirements.txt           # Python dependencies
```

---

## 👥 User Roles

### 🔴 Admin
- Full access to all platform features
- User management and role assignment
- Content moderation
- System configuration
- Access to Django admin panel

### 🟡 Chef
- Create and publish recipes
- Add cooking steps and nutrition information
- Upload recipe images
- Manage own recipe collection
- View analytics on recipe engagement

### 🟢 User (Regular)
- Browse recipe collection
- Search and filter recipes
- Create meal plans
- Rate and review recipes
- Like favorite recipes
- View nutritional information

---

## 🎯 Key Features Explained

### Recipe Creation
1. Navigate to dashboard (role-specific)
2. Click "Add New Recipe"
3. Fill in recipe details:
   - Name and description
   - Category selection (multiple)
   - Difficulty level
   - Preparation time and servings
   - Nutrition information (optional)
   - Recipe image
4. Add cooking steps with instructions and timers
5. Save and publish

### Meal Planning
1. Access "Meal Planner" from navigation
2. View calendar in month or week view
3. Click on a date to add meals
4. Select recipes from your collection
5. Organize by meal type (breakfast, lunch, dinner)
6. Track your weekly/monthly meal schedule

### Social Engagement
- **Rating**: Click on a recipe and provide 1-5 star rating with optional review
- **Liking**: Click the heart icon to like/unlike recipes
- **Browsing**: Filter by category, difficulty, or search by keywords

---

## 🎨 Theme Customization

CookMaster Pro uses CSS variables for easy theme customization. Edit `/static/css/style.css`:

```css
:root {
    --primary-color: #6366f1;        /* Indigo */
    --primary-dark: #4f46e5;
    --secondary-color: #8b5cf6;      /* Purple */
    --secondary-dark: #7c3aed;
    --accent-color: #ec4899;         /* Pink accent */
    --success-color: #10b981;
    --warning-color: #f59e0b;
    --danger-color: #ef4444;
}
```

---

## 🔧 Configuration

### Development Settings
- `DEBUG = True`
- SQLite database
- Static files served by Django

### Production Recommendations
- Set `DEBUG = False`
- Use PostgreSQL database
- Configure `ALLOWED_HOSTS`
- Use environment variables for `SECRET_KEY`
- Serve static files with WhiteNoise or CDN
- Configure media file storage (AWS S3, etc.)
- Enable HTTPS
- Set up logging

### Database Migration to PostgreSQL
```python
# Update settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cookmaster_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🧪 Development

### Running Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating Sample Data
Access Django admin at `http://localhost:8080/admin` and create:
1. Categories (Italian, Mexican, Breakfast, Desserts, etc.)
2. Sample recipes with images
3. Cooking steps
4. User accounts with different roles

### Collecting Static Files (Production)
```bash
python manage.py collectstatic
```

---

## 📊 Database Models

### Core Models
- **Recipe**: Main recipe entity with nutrition and metadata
- **Category**: Recipe categorization (ManyToMany with Recipe)
- **CookingStep**: Step-by-step instructions linked to recipes
- **RecipeLike**: Social engagement tracking
- **Rating**: User ratings and reviews (5-star system)
- **Day**: Meal planning calendar entries
- **UserProfile**: Extended user information (if implemented)

---

## 🔒 Security Features

- CSRF protection on all forms
- Password hashing with Django's built-in system
- Group-based permissions
- SQL injection protection via ORM
- XSS protection with template auto-escaping
- Secure file upload handling

---

## 📝 Future Enhancements

- [ ] Recipe sharing via social media
- [ ] Grocery list generation from meal plans
- [ ] Recipe collections and favorites
- [ ] Ingredient inventory management
- [ ] Recipe scaling calculator
- [ ] Print-friendly recipe cards
- [ ] Mobile app (iOS/Android)
- [ ] REST API for third-party integrations
- [ ] Recipe import from external sources
- [ ] Cooking mode (hands-free, step-by-step guidance)
- [ ] Community features (follow chefs, recipe feeds)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**CookMaster Pro Development Team**

---

## 🙏 Acknowledgments

- Django Software Foundation
- Bootstrap team
- FullCalendar contributors
- Bootstrap Icons
- The open-source community

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact the development team
- Check documentation

---

<div align="center">
  <p>Made with ❤️ by passionate developers and food enthusiasts</p>
  <p>© 2026 CookMaster Pro. Professional Cooking Platform.</p>
</div>
