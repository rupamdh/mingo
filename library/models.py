from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    COPIE_CHOICE = (
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('reserved', 'Reserved'),
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    status = models.BooleanField()
    price = models.IntegerField()
    copies = models.CharField(max_length=200, choices=COPIE_CHOICE, default='available')
    created_at = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return self.title
