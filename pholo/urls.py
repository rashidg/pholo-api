from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers

from viewsets import StoreViewSet, TableViewSet, BookViewSet


router = routers.DefaultRouter()
router.register(r'stores', StoreViewSet)
router.register(r'stores/(?P<store_id>[0-9]+)/tables', TableViewSet, base_name='tables')

router.register(r'book', BookViewSet, base_name='book')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^', include(router.urls))
]


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]