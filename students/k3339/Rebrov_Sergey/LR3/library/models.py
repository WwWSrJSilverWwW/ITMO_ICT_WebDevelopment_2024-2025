from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_staff']

    def __str__(self):
        return self.username


class Publisher(models.Model):
    name = models.CharField(max_length=128, null=True)
    year = models.IntegerField(null=True)

    def __str__(self):
        return f"({self.name} {self.year})"


class Author(models.Model):
    surname = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=128, null=True)
    patronymic = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"({self.name} {self.surname})"


class Book(models.Model):
    name = models.CharField(max_length=128, null=True)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    cipher = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"({self.name})"


class Library(models.Model):
    name = models.CharField(max_length=128, null=True)
    address = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"({self.name}"


class Hall(models.Model):
    number = models.IntegerField(null=True)
    name = models.CharField(max_length=128, null=True)
    capacity = models.IntegerField(null=True)
    library = models.ForeignKey(Library, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.number} {self.library})"


class Reader(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    surname = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=128, null=True)
    patronymic = models.CharField(max_length=128, null=True)
    ticket = models.CharField(max_length=128, null=True)
    passport = models.CharField(max_length=128, null=True)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=128, null=True)
    education = models.CharField(max_length=128, null=True)
    is_academic = models.BooleanField(default=False, null=True)
    hall = models.ForeignKey(Hall, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"({self.name} {self.surname})"


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.book} {self.author})"


class BookReader(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return f"({self.book} {self.reader})"


class BookHall(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, null=True, on_delete=models.CASCADE)
    count = models.IntegerField(null=True)

    def __str__(self):
        return f"({self.book} {self.hall})"
