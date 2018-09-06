from rest_framework import serializers
from company.models import CompanyByType, COMPANY_TYPE_CHOICES, CompanyLocation, CompanyContacts
from rest_framework.serializers import ModelSerializer

class CompanyContactsRetriSerializer(ModelSerializer):
    class Meta:
        model = CompanyContacts
        fields = [
        'company_name',
        'company_twitter',
        'company_facebook',
        'company_instagram',
        'company_email',
        'slug'
        ]
class CompanyContactsListSerializer(ModelSerializer):
    class Meta:
        model = CompanyContacts
        fields = [
        'company_name',
        'company_twitter',
        'company_facebook',
        'company_instagram',
        'company_email',
        'slug'
        ]
class CompanyContactsDetailSerializer(ModelSerializer):
    class Meta:
        model = CompanyContacts
        fields = [
        'company_name',
        'company_twitter',
        'company_facebook',
        'company_instagram',
        'company_email',
        'slug'
        ]

class CompanyByTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company_name = serializers.CharField(required= False, allow_blank=True, max_length=50)
    company_type = serializers.ChoiceField(choices=COMPANY_TYPE_CHOICES, default='other')

    def create(self,validated_data):
        return CompanyByType.objects.create(**validated_data)
    def update(self,validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.company_type = validated_data.get('company_type', instance.company_type)
        return instance

class CompanyContactsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company_name = serializers.CharField(required= False, allow_blank=True, max_length=50)
    company_twitter = serializers.CharField(required=False, allow_blank=True, max_length=50)
    company_facebook = serializers.CharField(allow_blank=True, required=False, max_length=50)
    company_instagram = serializers.CharField(allow_blank=True, required=False, max_length=50)
    company_email = serializers.EmailField(allow_blank=True, required=False, max_length=50)

    def create(self,validated_data):
        return CompanyContacts.objects.create(**validated_data)

    def update(self,validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.company_twitter = validated_data.get('company_twitter', instance.company_twitter)
        instance.company_facebook = validated_data.get('company_facebook', instance.company_facebook)
        instance.company_instagram = validated_data.get('company_instagram', instance.company_instagram)
        instance.company_email = validated_data.get('company_email', instance.company_email)
        instance.save()
        return instance

class CompanyLocationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company_name = serializers.CharField(max_length=50)
    street_address = serializers.CharField(allow_blank=True, max_length=50)
    city = serializers.CharField(allow_blank=True, max_length=25)
    state = serializers.CharField(allow_blank=True, max_length=25)
    zip_code = serializers.IntegerField(required=False)
    comp_longitude = serializers.DecimalField(required=False, max_digits=9, decimal_places=6)
    comp_latitude = serializers.DecimalField(required=False, max_digits=9, decimal_places=6)

    def create(self,validated_data):
        return CompanyLocation.objects.create(**validated_data)

    def update(self,validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.street_address = validated_data.get('street_address', instance.street_address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.comp_longitude = validated_data.get('comp_longitude', instance.comp_longitude)
        instance.comp_latitude = validated_data.get('comp_latitude', instance.comp_latitude)
        instance.save()
        return instance
