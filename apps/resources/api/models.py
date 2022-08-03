from django.db import models
from apps.base.models import BaseModel

# Parte 0: Importaciones necesarias para las relaciones entre modelos.
# Parte 1: Model ---> El nombre del modelo (Tabla o Entidad)
# Parte 2: BaseModel ---> Modelo que hereda los campos del modelo base (Pk y demas)
# Parte 3: Campos ---> Los fijados en el modelo MER (Atributos)
# Parte 4: Clase Meta + Orderin --->  Definicion en los metadatos (Nombre del modelo)
# Parte 5: Funcion __str__ ---> Representacion en Unicode
# Parte 6: Funciones adicionales @

# 6.1 HelpsModel
class HelpsModel(BaseModel):

    

    class Meta:
        verbose_name = _("HelpsModel")
        verbose_name_plural = _("HelpsModels")

    def __str__(self):
        return self.name


# 6.2 ResourcecategoryModel
class ResourcecategoryModel(BaseModel):

    

    class Meta:
        verbose_name = _("ResourcecategoryModel")
        verbose_name_plural = _("ResourcecategoryModels")

    def __str__(self):
        return self.name


# 6.3 ResourcesModel
class ResourcesModel(BaseModel):

    

    class Meta:
        verbose_name = _("ResourcesModel")
        verbose_name_plural = _("ResourcesModels")

    def __str__(self):
        return self.name

