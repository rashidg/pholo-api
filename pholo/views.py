from rest_framework import generics, mixins, views, status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from models import Booking
from serializers import BookingSerializer


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
