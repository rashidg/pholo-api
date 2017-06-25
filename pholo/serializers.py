from rest_framework import serializers

from models import Store, Table


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'desc')


class TableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Table
		fields = ('number', 'status', 'store')
