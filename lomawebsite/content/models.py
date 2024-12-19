from django.db import models


class MoviePoster(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BackgroundImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='backgrounds/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ConcessionItem(models.Model):
    CATEGORY_CHOICES = [
        ('popcorn', 'Popcorn'),
        ('combo', 'Combo'),
        ('candy', 'Candy'),
        ('drink', 'Drink'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class TicketPrice(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General Admission'),
        ('3d', '3D Admission'),
    ]
    SHOWTIME_CHOICES = [
        ('evening', 'Evening Show'),
        ('matinee', 'Matinee'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    showtime = models.CharField(max_length=50, choices=SHOWTIME_CHOICES)
    age_group = models.CharField(max_length=50)  # E.g., Adults, Students, etc.
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.showtime} - {self.age_group}"
