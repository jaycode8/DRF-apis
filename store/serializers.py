
from .models import eBooks, authors, test, test4
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = eBooks
        fields = '__all__'

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = authors
        fields = '__all__'

class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields = '__all__'

class test4Serializer(serializers.ModelSerializer):
    images = testSerializer(many=True)
    class Meta:
        model = test
        fields = '__all__'


