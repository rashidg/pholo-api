from rest_framework import generics, mixins, views, status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from models import Booking
from serializers import BookingSerializer


class BookView(views.APIView):
	permission_classes = []

	def get(self, request, *args, **kwargs):
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
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	def get_object(self):
		return Booking.objects.filter(active=True,user=self.request._user).first()
		#return Booking.objects.get(active=True,user=self.request._user)
