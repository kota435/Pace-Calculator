from tabulate import tabulate

def validate_time_to_sec():
    #入力されたタイムが正しい形式で入力されているか確認、秒変換を行い、入力されたタイムを返す。
    while True:
        try:
            minutes,secounds=int(input('何分？:')),int(input('何秒？:'))
            break
        except ValueError:
            print('半角数字を入力して下さい')

    #分単位から秒単位に変更
    min_sec=minutes*60+secounds
    return min_sec

def validate_distance_input():
    #入力された距離が正しい形式で入力されてるか確認し、入力された距離を返す
    while True:
        try:
            distance=int(input('100m単位で距離を入力して下さい。:'))
            if check_distance(distance):
                print('100m単位で入力して下さい。')
                continue
            return distance
            break
        except ValueError:
            print('半角数字を入力して下さい。')
        

def check_distance(num):
    ones_place=num%10
    tens_place=(num//10)%10
    
    #一の位、十の位に0以外が入っていないか判定
    if ones_place != 0 or tens_place != 0:
        return True
    else:
        return False

def create_list_distance(distance):
    #入力された距離を100mごとのリストに分割
    distance_list=list((range(100,int(distance)+100,100)))
    return distance_list

def create_list_time(min_sec,input_distance):
    #入力されたタイムを距離に対しての100mのタイムに
    time_per_100m=int(min_sec*100/input_distance) 
    time_list=list(range(time_per_100m,min_sec+time_per_100m,time_per_100m)) #100mごとのタイムの要素作成
    return time_list

def convert_to_min(timelist):
    min_sec_list=[]
    #与えられたタイムが60秒未満であればそのまま、60秒以上であれば繰り上げを行う
    for seconds in timelist:
        if seconds<60:
            min_sec_list.append(seconds)
        else:
            minutes=seconds//60
            remaing_seconds=seconds%60
            min_sec_list.append(f'{minutes}\'{remaing_seconds:02}')
    return min_sec_list

def output_sprit_table(distance,time):
    #表を作成し、出力
    date={
		'distance':distance,
        'raptime':time
	}
    print(tabulate(date,headers=['distance(m)','sprittime(s)'],tablefmt='simple_grid'))
     
def main():
    distance=validate_distance_input()
    min_sec=validate_time_to_sec()
    time_list=create_list_time(min_sec,distance)
    min_sec_list=convert_to_min(time_list)
    distance_list=create_list_distance(distance)
    
    output_sprit_table(distance_list,min_sec_list)
    
if __name__ == '__main__':
    main()