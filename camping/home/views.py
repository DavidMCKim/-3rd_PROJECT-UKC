from django.shortcuts import render
from .models import CampingPlace, ReviewUkc
from . import Hybrid, gyojiphap,check_id
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        ID = request.user
        check = check_id.check(str(ID))
        check_in_csv = check_id.check_in_csv(str(ID))
        if check == 'exist':
            if check_in_csv == 'data exist':
                best, only_by_contents ,only_by_items = Hybrid.review_filter(str(ID))
                context = ({'check':check,'best':best, 'only_by_contents':only_by_contents, 'only_by_items':only_by_items})
            else:
                context = ({'check':'none'})
            return render(request, 'UKC/index.html', context)
        elif check == 'none':
            context = ({'check': check})
            return render(request, 'UKC/index.html',context)
    else:
        return render(request,  'UKC/index.html')

def find_tag(request):
    if request.method == 'GET':
        values = request.GET.getlist('m_tab')
        value_list = ''
        for value in values:
            url = 'm_tab=' + value + '&'
            value_list += url

        df_dict_final = gyojiphap.intersection(values)

        paginator = Paginator(df_dict_final, 6)
        page_number=request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = ({'value_list':value_list,'a':page_obj,'df_dict_final':df_dict_final})

    return render(request, "UKC/find_tag.html", context)

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

def select_favorite(request):
    if request.method == 'GET':
        pass
    return render(request, 'accounts/select_favorite.html')
