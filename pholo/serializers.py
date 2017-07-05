from rest_framework import serializers

from models import Store, Table, Booking, Product, Request


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


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'store')


class RequestSerializer(serializers.ModelSerializer):
	product = serializers.CharField(source='get_product_name', read_only=True)
	table = serializers.IntegerField(read_only=True)
	class Meta:
		model = Request
		fields = ('id', 'product', 'table')
