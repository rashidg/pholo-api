from rest_framework import viewsets

from models import Store, Table
from serializers import StoreSerializer, TableSerializer


class StoreViewSet(viewsets.ModelViewSet):
	queryset = Store.objects.all()
	serializer_class = StoreSerializer

class TableViewSet(viewsets.ModelViewSet):
	serializer_class = TableSerializer

	def get_queryset(self):
		store_id = self.kwargs.get('store_id')
		return Table.objects.filter(store=store_id)

	def create(self, request, *args, **kwargs):
		request.data.update({
			"store": kwargs.get('store_id', 1)
		})
		return super(TableViewSet, self).create(request, *args, **kwargs)
