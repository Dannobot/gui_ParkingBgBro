import numpy as np
import info as NF
import psycopg2
import json
import time
from datetime import date
import datetime
import random as rand

def get_rds_fps():
    result = []
    a = {"id": "id0", "value": "Road0", "coordinates": ["170", "215"], "fid": None, "children": [{"id": "id1", "value": "Road00", "coordinates": ["343", "174"], "fid": "id0", "children": [{"id": "id2", "value": "Standart", "coordinates": ["627", "1013"], "fid": "id1", "children": [{"id": "id3", "value": "Standart", "coordinates": ["819", "798"], "fid": "id2", "children": [{"id": "id4", "value": "Standart", "coordinates": ["630", "210"], "fid": "id3", "children": []}, {"id": "id5", "value": "Standart", "coordinates": ["1030", "615"], "fid": "id3", "children": [{"id": "id6", "value": "Standart", "coordinates": ["931", "148"], "fid": "id5", "children": []}]}]}]}]}]}
    b = [['id0', {'id1': 178}], ['id1', {'id2': 886}], ['id2', {'id3': 288}], ['id3', {'id4': 618, 'id5': 279}], ['id5', {'id6': 477}]]
    
    conn = psycopg2.connect(dbname=NF.dbName, user=NF.user, password=NF.password, host=NF.host)
    ar = [5, 2]
    k = None
    t = [{'lat': 40.57506190453858, 'lng': 73.98742760741301}, {'lat': 40.57257519954614, 'lng': 73.98723727155824}, {'lat': 40.572644331164895, 'lng': 73.98395062708018}, {'lat': 40.57520423434191, 'lng': 73.98477094780635}]
    sa = []
    
    for i in range(len(t)):
        sa.append(rand.randint(0, 1))

    jsn_a = json.dumps(t)
    with conn.cursor() as cursor:
            # cursor.execute('INSERT INTO public."TICKETS_LOG" (machine_id_fk_pk, account_id_fk, create_date, pre_auth_amount, ticket_machine_id_fk, token, ticket_id_fk, online_entry_yn) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (k, k*2, crd, 1, i, f'tokan{i}', 3, 'TRUE'))
        cursor.execute('UPDATE tabletutu SET parking = %s WHERE id = %s', (jsn_a, 286199))
        conn.commit()

def del_rds_fps():
    conn = psycopg2.connect(dbname=NF.dbName, user=NF.user, password=NF.password, host=NF.host)
    for i in range(301631, 301634):
        with conn.cursor() as cursor:
            cursor.execute(f'DELETE FROM tabletutu WHERE id = {i}')
            conn.commit()

def test(i, d):
    try:    # добавляє юзера в таблицю
        conn = psycopg2.connect(dbname=NF.dbName, user=NF.user, password=NF.password, host=NF.host)
        with conn.cursor() as cursor:
            rnd = rand.randint(5, 20) 
            # rnd = int(d/2)
            cursor.execute(f'UPDATE tabletutu SET allowfree = {rnd}')
            conn.commit()
            cursor.close()
        return 'DONE'
    except:
        return 'ERROR'


def norm_rds(t, a, it):
    conn = psycopg2.connect(dbname=NF.dbName, user=NF.user, password=NF.password, host=NF.host)
    # print(t)
    sa = []
    for i in range(len(t)):
        sa.append(rand.randint(0, 1))

    jsn_a = json.dumps(a)
    jsn_b = json.dumps(t)
    jsn_c = json.dumps(sa)
    with conn.cursor() as cursor:
        cursor.execute('UPDATE tabletutu SET parking = %s WHERE id = %s', (jsn_a, it))
        cursor.execute('UPDATE tabletutu SET parkingplaces = %s WHERE id = %s', (jsn_b, it))
        cursor.execute('UPDATE tabletutu SET json_park = %s WHERE id = %s', (jsn_c, it))
        conn.commit()
    
if __name__ == '__main__':
    # parks = os.listdir('city_txt')
    # for i in parks:
    #     if i.split('.')[-1]=='txt':
    #         with open(f'city_txt/{i}', 'r') as txt:
    #             print(int(i.split('.')[0]))
    #             text = txt.read()
    #             a1 = ast.literal_eval(text.split('#')[0].rstrip())
    #             a2 = ast.literal_eval(text.split('#')[1].rstrip())
                # t = json.dumps(a1)
                # a = json.dumps(a2)
                # print(a2)
                # try:
                #     a = txt.read().split('#')
                    # a = json.dumps(txt.read().split('/n')[1])
                #     print(a)
                # except:
                #     print('ee')
                # norm_rds(a1, a2, int(i.split('.')[0]))


    # today = datetime.datetime.utcnow()
    # print(today)
    # result = []
    # conn = psycopg2.connect(dbname=NF.dbName, user=NF.user, password=NF.password, host=NF.host)
    # with conn.cursor() as cursor:
    #     cursor.execute(f'SELECT id, allplaces FROM tabletutu')
    #     conn.commit()
    #     for i in cursor:
    #         result.append([i[0], i[1]])
    #     cursor.close()
    # print(result)
    # for i in result:
    test(1,2)
    # print('DONE')

    # get_rds_fps()
    # del_rds_fps()

# randList = []
# t = []
# for i in range(1000):
#     t.append(i)
#     # randList.append(int(f'1{rd.randint(1,9)}{rd.randint(1,9)}'))
#     plt.scatter(i, int(f'1{rd.randint(1,9)}{rd.randint(1,9)}'))
#     plt.pause(0.5)

# fig, ax = plt.subplots()
# ax.plot(t, randList)

# plt.show()

# plt.axis([0, 10, 0, 1])
#
# for i in range(10):
#     y = np.random.random()
#     plt.scatter(i, y)
#     plt.pause(0.05)
#
# plt.show()
