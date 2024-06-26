from rest_framework import viewsets, status
from .models import CustomUser, Parcel, DeliveryProof
from .serializers import *
from rest_framework.response import Response 

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status= status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
       



class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


class DeliveryProofViewSet(viewsets.ModelViewSet):
    queryset = DeliveryProof.objects.all()
    serializer_class = DeliveryProofSerializer