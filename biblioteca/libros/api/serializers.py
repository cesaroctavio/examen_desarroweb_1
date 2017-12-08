from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from libros.models import  libro

class LibroModelSerializer(serializers.ModelSerializer):
    #user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = libro
        fields = [

            'titulo',
            'autor',
            'editorial',
            'ISBN',
            'precio',
            'creado',
            'date_display',
            'timesince',
            'id'
        ]

    def get_date_display(self, obj):
        return obj.creado.strftime("%b %d %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.creado) + " ago"
