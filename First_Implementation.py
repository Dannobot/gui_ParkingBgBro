import numpy as np
import psycopg2
import info as NF
import cv2
import os
import time

asd = []
alfa = []
beta = []
ddd = []
tree_p = []
# re = 263

def nothing(x):
    pass

def nothing2(x):
    return x - 25


def mouse_move(event, x, y, flag, void):
    if event == cv2.EVENT_MBUTTONDOWN:
        cv2.line(img, (x, y), (x, y), (200, 20, 155), 2)
        asd.append([x,y])
        if len(asd)%2 == 0:
            cv2.line(img, (asd[-1][0], asd[-1][1]), (asd[-2][0], asd[-2][1]), (120, 220, 155), 2)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        poroh(h, w, x, y, alfa)
        cv2.line(img, (x, y), (x, y), (250, 110, 250), 1)

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.line(img, (x, y), (x, y), (220, 220, 15), 4)
        tree_p.append([x, y])

        if len(tree_p)%2 == 0:
            k = 0
            z = 0
            n = 11
            # xn, yn = tree_p[-3]
            xv, yv = tree_p[-2]
            # for i in range(kilk):
                # ddd.append([xv+k, yv-z])
                # ddd.append([xv+k+n, yv-z])
                # ddd.append([xv+k+n-3, yv-20-z])
                # ddd.append([xv+k-3, yv-20-z])

                # ddd.append([xv+k, yv+z])
                # ddd.append([xv+20+k, yv+z])
                # ddd.append([xv+20-3+k, yv+11+z])
                # ddd.append([xv-3+k, yv+11+z])

                # ddd.append([xv+k, yv+z])
                # ddd.append([xv+20+k, yv+z])
                # ddd.append([xv+20+1+k, yv+10+z])
                # ddd.append([xv+1+k, yv+10+z])

                # poroh(h, w, xv+k, yv+z, alfa)
                # poroh(h, w, xv+20+k, yv+z, alfa)
                # poroh(h, w, xv+20+1+k, yv+10+z, alfa) 
                # poroh(h, w, xv+1+k, yv+10+z, alfa) 
                
                # if i % 3:
                #     k += 2
                # else:
                #     k += 2
                # z += 10

                # if len(ddd)%4 == 0:
                #     points = np.array([ddd[-4], ddd[-3], ddd[-2], ddd[-1]])
                #     cv2.polylines(img, [points], True, (0, 255, 255), 1)

            
            for i in range(kilk):
                nx = (tree_p[-1][0]-xv)/(kilk-i)
                ny = (tree_p[-1][1]-yv)/(kilk-i)
                
                k = int(nx)
                z = int(ny)

                ddd.append([xv, yv])
                ddd.append([xv+xp, yv+yp])
                # ddd.append([xn, yn])
                ddd.append([xv+k+xp, yv+z+yp])
                ddd.append([xv+k, yv+z])
                # ddd.append([xn+k, yn+z])
                

                poroh(h, w, xv, yv, alfa)
                poroh(h, w, xv+xp, yv+yp, alfa)
                # poroh(h, w, xn, yn, alfa)
                # poroh(h, w, xn+k, yn+z, alfa)
                poroh(h, w, xv+k+xp, yv+z+yp, alfa) 
                poroh(h, w, xv+k, yv+z, alfa)  

                # xn = xn+k
                # yn = yn+z
                xv = xv+k
                yv = yv+z

                if len(ddd)%4 == 0:
                    points = np.array([ddd[-4], ddd[-3], ddd[-2], ddd[-1]])
                    cv2.polylines(img, [points], True, (0, 255, 255), 1)

        


def do_crop_img(arr):
    pts = np.array(arr)
    rect = cv2.boundingRect(pts)
    x, y, w, h = rect
    crop_img = img[y:y + h, x:x + w].copy()
    pts = pts - pts.min(axis=0)
    mask = np.zeros(crop_img.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
    dst = cv2.bitwise_and(crop_img, crop_img, mask=mask)
    return dst, rect


def get_by_city_fps(name):
    result = []
    tables = ['parkname', 'Id']
    conn = psycopg2.connect(dbname=NF.dbName, user=NF.user, password=NF.password, host=NF.host)

    with conn.cursor() as cursor:
        cursor.execute(f'SELECT geo, city, id FROM tabletutu WHERE city = \'{name}\'')
        conn.commit()
        for row in cursor:
            result.append(list(row))
        cursor.close()
        return result


def poroh(h, w, x, y, alfa):
    for i in ananas:
        if i[2] == re:
            g = 40.5877603
            z = -73.9526928
            PMHLt = float(i[0][0]) + (-0.000672*2)
            PMWLn = float(i[0][1]) + (0.000886*2)
            PZHLt = float(i[0][0]) + (0.000672*2)
            PZWLn = float(i[0][1]) + (-0.000886*2)
            KH = (PMHLt-PZHLt)/h
            KW = (PMWLn-PZWLn)/w
            Lt = KH*(y) + PZHLt
            Ln = KW*(x) + PZWLn
            alfa.append({'lat':Lt, 'lng':Ln})
            # print([{'lat': g + (0.000472), 'lng': z + (0.000486)}, {'lat': g - (0.000472), 'lng': z + (0.000486)}, {'lat': g - (0.000472), 'lng': z - (0.000386)}, {'lat': g + (0.000472), 'lng': z - (0.000386)}])
            print(alfa)


if __name__ == '__main__':
    for i in os.listdir('/home/dannobot/Use'):
        if i.split('-')[1] == 'New York':
            global re, kilk
            img = cv2.imread(f'/home/dannobot/Use/{i}', cv2.IMREAD_COLOR)
            zeros = np.zeros((150, 150, 3))
            imgCopy = zeros.copy()
            ananas = get_by_city_fps(i.split('-')[1])
            re = int(i.split('-')[0])
            h, w = img.shape[:2]

            cv2.namedWindow('OpenedImg', cv2.WND_PROP_FULLSCREEN)

            cv2.createTrackbar("KP", "OpenedImg", 1, 40, nothing)
            cv2.createTrackbar("x+", "OpenedImg", 25, 50, nothing)
            cv2.createTrackbar("y+", "OpenedImg", 35, 50, nothing)
            
            cv2.setMouseCallback('OpenedImg', mouse_move, None)
            # cv2.setMouseCallback('OpenedImg2', mouse_move, None)
            ax = 0
            ay = 0
            while (True):
                kilk = cv2.getTrackbarPos("KP", "OpenedImg") 
                xp = cv2.getTrackbarPos("x+", "OpenedImg") - 25
                yp = cv2.getTrackbarPos("y+", "OpenedImg") - 25
                cv2.imshow('OpenedImg', img)

                cv2.line(zeros, (75, 75), (75+xp, 75+yp), (120, 220, 155), 2)
                cv2.imshow('OpenedImg2', zeros)
                if ax != xp:
                    zeros = imgCopy.copy()
                if ay != yp:
                    zeros = imgCopy.copy()
                ax = xp
                ay = yp

                if cv2.waitKey(1) == 27:
                    break
            we = []
            ew = []
            for j in alfa:
                we.append(j)
                if len(we) % 4 == 0:
                    ew.append(we)
                    we = []
            with open(f'/home/dannobot/PythonW/Kalman/Python/city_txt/{re}.txt', 'a') as wr:
                for j in ew:
                    wr.write(f'{j}')