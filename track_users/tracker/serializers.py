from tracker.models import *
from rest_framework import serializers
from datetime import datetime


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    activity_periods = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id', 'real_name', 'tz', 'activity_periods']

    def get_id(self, userprofile_obj):
        return userprofile_obj.user_id

    def get_activity_periods(self, userprofile_obj):
        activity_periods = ActivityPeriod.objects.filter(user_id=userprofile_obj.id)
        activity_period_list = []
        if activity_periods.exists():
            for activity in activity_periods:
                activity_period_list.append({
                    "start_time": datetime.strftime(activity.start_time, "%b %-d %Y %-H:%M%p"),
                    "end_time": datetime.strftime(activity.end_time, "%b %-d %Y %-H:%M%p")
                })
        return activity_period_list
