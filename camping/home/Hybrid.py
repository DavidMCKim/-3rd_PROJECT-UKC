import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
import pymysql

# # 실제 구현할때 쓸 example
# ID = 'id4151' # 추천 대상
# title_name = '럭셔리글램핑 W 풀빌라' # 제일 최근에 방문한 캠핑장


### 콘텐츠 기반 추천 시스템 ###
def recomm_campings_by_contents(title_name):
    genre_sim_sorted_ind = np.load('home/genre_sim_sorted_ind.npy')
    df = pd.read_csv('home/camping_contents.csv')
    # 인자로 전달된 title에 해당되는 데이터 추출
    title_camp = df[df['Name'] == title_name]

    # title_named을 가진 DataFrame의 index 객체를 ndarray로 반환하고
    # sorted_ind 인자로 입력된 genre_sim_sorted_ind 객체에서
    # 유사도 순으로 top_n 개의 index 추출
    title_index = title_camp.index.values
    similar_indexes = genre_sim_sorted_ind[title_index, 1:10]

    # 추출된 top_n index들 출력. top_n index는 2차원 데이터 임.
    # dataframe에서 index로 사용하기 위해서 1차원 array로 변경
    similar_indexes = similar_indexes.reshape(-1)

    # index에 해당되는 데이터프레임 반환
    return df.iloc[similar_indexes]['Name'].tolist()

### 아이텝 기반 협업 필터링 시스템 ###
def recomm_campings_by_items(ID):
    ratings_pred_matrix = pd.read_csv('home/ratings_pred_matrix.csv')
    ratings_matrix = pd.read_csv('home/ratings_matrix.csv')
    ratings_pred_matrix.set_index('ID', inplace=True)
    ratings_matrix.set_index('ID', inplace=True)

    # ID로 입력받은 사용자의 모든 캠핑장 정보를 추출해 Series로 반환
    # 반환된 user_rating은 캠핑장(Name)을 인덱스로 가지는 Series 객체임
    user_rating = ratings_matrix.loc[ID, :]

    # user_rating이 0보다 크면 기존에 간 캠핑장임. 대상 인덱스를 추출해 list객체로 만듬
    already_gone = user_rating[user_rating > 0].index.tolist()

    # 모든 캠핑장을 list객체로 만듦
    camping_list = ratings_matrix.columns.tolist()

    # list comprehension으로 already_gone에 해당하는 캠핑장는 camping_list에서 제외함
    ungone_list = [camping for camping in camping_list if camping not in already_gone]

    recomm_campings = ratings_pred_matrix.loc[ID, ungone_list].sort_values(ascending=False)[:10].index.tolist()
    return recomm_campings

### 하이브리드 추천시스템 ###
def hybrid_recomm_system(ID,title_name):
    best = list(set(recomm_campings_by_items(ID)) & set(recomm_campings_by_contents(title_name)))[:3]
    only_by_contents = list(set(recomm_campings_by_contents(title_name))-set(recomm_campings_by_items(ID)))[:3]
    only_by_items = list(set(recomm_campings_by_items(ID))-set(recomm_campings_by_contents(title_name)))[:3]
    return best, only_by_contents, only_by_items

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

