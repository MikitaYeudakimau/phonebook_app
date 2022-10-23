# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from . import serializers
from .models import Person

# @csrf_exempt
# def person_list(request):
#     if request.method == "GET":
#         persons = Person.objects.all()
#         serializer = serializers.PersonSerializer(persons, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == "POST":
#         person = request.POST
#         serializer = serializers.PersonSerializer(data=person)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# class PersonListView(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = serializers.PersonSerializer
#
#
# class PersonDetailView(generics.RetrieveAPIView):
#     queryset = Person.objects.all()
#     serializer_class = serializers.PersonSerializer
#
# class PersonUpdateView(generics.UpdateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = serializers.PersonSerializer


class PersonModelViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer
