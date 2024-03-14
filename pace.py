from tabulate import tabulate

def input_time():
    input_min=input("何分")
    input_sec=input("何秒？")
    min_sec=int(input_min)*60+int(input_sec)
    return min_sec

def input_dis():
    input_distance=int(input('距離を入力してください'))
    return input_distance

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