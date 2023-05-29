from rest_framework.views import APIView
from api.models import MyModel
from api.serializers import MySerializer
from rest_framework.response import Response
import requests
import json
# Create your views here.


class MyApiView(APIView):
#         def get(self, request, postId=None):
#             url ='https://jsonplaceholder.typicode.com/comments'
#             if postId is not None:
#                 params = {'postId': postId}
#             else:
#                 params = {}
#             params = {'postId': postId}
#             response = requests.get(url, params=params)
#
#             if response.status_code == 200:
#                 data = response.json()
#                 # Process the data as needed
#                 # Return a response or render a template with the data
#             else:
#                 # Handle the case when the request fails
#                 data = []
#
#             return Response(data)


    def post(self, request):
        try:
            url = 'https://jsonplaceholder.typicode.com/posts/1'
            # payload = {'id': id}
            data = request.data
            print(data)
            print(json.dumps(data))

            response = requests.put(url, data=json.dumps(data))
            print(response)
            print(response.status_code)

            if response.status_code == 200:
                print(data)
                print("=============================")
                print(response.json())

                data = response.json()
                print(data)
                # Process the data as needed
                # Return a response or render a template with the data
            else:
                # Handle the case when the request fails
                data = []

            return Response(data)
        except Exception as exception:
            print(exception)

        # def put(self, request):
        #     url = 'https://jsonplaceholder.typicode.com/posts'
        #     data = request.data  # Retrieve the data from the request body
        #     headers = {
        #         'Content-type': 'application/json; charset=UTF-8'
        #     }
        #
        #     response = requests.put(url, data=json.dumps(data), headers=headers)
        #     json_response = response.json()
        #
        #     return Response(json_response)




