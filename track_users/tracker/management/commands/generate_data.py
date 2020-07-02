import pytz
import string
import random
import names
from random import randrange
from faker import Faker
from tracker.models import *
from django.utils.timezone import make_aware
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--user_count', type=int, help="UserCount")
        parser.add_argument('--max_activity_entries', type=int,
                            help="Eg, If 5 is given random number from 0 to 5 will be taken, and that much activity period entries will be added")

    def handle(self, *args, **options):
        user_count = options['user_count']
        max_entries = options['max_activity_entries']
        if not user_count or not max_entries:
            raise CommandError('Enter both UserCount and Max Activity Period Entry')
        timezones = pytz.all_timezones
        for idx in range(0, user_count):
            user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
            user_obj, is_created = UserProfile.objects.get_or_create(user_id=user_id)
            if is_created:
                user_obj.real_name = names.get_full_name()
                user_obj.tz = timezones[randrange(len(timezones))]
            user_obj.save()
            no_of_activity_periods = random.randint(0, max_entries)
            fake = Faker()
            for idx in range(0, no_of_activity_periods):
                start_time = make_aware(fake.date_time())
                end_time = make_aware(fake.date_time())
                if start_time > end_time:
                    (start_time, end_time) = (end_time, start_time)
                ActivityPeriod.objects.create(user=user_obj, start_time=start_time, end_time=end_time)
        print("*-- Completed --*")
