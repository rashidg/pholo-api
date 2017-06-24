from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


#Models
from models import Store, Table

admin.site.register(Store)
admin.site.register(Table)

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'desc')

class TableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Table
		fields = ('number', 'status', 'store')

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

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'stores', StoreViewSet)
router.register(r'stores/(?P<store_id>[0-9]+)/tables', TableViewSet, base_name='tables')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls))
]


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]