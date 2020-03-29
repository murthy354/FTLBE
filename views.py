from django.shortcuts import render
from rest_framework.views import APIView
from .models import Members,ActivityPeriods
from rest_framework.response import Response
# Create your views here.


class MembersView(APIView):
    def get(self, request):
        final_result = {}
        members_list = []
        for member in Members.objects.all():
            members_dic = {}
            members_dic['id'] = member.identity
            members_dic['real_name'] = member.real_name
            members_dic['tz'] = member.tz
            activity_periods_list = []
            for activity_period in ActivityPeriods.objects.filter(activity_periods=member):
                activity_periods_dic = {}
                activity_periods_dic['start_time'] = activity_period.start_time
                activity_periods_dic['end_time'] = activity_period.end_time
                activity_periods_list.append(activity_periods_dic)
            members_dic['activity_periods'] = activity_periods_list
            members_list.append(members_dic)

        final_result['ok'] = True
        final_result["members"] = members_list
        return Response(final_result)

