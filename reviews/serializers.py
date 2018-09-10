from reviews.models import Review, RATING_CHOICES, COMPANY_TYPE_CHOICES
from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from datetime import datetime

class ReviewListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = (
        'id', 'url', 'company_name', 'company_type',
        'first_name', 'last_name', 'comment',
        'rating', 'pub_date'
        )


class CompanyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
        'id', 'company_type', 'company_name',
        'first_name', 'last_name', 'rating',
        'comment', 'pub_date'
        )

class ReviewSerializer(serializers.Serializer):
    company_type = serializers.ChoiceField(choices=COMPANY_TYPE_CHOICES)
    company_name= serializers.CharField(max_length=50)
    first_name = serializers.CharField(required= False, allow_blank=True, max_length=50)
    last_name = serializers.CharField(required= False, allow_blank=True, max_length=50)
    rating = serializers.ChoiceField(choices=RATING_CHOICES, default='three_stars')
    comment = serializers.CharField(required=False, allow_blank=True, max_length=500)
    pub_date = serializers.models.DateTimeField(auto_now=True)

    def create(self,validated_data):
        return Review.objects.create(**validated_data)

    def update(self,validated_data):
        instance.comapny_type = validated_data.get('company_type', instance.company_type)
        instance.first_nam = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.rating = validated_data.get('rating', instance.rating)
        instanct.save()
        return instance
