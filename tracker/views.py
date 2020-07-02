import json
from django.shortcuts import render
from django.http import HttpResponse
from tracker.models import *
from tracker.serializers import *


def home_page(request):
    return HttpResponse(
        '''
        <h1>
        Hi, This is FTL User Tracker.
        <br/>
        To Check API Response, <a href="/users_list/"> Click here </a>.
        <br/>
        For more details <a target="_blank" href="https://github.com/Sehanshah/FTL_user_tracker"> Click here </a>.
        <br/>
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
