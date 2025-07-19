from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']

class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.quote[:50]}"

    class Meta:
        ordering = ['-created_at']

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Gallery Image {self.id}"

    class Meta:
        ordering = ['-uploaded_at']



class Cabinet(models.Model):
    name = models.CharField(max_length=200, help_text="Full name of the cabinet member")
    role = models.CharField(max_length=100, help_text="Position or role in the cabinet (e.g., President, Secretary)")
    email = models.EmailField(blank=True, null=True, help_text="Contact email (optional)")
    phone = models.CharField(max_length=15, blank=True, null=True, help_text="Contact phone number (optional)")
    image = models.ImageField(upload_to='cabinet/', blank=True, null=True, help_text="Profile photo of the cabinet member")
    bio = models.TextField(blank=True, null=True, help_text="Brief biography or description")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date the member was added")

    def __str__(self):
        return f"{self.role}: {self.name}"

    class Meta:
        ordering = ['role', 'name'] 
        verbose_name_plural = "Cabinet Members"  

class Course(models.Model):
    COURSE_CHOICES = [
        ('BIT', 'Bachelor of Information Technology'),
        ('DCIT', 'Diploma in Computer Information Technology'),
        ('CSC', 'Computer Science'),
    ]
    title = models.CharField(max_length=200, choices=COURSE_CHOICES, help_text="Select the course type")
    description = models.TextField(help_text="Brief description of the course content")
    
    def __str__(self):
        return self.title
