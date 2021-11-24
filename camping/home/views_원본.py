from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import CampingPlace, ReviewUkc
from . import recommendation_code


# Create your views here.
def home(request):
    images=[]
    reviews = ReviewUkc.objects.all()
    name = reviews[len(reviews)-1].camping_name
    camping = CampingPlace.objects.all()
    context_list = []
    recommend_items = recommendation_code.test(name)
    for j in recommend_items:
        for camp in camping:
            if camp.name == j:
                images.append(str(camp.images.replace('\r','').replace("'",'')))
                context_list.append(zip(j,images))
    print(images)
    print(context_list)

    context = ({'context_list': context_list})
    return render(request, 'UKC/index.html', context)

# def find_tag(request):
#     a = CampingPlace.objects.all()
#
#     return render(request, "UKC/find_tag.html" ,{'a':a})

def find_tag(request):
    value = request.GET.getlist('m_tab')

    if len(value) >=4 :
        value = request.GET.getlist('m_tab')[:3]

    camping_place_info = CampingPlace.objects.all()
    infos = []
    num = []
    n=1
    for x in range(len(camping_place_info)):
        try:
            if value[0] in camping_place_info[x].info2.split(' '):
                if value[1] in camping_place_info[x].info2.split(' '):
                    if value[2] in camping_place_info[x].info2.split(' '):
                        infos.append(camping_place_info[x])
                        num.append(n)
                        n+=1
        except:
            pass

    print(infos)
    context = {'infos': infos,'value':value,'num':num}
    return render(request,"UKC/find_tag.html", context)


def site(request):
    return render(request, 'UKC/site.html')

def review(request):
    if request.method == 'POST':

        ## 리뷰작성 시 REVIEWUKC 테이블에 저장
        username = request.POST.get('username')
        campingname = request.POST.get('campingname')
        rating = request.POST.get('rating')
        review = request.POST.get('review')

        db = ReviewUkc()
        db.user_id = request.POST.get('username')
        db.camping_name = request.POST.get('campingname')
        db.rating = request.POST.get('rating')
        db.review = request.POST.get('review')
        db.date = request.POST.get('camping_date')
        db.save()

    return render(request, 'UKC/review.html')