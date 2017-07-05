from rest_framework import generics, mixins, views, status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from models import Booking, Product, Request
from serializers import BookingSerializer, ProductSerializer, RequestSerializer


class BookView(views.APIView):
	permission_classes = []

	def already_booked(self):
		qs = Booking.objects.filter(active=True, user=self.request.user)
		return len(qs) > 0

	def get(self, request, *args, **kwargs):
		if self.already_booked():
			return Response({"error": "You booked a table already."},
							 status=status.HTTP_400_BAD_REQUEST)

		data = kwargs
		data.update({ "user": request.user.id })
		serializer = BookingSerializer(data=kwargs)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

	def get_success_headers(self, data):
	    try:
	        return {'Location': data[api_settings.URL_FIELD_NAME]}
	    except (TypeError, KeyError):
	        return {}


class BookingView(generics.RetrieveAPIView):
	permission_classes = []
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	def get_object(self):
		return Booking.objects.get(active=True, user=self.request._user)


class CheckoutView(views.APIView):
	permission_classes = []
	def get(self, request, *args, **kwargs):
		try:
			booking = Booking.objects.get(active=True, user=self.request.user)
		except Booking.DoesNotExist:
			return Response({"error": "You haven't booked a table yet."},
							 status=status.HTTP_400_BAD_REQUEST)
		booking.active = False
		booking.save()
		return Response({"detail": "done"})


class ProductView(generics.ListAPIView):
	permission_classes = []
	serializer_class = ProductSerializer

	def get_queryset(self):
		user = self.request.user
		try:
			booking = Booking.objects.get(active=True, user=self.request.user)
		except Booking.DoesNotExist:
			return []
		store = booking.table.store

		return Product.objects.filter(store=store)


class RequestView(mixins.ListModelMixin, generics.GenericAPIView):
	permission_classes = []
	serializer_class = RequestSerializer

	def create(self, data):
		serializer = RequestSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

	def post(self, request, *args, **kwargs):
		user = request.user
		try:
			booking = Booking.objects.get(active=True, user=user)
		except Booking.DoesNotExist:
			return Response({"error": "You haven't booked a table yet."},
							 status=status.HTTP_400_BAD_REQUEST)

		items = request.data.get('items', [])
		for item in items:
			self.create({"product": item, "booking": booking.id})

		return Response({"detail": "done"})

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def get_queryset(self):
		user = self.request.user
		try:
			booking = Booking.objects.get(active=True, user=user)
		except Booking.DoesNotExist:
			return Response({"error": "You haven't booked a table yet."},
							 status=status.HTTP_400_BAD_REQUEST)

		return Request.objects.filter(booking=booking.id)


class StoreRequestsView(generics.ListAPIView):

	serializer_class = RequestSerializer

	def get_queryset(self):
		store = self.request.user.userprofile.store
		if store is None:
			return []
		return Request.objects.filter(booking__table__store=store)

















