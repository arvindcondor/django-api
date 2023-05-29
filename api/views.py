from rest_framework.views import APIView
from api.models import MyModel
from api.serializers import MySerializer
from rest_framework.response import Response
import requests
# Create your views here.


class MyApiView(APIView):
        def get(self, request, postId=None):
            url ='https://jsonplaceholder.typicode.com/comments'
            if postId is not None:
                params = {'postId': postId}
            else:
                params = {}
            params = {'postId': postId}
            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                # Process the data as needed
                # Return a response or render a template with the data
            else:
                # Handle the case when the request fails
                data = []

            return Response(data)






