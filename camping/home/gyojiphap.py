import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
import pymysql

def db_conn():
    # db 연결 함수
    db = pymysql.connect(
        host='localhost',  # MySQL Server Address
        port=3306,  # MySQL Server Port
        user='root',  # MySQL username
        passwd='1234',  # password for MySQL username
        db='camping',  # Database name
        charset='utf8'
    )
    return db

def intersection(values):
    df = pd.read_csv('home/1109_onehotencoding.csv')
    df_new = df[values]
    sum = pd.DataFrame(df_new.sum(axis=1)).rename(columns={0:'row_sum'}).astype('int')
    sum = sum.sort_values('row_sum',ascending=False)[:20]
    index = sum.index.tolist()
    df_final = pd.DataFrame()
    for i in index:
        df_final = df_final.append(df.loc[i])

    name = df_final['Name'].tolist()
    db = db_conn()
    df_final = pd.DataFrame()
    df_dict_final = []
    for i in name:
        sql = "SELECT IMAGE,CAMPING_NAME,ADDRESS,PHONE,INFO,URL FROM CAMPING_PLACE WHERE CAMPING_NAME = '" + i + "'"
        df = pd.read_sql(sql, db)
        df_final = df_final.append(df)
        df_final.index = range(0,len(df_final))
    for i in range(0,len(df_final)):
        if df_final.loc[i]['IMAGE'][-1] == '\r':
            dict_final = {'image':df_final.loc[i]['IMAGE'][:-1],'name':df_final.loc[i]['CAMPING_NAME'],'address':df_final.loc[i]['ADDRESS'],'phone':df_final.loc[i]['PHONE'],'info':df_final.loc[i]['INFO'],'url':df_final.loc[i]['URL']}
        elif df_final.loc[i]['IMAGE'][-1] == 'i':
            dict_final = {'image':df_final.loc[i]['IMAGE']+'f','name':df_final.loc[i]['CAMPING_NAME'],'address':df_final.loc[i]['ADDRESS'],'phone':df_final.loc[i]['PHONE'],'info':df_final.loc[i]['INFO'],'url':df_final.loc[i]['URL']}
        elif df_final.loc[i]['IMAGE'][-1] == '\n':
            dict_final = {'image':df_final.loc[i]['IMAGE'][:-1],'name':df_final.loc[i]['CAMPING_NAME'],'address':df_final.loc[i]['ADDRESS'],'phone':df_final.loc[i]['PHONE'],'info':df_final.loc[i]['INFO'],'url':df_final.loc[i]['URL']}
        else:
            dict_final = {'image':df_final.loc[i]['IMAGE'],'name':df_final.loc[i]['CAMPING_NAME'],'address':df_final.loc[i]['ADDRESS'],'phone':df_final.loc[i]['PHONE'],'info':df_final.loc[i]['INFO'],'url':df_final.loc[i]['URL']}
        df_dict_final.append(dict_final)

    return df_dict_final

# values = ['가족','아이','물멍']
# intersection(values)



# def find_tag(request):
#     if request.method == 'GET':
#         values = request.GET.getlist('m_tab')
#         value_list = ''
#         for value in values:
#             url = 'm_tab=' + value + '&'
#             value_list += url
#         print(values)
#         camping_place = CampingPlace.objects.all()
#         # print('camping_place : ',camping_place)
#         info_ex = []
#         for i in values:
#             for j in range(len(camping_place)):
#                 try:
#                     if i in camping_place[j].tag.split(' '):
#
#                         if camping_place[j].image[-1] == '\r':
#                             camping_place[j].image = camping_place[j].image[:-1]
#                         info_ex.append(camping_place[j])
#                 except:
#                     pass
#
#         paginator = Paginator(info_ex, 6)
#         page_number=request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context = ({'value_list':value_list,'a':page_obj})
#
#     return render(request, "UKC/find_tag.html", context)
#
# def site(request):
#     return render(request, 'UKC/site.html')
#
# def review(request):
#     if request.method == 'POST':
#
#         ## 리뷰작성 시 REVIEWUKC 테이블에 저장
#         username = request.POST.get('username')
#         campingname = request.POST.get('campingname')
#         rating = request.POST.get('rating')
#         review = request.POST.get('review')
#
#         db = ReviewUkc()
#         db.user_id = request.POST.get('username')
#         db.camping_name = request.POST.get('campingname')
#         db.rating = request.POST.get('rating')
#         db.review = request.POST.get('review')
#         db.date = request.POST.get('camping_date')
#         db.save()
#
#     return render(request, 'UKC/review.html')
