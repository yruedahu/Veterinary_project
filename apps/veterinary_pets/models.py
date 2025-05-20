from django.db import models

class Especie(models.Model):
    specie = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.specie
    
class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    age = models.IntegerField()
    specie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='mascotas/', null=True, blank=True)
    

    def __str__(self):
        return f"{self.name} - {self.owner}"
    
class Visit(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

    def __str__(self):
        return f"Visita de {self.pet.name} el {self.date.strftime('%d/%m/%Y')}"

class Toy(models.Model):
    toy = models.CharField(max_length=100)
    description = models.TextField()
    pet = models.ManyToManyField(Pet, blank=True)

    def __str__(self):
        return self.toy