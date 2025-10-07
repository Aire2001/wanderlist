from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField  # 🌍 Country dropdown
from django.utils import timezone


# ==============================
# 👤 USER PROFILE MODEL
# ==============================
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username or self.user.username}'s Profile"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    profile, _ = UserProfile.objects.get_or_create(user=instance)
    profile.username = instance.username
    profile.email = instance.email
    profile.save()


# ==============================
# 🌍 DESTINATION MODEL
# ==============================
class Destination(models.Model):
    STATUS_CHOICES = [
        ("Wishlist", "Wishlist"),
        ("Visited", "Visited"),
        ("Vacation", "Vacation"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="destinations"
    )

    name = models.CharField(
        max_length=255,
        verbose_name="Destination Name",
        default="Unnamed Destination",
    )

    location = CountryField(
        blank_label="Select a country",
        blank=True,
        null=True
    )

    # ✅ Optional city field
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Optional city name, like 'Boracay' or 'Tokyo'"
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Wishlist"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        country_name = getattr(self.location, "name", "Unknown")
        return f"{self.name} - {country_name}"

    def save(self, *args, **kwargs):
        """Ensure updated_at always updates."""
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-updated_at", "-created_at"]
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"
