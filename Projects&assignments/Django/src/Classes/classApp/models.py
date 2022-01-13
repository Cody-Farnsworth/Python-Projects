from django.db import models

TYPE_CHOICES = {
    ('Math','Math'),
    ('English','English'),
    ('Accounting','Accounting'),
    ('Science','Science'),
}


class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, choices=TYPE_CHOICES)
    Course_Number = models.DecimalField(default=0, max_digits=10000, decimal_places=0)
    Instructor_Name = models.TextField(max_length=300, default="", blank=False)
    Duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)


    objects = models.Manager()

    def __str__(self):
        return self.Title

