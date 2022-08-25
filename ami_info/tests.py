import datetime
from django.utils import timezone
from django.test import TestCase, Client
from .models import Ami, Update
from django.views import generic
from django.urls import reverse

# Lots of work to be done here..

class AmiModelTests(TestCase):
    #Testing default values - AMI date is default to now, end of life 60 days from then
    def test_near_end_of_life(self):
        ami = Ami(ami_name="test_ami", ami_id="ami-4ddcf436",platform="CentOS")
        self.assertIs(ami.near_end_life(), False)
    def test_near_end_of_life_10_days(self):
        ami = Ami(ami_name="test_ami", ami_id="ami-4ddcf436",platform="CentOS", end_of_life_date=timezone.now() + datetime.timedelta(days=10))
        self.assertIs(ami.near_end_life(), True)
    def test_ami_id_not_repeated(self):


'''
GOING TO COME BACK TO TESTING EVENTUALLY, RUNNING OUT OF TIME THIS SPRINT
class IndexViewTests(generic.ListView, self):
    def test_index_page(self):
        ami = Ami(ami_name="test_ami", ami_id="ami-4ddcf436",platform="CentOS")
        response = self.client.get(reverse('ami_info'))
        self.assertQuerySetEqual(
            response.context['ami_listing'], ['<Ami: ami-4ddcf436']
        )
'''
