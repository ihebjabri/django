from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


class Category(models.Model):
    """Recipe categories like Breakfast, Lunch, Dinner, Dessert, etc."""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Bootstrap icon class or emoji")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Enhanced Recipe model with image and categories"""
    DIFFICULTY_CHOICES = [
        ('easy', 'Facile'),
        ('medium', 'Moyen'),
        ('hard', 'Difficile'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    day = models.DateField(help_text="Date du repas")
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/', null=True, blank=True, help_text="Recipe image")
    categories = models.ManyToManyField(Category, blank=True, related_name='recipes')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    preparation_time = models.PositiveIntegerField(help_text="Temps en minutes", default=30)
    servings = models.PositiveIntegerField(help_text="Nombre de personnes", default=2)

    # Nutrition Information (per serving)
    calories = models.PositiveIntegerField(null=True, blank=True, help_text="Calories per serving")
    protein = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True, help_text="Protein in grams")
    carbs = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True, help_text="Carbohydrates in grams")
    fats = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True, help_text="Fats in grams")

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.day})"

    def average_rating(self):
        """Calculate average rating for this recipe"""
        return self.ratings.aggregate(Avg('score'))['score__avg'] or 0

    def rating_count(self):
        """Get total number of ratings"""
        return self.ratings.count()

    def like_count(self):
        """Get total number of likes"""
        return self.likes.count()

    def is_liked_by(self, user):
        """Check if recipe is liked by specific user"""
        if user.is_authenticated:
            return self.likes.filter(user=user).exists()
        return False


class Rating(models.Model):
    """User ratings and reviews for recipes"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5 stars"
    )
    review = models.TextField(blank=True, help_text="Optional review text")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['recipe', 'user']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.recipe.name} ({self.score}★)"


class CookingStep(models.Model):
    """Step-by-step cooking instructions with optional timers"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='cooking_steps')
    step_number = models.PositiveIntegerField(help_text="Order of this step")
    title = models.CharField(max_length=100, blank=True, help_text="Optional step title")
    instruction = models.TextField(help_text="Detailed instruction for this step")
    duration_minutes = models.PositiveIntegerField(null=True, blank=True, help_text="Time needed for this step")
    image = models.ImageField(upload_to='steps/', null=True, blank=True, help_text="Optional step image")

    class Meta:
        ordering = ['recipe', 'step_number']
        unique_together = ['recipe', 'step_number']

    def __str__(self):
        return f"{self.recipe.name} - Step {self.step_number}"


class RecipeLike(models.Model):
    """Track user likes on recipes for social features"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_recipes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['recipe', 'user']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} likes {self.recipe.name}"
