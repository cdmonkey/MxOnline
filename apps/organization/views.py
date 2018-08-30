from django.shortcuts import render
from django.views.generic.base import View

from .models import *

from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class OrgListView(View):
    def get(self, request):
        all_org = CourseOrg.objects.all()
        all_city = City.objects.all()
        org_num = all_org.count()
        # 城市筛选
        city_id = request.GET.get("city", "")
        if city_id:
            all_org = all_org.filter(city_id=int(city_id))
        #类别筛选
        category = request.GET.get("ct", "")
        if category:
            all_org = all_org.filter(category=category)

        # 对课程机构页面进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_org, per_page=3, request=request)
        orgs = p.page(page)
        return render(request, 'org-list.html', {
            'all_org': orgs,
            'all_city': all_city,
            'org_num': org_num,
            'city_id': city_id,
            'category': category
        })

