from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from user_data.models import user_data
from .serializers import User_dataSerializer #capital U hobenaki sure na

class user_dataListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated | HasAPIKey]


    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        #todos = Todo.objects.filter(user = request.user.id)
        user_data_all = user_data.objects.all()
        serializer = User_dataSerializer(user_data_all, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'device_id': request.data.get('device_id'),
            'temp': request.data.get('temp'),
            'bp_systolic': request.data.get('bp_systolic'),
            'bp_diastolic': request.data.get('bp_diastolic'),
            'hr': request.data.get('hr'),
            'spo2': request.data.get('spo2')

        }
        serializer = User_dataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)