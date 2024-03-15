from tabulate import tabulate
import sys

def convert_to_sec(a,b):
    minutes,secounds=a,b
    min_sec=int(minutes)*60+int(secounds)
    return min_sec

def input_dis(num):
    c_distance=num
    if check_distance(c_distance):
        print('100m単位で入力して下さい')
        sys.exit()
    else:
        return c_distance

def check_distance(num):
    ones_place=num%10
    tens_place=(num//10)%10
    
    if ones_place != 0 or tens_place != 0:
        return True
    else:
        return False

def create_list_distance(num):
    distance=num
    distance_list=list((range(100,int(distance)+100,100)))
    return distance_list

def create_list_time(a,b):
    min_sec,input_distance=a,b
    t_100m=min_sec*100/int(input_distance) #100mのタイム
    time_list=list(range(int(t_100m),min_sec+int(t_100m),int(t_100m))) #100mごとのタイムの要素作成
    return time_list

def convert_to_min(a):
    timelist=a
    min_sec_list=[]
    for seconds in timelist:
        if seconds<60:
            min_sec_list.append(seconds)
        else:
            minutes=seconds//60
            remaing_seconds=seconds%60
            min_sec_list.append(str(minutes)+"'"+str(remaing_seconds))
    return min_sec_list

def sprit_table(a,b):
    distance,time=a,b
    date={
		'distance':distance,
        'raptime':time
	}
    print(tabulate(date,headers=['distance(m)','raptime(s)'],tablefmt='simple_grid'))
     
def main():
    input_distance=int(input('距離を入力してください'))
    input_min=input("何分")
    input_sec=input("何秒？")
    min_sec=convert_to_sec(input_min,input_sec)
    distance=input_dis(input_distance)
    time_list=create_list_time(min_sec,distance)
    min_sec_list=convert_to_min(time_list)
    distance_list=create_list_distance(distance)
    
    sprit_table(distance_list,min_sec_list)
    
main()