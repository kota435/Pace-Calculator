from tabulate import tabulate
import sys

def input_time():
    input_min=input("何分")
    input_sec=input("何秒？")
    min_sec=int(input_min)*60+int(input_sec)
    return min_sec

def input_dis():
    input_distance=int(input('距離を入力してください'))
    
    if check_distance(input_distance):
        print('100m単位で入力して下さい')
        sys.exit()
    else:
        return input_distance

def check_distance(num):
    ones_place=num%10
    tens_place=(num//10)%10
    
    if ones_place != 0 or tens_place != 0:
        return True
    else:
        return False

def create_list():
    input_distance=input_dis()
    min_sec=input_time()
    t_100m=min_sec*100/int(input_distance) #100mのタイム
    time_list=list(range(int(t_100m),min_sec+int(t_100m),int(t_100m))) #100mごとのタイムの要素作成
    distance_list=list((range(100,int(input_distance)+100,100)))
    return distance_list,time_list
    
def rap_table():
    distance,time=create_list()
    date={
		'distance':distance,
        'raptime':time
	}
    print(tabulate(date,headers=['distance(m)','raptime(s)'],tablefmt='simple_grid'))
     
rap_table()