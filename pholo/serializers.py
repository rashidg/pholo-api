from rest_framework import serializers

from models import Store, Table, Booking


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'desc')


class TableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Table
		fields = ('id', 'number', 'status', 'store')


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ('id', 'table', 'user')

	def create(self, validated_data):
		validated_data.update({
			"user": self.context['request'].user
		})
		return super(BookingSerializer, self).create(validated_data)
