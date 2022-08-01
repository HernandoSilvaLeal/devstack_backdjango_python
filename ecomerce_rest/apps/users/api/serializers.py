from rest_framework import serializers               # Importo los serializers del framework
from apps.users.models import User                   # Importo el modelo que voy a serializar


class UserSerializer(serializers.ModelSerializer):   # Por convencion se le coloca el nombre del modelo al que hace referencia y luego Serializer y hereda de model serializar porque es un MODELO
    class Meta:
        model = User
        # fields = '__all__'                         # Se utiliza fields o exclude, para señalar los campos, para campos especificos usar []
        fields = ['id','password','username','email','name','last_name']


class TestUserSerializer(serializers.Serializer):     # Este es un ejemplo de serializer que no esta basado en un modelo.
    name = serializers.CharField()      # Realizo las validaciones customizadas por campo.
    email = serializers.EmailField()                  # Valida primero el nombre, luego el tipo de dato y luego los atributos

    def validate_name(self,value):                    # Primera validacion por secuencia y nombre de campo
        # Custom Validation
        if 'develop' in value:
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')
        # print(self.context)
        return value

    def validate_email(self,value):                   # Segunda validacion por secuencia y nombre de campo
        # Custom Validation
        if value == '':
            raise serializers.ValidationError('Error, Tiene que indicar un correo')
        
        # print(self.context)
        # print(value)
        if self.context['name'] in self.context.values():             # Antes no aplicaba la excepcion porque faltaba validar los valores de las llaves del dict CONTENIAN a
            raise serializers.ValidationError('Error, El correo no puede contener el nombre!!!!!!!!!!!!!!')   # Esto es una validacion de campos dependendientes

        return value

    def validate(self,data):                          # Tercera validacion general, y predeterminada que aplica el framework a todos los campos.
        print('Validate General')
        return data                                   # Se puede validar por ejemplo que el nombre no se incluya en el correo o la contraseña.


    # def create(self,validated_data):
    #     user = User(**validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
