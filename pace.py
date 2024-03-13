from tabulate import tabulate

def input_dis_pace():
    input_distance=input("距離を入力してください")
    input_min=input("何分")
    input_sec=input("何秒？")
    min_sec=int(input_min)*60+int(input_sec)
    t_100m=min_sec*100/int(input_distance) #100mのタイム
    distance_list=list((range(100,int(input_distance)+100,100))) #100mごとに要素を作成
    time_list=list(range(int(t_100m),min_sec+int(t_100m),int(t_100m))) #100mごとのタイムの要素作成
    return distance_list,time_list
	
def rap_table():
    distance,time=input_dis_pace()
    date={
		'distance':distance,
        'raptime':time
	}
    print(tabulate(date,headers=['distance(m)','raptime(s)'],tablefmt='simple_grid'))
     
rap_table()