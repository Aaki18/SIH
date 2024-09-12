from django.db import models

class Alumni(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    graduation_year = models.IntegerField()
    field_of_study = models.CharField(max_length=255)
    skills = models.TextField()
    area_of_interest = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Donation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField()

    def __str__(self):
        return f"Donation by {self.name} for {self.amount}"

class SuccessStory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Mentorship(models.Model):
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE)
    skills = models.TextField()
    area_of_interest = models.CharField(max_length=255)
    recommendations = models.JSONField(blank=True, null=True)  # To store mentorship recommendations

    def __str__(self):
        return f"Mentorship for {self.alumni.name}"
