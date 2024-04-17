# views.py
import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import NotFound

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        
        try:
            return queryset.get(account_id=pk)
        except Account.DoesNotExist:
            raise NotFound(f"Account with ID '{pk}' not found.")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Account deleted successfully"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

    @action(detail=True, methods=['get'])
    def destinations(self, request, pk=None):
        account = self.get_object()
        destinations = account.destinations.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get_object(self):
        queryset = self.get_queryset()
        account_id = self.kwargs.get('pk')
        try:
            return queryset.filter(account__account_id=account_id).first()
        except Destination.DoesNotExist:
            raise NotFound(f"Destination with account ID '{account_id}' not found.")
    def perform_create(self, serializer):
        account_id = self.request.data.get('account')
        account = Account.objects.get(account_id=account_id)
        serializer.save(account=account)
@api_view(['POST'])
def incoming_data(request):
    app_secret_token = request.headers.get('CL-X-TOKEN')
    if not app_secret_token:
        return Response({"message": "UnAuthenticated"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        account = Account.objects.get(app_secret_token=app_secret_token)
    except Account.DoesNotExist:
        return Response({"message": "UnAuthenticated"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET' and not request.data:
        return Response({"message": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)

    destinations = account.destinations.all()
    print(destinations)
    for destination in destinations:
        headers = destination.headers
        url = destination.url
        method = destination.http_method.upper()

        if method == 'GET':
            params = request.data
            response = requests.get(url, headers=headers, params=params)
        else:
            data = request.data
            if method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data)

        # Handle response as needed

    return Response({"message": "Data sent successfully"}, status=status.HTTP_200_OK)