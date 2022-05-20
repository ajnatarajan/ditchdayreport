from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User, Report
from .serializers import UserSerializer, ReportSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def user_list(request, format=None):
    '''
    Get list of users (people who can be reported)
    '''
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def user_detail(request, pk, format=None):
    '''
    Perform actions on individual users (people who can be reported)

    GET: gets user
    POST: adds a new user
    DELETE: removes a user
    '''
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response("User {} does not exist".format(pk), status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(data=request.data)
        bob = "oi levi"
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def report_list(request, first_name="", last_name="", format=None):
    '''
    Get list of all reports for all users
    '''
    if request.method == 'GET':
        if first_name and last_name:
            try:
                user_id = User.objects.filter(
                    first_name=first_name, last_name=last_name)[0].id
                report = Report.objects.filter(user=user_id)
            except Report.DoesNotExist:
                return Response('User {} {} has no reports'.format(first_name, last_name), status=status.HTTP_404_NOT_FOUND)
        else:
            report = Report.objects.all()
        serializer = ReportSerializer(report, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        first, last = request.data['player'].split(" ")
        user_id = User.objects.filter(
            first_name=first, last_name=last)[0].id
        formatted_data = {
            "report_text": request.data['report_reason'],
            "negative_attitude_opt": request.data['is_negative_attitude'],
            "trolling_opt": request.data['is_trolling'],
            "verbal_abuse_opt": request.data['is_verbal_abuse'],
            "unskilled_player_opt": request.data['is_unskilled_player'],
            "is_andy_tong_opt": request.data['is_is_andy_tong'],
            "user": user_id
        }
        serializer = ReportSerializer(data=formatted_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
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
    elif request.method == 'PUT':
        first_name, last_name = request.data['player'].split(" ")
        user_id = User.objects.filter(
            first_name=first_name, last_name=last_name)[0].id
        formatted_data = {
            "report_text": request.data['report_reason'],
            "negative_attitude_opt": request.data['is_negative_attitude'],
            "trolling_opt": request.data['is_trolling'],
            "verbal_abuse_opt": request.data['is_verbal_abuse'],
            "unskilled_player_opt": request.data['is_unskilled_player'],
            "is_andy_tong_opt": request.data['is_is_andy_tong'],
            "user": user_id
        }
        serializer = ReportSerializer(data=formatted_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
