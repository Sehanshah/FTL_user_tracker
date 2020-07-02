import json
from django.shortcuts import render
from django.http import HttpResponse
from tracker.models import *
from tracker.serializers import *


def home_page(request):
    return HttpResponse(
        '''
        <h1>
        Hi, This is FTL User Tracker. For more details <a href="https://github.com/Sehanshah/FTL_user_tracker"> Click here </a> .
        </h1>
        '''
    )


def users_list(request):
    users = UserProfile.objects.all()
    serializer = UserProfileSerializer(users, many=True)
    response_data = {
        "ok": True,
        "members": serializer.data
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
