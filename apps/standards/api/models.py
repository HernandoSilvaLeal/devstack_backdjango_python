from email import charset
from django.db import models
from apps.base.models import BaseModel

# Parte 0: Importaciones necesarias para las relaciones entre modelos.
# Parte 1: Model ---> El nombre del modelo (Tabla o Entidad)
# Parte 2: BaseModel ---> Modelo que hereda los campos del modelo base (Pk y demas)
# Parte 3: Campos ---> Los fijados en el modelo MER (Atributos)
# Parte 4: Clase Meta + Orderin --->  Definicion en los metadatos (Nombre del modelo)
# Parte 5: Funcion __str__ ---> Representacion en Unicode
# Parte 6: Funciones adicionales @

# 7.1 StandardsModel
class StandardsModel(BaseModel):

    title_standard = models.CharField('Titulo de la Documentacion', max_length=50)
    version_standard = models.DecimalField('Version', max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'StandardsModel'
        verbose_name_plural = 'StandardsModels'

    def __str__(self):
        return self.name


# 7.2 ChaptersModel
class ChaptersModel(StandardsModel):

    title_chapter = models.CharField('Titulo del Capitulo', max_length=50)
    description_chapter = models.CharField('Descripcion', max_length=200)
    image_chapter = models.ImageField('Imagen', upload_to='standards/', blank=True, null=True)
    link_chapter = models.CharField(max_length=100, default='', null=True, blank=True)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'ChaptersModel'
        verbose_name_plural = 'ChaptersModels'

    def __str__(self):
        return self.name


# 7.3 ArticlesModel
class ArticlesModel(ChaptersModel):

    title_article = models.CharField('Titulo del Capitulo', max_length=50)
    description_article = models.CharField('Descripcion', max_length=200)
    image_article = models.ImageField('Imagen', upload_to='standards/', blank=True, null=True)
    link_article = models.CharField(max_length=100, default='', null=True, blank=True)

    class Meta:
        ordering = ['-id']                                                                              # Orden descendente o ascendente        
        verbose_name = 'ArticlesModel'
        verbose_name_plural = 'ArticlesModels'

    def __str__(self):
        return self.name