def review_filter(ID):
    db = db_conn()
    sql = "select * from REVIEW_UKC WHERE USER_ID = '" + ID + "' and RATING > 3 ORDER BY DATE DESC LIMIT 1"  #최근 데이터부터 19일치 데이터 추출
    df = pd.read_sql(sql,db)
    title_name = df['CAMPING_NAME'][0]
    print(title_name)

    best, only_by_contents, only_by_items = hybrid_recomm_system(ID,df['CAMPING_NAME'][0])

    df_best = pd.DataFrame()
    dict_best = {}
    df_dict_best = []

    for i in best:
        sql = "SELECT IMAGE,CAMPING_NAME,ADDRESS,PHONE,INFO,URL FROM CAMPING_PLACE WHERE CAMPING_NAME = '" + i + "'"
        df = pd.read_sql(sql, db)
        df_best = df_best.append(df)
        df_best.index = range(0,len(df_best))

    print(df_best)
        ## DB에 값이 잘못들어가고있는게 있음 확인필요!!!!
    for i in range(0,len(df_best)):
        if df_best.loc[i]['IMAGE'][-1] == '\r' or df_best.loc[i]['IMAGE'][-1] == '\n':
            dict_best = {'image':df_best.loc[i]['IMAGE'][:-1],'name':df_best.loc[i]['CAMPING_NAME'],'address':df_best.loc[i]['ADDRESS'],'phone':df_best.loc[i]['PHONE'],'info':df_best.loc[i]['INFO'],'url':df_best.loc[i]['URL']}
        elif df_best.loc[i]['IMAGE'][-1] == 'i':
            dict_best = {'image':df_best.loc[i]['IMAGE']+'f','name':df_best.loc[i]['CAMPING_NAME'],'address':df_best.loc[i]['ADDRESS'],'phone':df_best.loc[i]['PHONE'],'info':df_best.loc[i]['INFO'],'url':df_best.loc[i]['URL']}
        else:
            dict_best = {'image':df_best.loc[i]['IMAGE'],'name':df_best.loc[i]['CAMPING_NAME'],'address':df_best.loc[i]['ADDRESS'],'phone':df_best.loc[i]['PHONE'],'info':df_best.loc[i]['INFO'],'url':df_best.loc[i]['URL']}
        df_dict_best.append(dict_best)

    df_only_by_contents = pd.DataFrame()
    dict_only_by_contents = {}
    df_dict_only_by_contents = []
    for i in only_by_contents:
        sql = "SELECT IMAGE,CAMPING_NAME,ADDRESS,PHONE,INFO,URL FROM CAMPING_PLACE WHERE CAMPING_NAME = '" + i + "'"
        df = pd.read_sql(sql, db)
        # print(df_image)
        df_only_by_contents = df_only_by_contents.append(df)
        df_only_by_contents.index = range(0,len(df_only_by_contents))
    for i in range(0,len(df_only_by_contents)):
        if df_only_by_contents.loc[i]['IMAGE'][-1] == '\r' or df_only_by_contents.loc[i]['IMAGE'][-1] == '\n':
            dict_only_by_contents = {'image':df_only_by_contents.loc[i]['IMAGE'][:-1],'name':df_only_by_contents.loc[i]['CAMPING_NAME'],'address':df_only_by_contents.loc[i]['ADDRESS'],'phone':df_only_by_contents.loc[i]['PHONE'],'info':df_only_by_contents.loc[i]['INFO'],'url':df_only_by_contents.loc[i]['URL']}
        elif df_only_by_contents.loc[i]['IMAGE'][-1] == 'i':
            dict_only_by_contest = {'image':df_only_by_contents.loc[i]['IMAGE']+'f','name':df_only_by_contents.loc[i]['CAMPING_NAME'],'address':df_only_by_contents.loc[i]['ADDRESS'],'phone':df_only_by_contents.loc[i]['PHONE'],'info':df_only_by_contents.loc[i]['INFO'],'url':df_only_by_contents.loc[i]['URL']}
        else:
            dict_only_by_contents = {'image':df_only_by_contents.loc[i]['IMAGE'],'name':df_only_by_contents.loc[i]['CAMPING_NAME'],'address':df_only_by_contents.loc[i]['ADDRESS'],'phone':df_only_by_contents.loc[i]['PHONE'],'info':df_only_by_contents.loc[i]['INFO'],'url':df_only_by_contents.loc[i]['URL']}
        df_dict_only_by_contents.append(dict_only_by_contents)
    # print(df_dict_only_by_contents[0]['image'])

    df_only_by_items = pd.DataFrame()
    dict_only_by_items = {}
    df_dict_only_by_items = []
    for i in only_by_items:
        sql = "SELECT IMAGE,CAMPING_NAME,ADDRESS,PHONE,INFO,URL FROM CAMPING_PLACE WHERE CAMPING_NAME = '" + i + "'"
        df = pd.read_sql(sql, db)
        df_only_by_items = df_only_by_items.append(df)
        df_only_by_items.index = range(0,len(df_only_by_items))
        # print(df_only_by_items)
    for i in range(0,len(only_by_items)):
        if df_only_by_items.loc[i]['IMAGE'][-1] == '\r' or df_only_by_items.loc[i]['IMAGE'][-1] == '\n':
            dict_only_by_items = {'image':df_only_by_items.loc[i]['IMAGE'][:-1],'name':df_only_by_items.loc[i]['CAMPING_NAME'],'address':df_only_by_items.loc[i]['ADDRESS'],'phone':df_only_by_items.loc[i]['PHONE'],'info':df_only_by_items.loc[i]['INFO'],'url':df_only_by_items.loc[i]['URL']}
        elif df_only_by_items.loc[i]['IMAGE'][-1] == 'i':
            dict_only_by_items = {'image':df_only_by_items.loc[i]['IMAGE']+'f','name':df_only_by_items.loc[i]['CAMPING_NAME'],'address':df_only_by_items.loc[i]['ADDRESS'],'phone':df_only_by_items.loc[i]['PHONE'],'info':df_only_by_items.loc[i]['INFO'],'url':df_only_by_items.loc[i]['URL']}
        else:
            dict_only_by_items = {'image':df_only_by_items.loc[i]['IMAGE'],'name':df_only_by_items.loc[i]['CAMPING_NAME'],'address':df_only_by_items.loc[i]['ADDRESS'],'phone':df_only_by_items.loc[i]['PHONE'],'info':df_only_by_items.loc[i]['INFO'],'url':df_only_by_items.loc[i]['URL']}
        df_dict_only_by_items.append(dict_only_by_items)
        print(df_dict_only_by_items[0]['image'])

    return df_dict_best, df_dict_only_by_contents, df_dict_only_by_items


