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

def check(ID):
    db = db_conn()
    sql = "SELECT USER_ID FROM REVIEW_UKC WHERE USER_ID = '" + ID + "'"
    df = pd.read_sql(sql, db)
    if df.index.tolist() != []:
        result = 'exist'
    else:
        result = 'none'
    return result

def check_in_csv(ID):
    df1 = pd.read_csv('home/ratings_pred_matrix.csv')
    df2 = pd.read_csv('home/ratings_matrix.csv')

    if ID not in df1['ID'].tolist() or ID not in df2['ID'].tolist():
        result = 'no data'
    else:
        result = 'data exist'

    return result
