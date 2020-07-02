import json
from django.shortcuts import render
from django.http import HttpResponse
from tracker.models import *
from tracker.serializers import *


def home_page(request):
    return HttpResponse('Hi')


def users_list(request):
    users = UserProfile.objects.all()
    serializer = UserProfileSerializer(users, many=True)
    response_data = {
        "ok": True,
        "members": serializer.data
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
