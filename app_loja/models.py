from django.db import models

class Categoria(models.Model):
    title = models.CharField(max_length=20)


    def __str__(self):
        return self.title

class Produtos(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.title