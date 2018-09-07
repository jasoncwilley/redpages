from reviews.models import Review, CompanyReviews, RATING_CHOICES
from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

class CompanyReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyReviews
        fields = (
        'id', 'company_name'
        )

class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    companyreviews = serializers.CharField(max_length=50)
    first_name = serializers.CharField(required= False, allow_blank=True, max_length=50)
    last_name = serializers.CharField(required= False, allow_blank=True, max_length=50)
    rating = serializers.ChoiceField(choices=RATING_CHOICES, default='three_stars')
    comment = serializers.CharField(required=False, allow_blank=True, max_length=500)
    pub_date = serializers.DateTimeField(required=False)

    def create(self,validated_data):
        return CompanyByType.objects.create(**validated_data)

    def update(self,validated_data):
        instance.first_nam = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.companyreviews = validated_data.get('companyreviews', instance.companyreviews)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.rating = validated_data.get('rating', instance.rating)
        instanct.save()
        return instance
