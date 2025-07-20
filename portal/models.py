from django.db import models

# Apartments section
class Apartment(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[("Available", "Available"), ("Unavailable", "Unavailable")]
    )

    def __str__(self):
        return self.name

# Bookings section
class Booking(models.Model):
    guest_name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.guest_name} - {self.date}"

# Hosts section
class Host(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

# Live Chat messages
class ChatMessage(models.Model):
    sender = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.message[:30]}"

# Live Logs
class LogEntry(models.Model):
    timestamp = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.message[:40]}"

# Finance Management
class FinanceRecord(models.Model):
    category = models.CharField(max_length=50)  # e.g. Revenue or Expense
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - ${self.amount}"