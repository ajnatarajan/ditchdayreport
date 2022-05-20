from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User, Report
from .serializers import UserSerializer, ReportSerializer

# Create your views here.


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def user_list(request, format=None):
    '''
    Get list of users (people who can be reported)
    '''
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def user_detail(request, pk, format=None):
    '''
    Perform actions on individual users (people who can be reported)

    GET: gets user
    POST: adds a new user
    DELET: removes a user
    '''
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response("User {} does not exist".format(pk), status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def report_list(request, user_id=None, format=None):
    '''
    Get list of all reports for all users
    '''
    if request.method == 'GET':
        if user_id:
            try:
                report = Report.objects.get(user=user_id)
            except Report.DoesNotExist:
                return Response('User {} has no reports'.format(user_id), status=status.HTTP_404_NOT_FOUND)
        else:
            report = Report.objects.all()
        serializer = ReportSerializer(report, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def report_detail(request, pk, format=None):
    '''
    Perform actions on individual reports given a report id
    '''
    try:
        report = Report.objects.get(pk=pk)
    except Report.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReportSerializer(report)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
