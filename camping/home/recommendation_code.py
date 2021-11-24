# 장르 유사도에 따라 캠핑장을 추천하는 함수
# 파라미터 : 데이터프레임, 레코드별 장르 코사인 유사도 인덱스, 캠핑장명, 추천할 캠핑장 개수
# 반환 : 추천 캠핑장 정보를 가지는 데이터프레임 반환
import pandas as pd
import numpy as np


# 장르 유사도에 따라 캠핑장을 추천하는 함수
# 파라미터 : 데이터프레임, 레코드별 장르 코사인 유사도 인덱스, 캠핑장명, 추천할 캠핑장 개수
# 반환 : 추천 캠핑장 정보를 가지는 데이터프레임 반환

# def find_sim_camping(df, genre_sim_sorted_ind, title_name, top_n=10):
#     # 인자로 전달된 title에 해당되는 데이터 추출
#     title_camp = df[df['Name'] == title_name]
#
#     # title_named을 가진 DataFrame의 index 객체를 ndarray로 반환하고
#     # sorted_ind 인자로 입력된 genre_sim_sorted_ind 객체에서
#     # 유사도 순으로 top_n 개의 index 추출
#     title_index = title_camp.index.values
#     similar_indexes = genre_sim_sorted_ind[title_index, :(top_n)]
#
#     # 추출된 top_n index들 출력. top_n index는 2차원 데이터 임.
#     # dataframe에서 index로 사용하기 위해서 1차원 array로 변경
#     # print(similar_indexes)
#     similar_indexes = similar_indexes.reshape(-1)
#
#     # index에 해당되는 데이터프레임 반환
#     return df.iloc[similar_indexes]
#
#
# # '난지캠핑장'과 감성이 유사한 캠핑장 10개 추천
# def user_info(df, user_camping, genre_sim_sorted_ind):
#     similar_camp = find_sim_camping(df, genre_sim_sorted_ind, user_camping, 10)
#     print(similar_camp['Name'])
#
#
# def recommendation_by_contents(df, user_camping, genre_sim_sorted_ind):
#     find_sim_camping(df, genre_sim_sorted_ind, user_camping, top_n=10)
#     user_info(df, user_camping, genre_sim_sorted_ind)
#
#
# def test() :
#     genre_sim_sorted_ind = np.load('pred/genre_sim_sorted_ind.npy')
#     df = pd.read_csv('pred/camping_contents.csv')
#     recommendation_by_contents(df,'난지캠핑장', genre_sim_sorted_ind)





# 장르 유사도에 따라 영화를 추천하는 함수
# 파라미터 : 데이터프레임, 레코드별 장르 코사인 유사도 인덱스,
#          영화제목, 추천할 영화 건수
# 반환 : 추천 영화 정보를 가지는 데이터프레임 반환

def find_sim_camping(df, genre_sim_sorted_ind, title_name, top_n=10):
    # 인자로 전달된 title에 해당되는 데이터 추출
    title_camp = df[df['Name'] == title_name]

    # title_named을 가진 DataFrame의 index 객체를 ndarray로 반환하고
    # sorted_ind 인자로 입력된 genre_sim_sorted_ind 객체에서
    # 유사도 순으로 top_n 개의 index 추출
    title_index = title_camp.index.values
    similar_indexes = genre_sim_sorted_ind[title_index, :(top_n)]

    # 추출된 top_n index들 출력. top_n index는 2차원 데이터임
    # dataframe에서 index로 사용하기 위해서 1차원 array로 변경
    # print(similar_indexes)
    similar_indexes = similar_indexes.reshape(-1)

    # index에 해당되는 데이터프레임 반환
    return df.iloc[similar_indexes]

def test(name) :
    genre_sim_sorted_ind = np.load('home/genre_sim_sorted_ind.npy')
    df = pd.read_csv('home/camping_contents.csv')
    similar_camp = find_sim_camping(df, genre_sim_sorted_ind, name)

    return similar_camp['Name']


# 사용자 정보에서 가장 최근에 간 캠핑장
# 뷰에서 테스트를 부르기 전 사용자 정보가 불러져야 함
# 최근에 리뷰 쓰고 레이팅 점수가 0점 이상해서 쿼리를 뽑아야 함
# 뷰에서 사용자가 최근에 갔던 캠핑장을 찾아서 test()의 인자로 들어가고, 인자가 '난지캠핑장'으로 들어가야 함
# db 셀렉트문 from

