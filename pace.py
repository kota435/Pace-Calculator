from tabulate import tabulate
import sys

def convert_to_sec(minutes,secounds):
    #分単位から秒単位に変更
    min_sec=int(minutes)*60+int(secounds)
    return min_sec

def validate_distance_input(c_distance):
    #入力された距離が100m単位ではなかった時、エラーメッセージを出し、スクリプトを終了させる
    if check_distance(c_distance):
        print('100m単位で入力して下さい')
        sys.exit()
    else:
        return c_distance

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
    time_per_100m=min_sec*100/int(input_distance) 
    time_list=list(range(int(time_per_100m),min_sec+int(time_per_100m),int(time_per_100m))) #100mごとのタイムの要素作成
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
            min_sec_list.append(f'{minutes}\'{remaing_seconds}')
    return min_sec_list

def output_sprit_table(distance,time):
    #表を作成し、出力
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
    distance=validate_distance_input(input_distance)
    time_list=create_list_time(min_sec,distance)
    min_sec_list=convert_to_min(time_list)
    distance_list=create_list_distance(distance)
    
    output_sprit_table(distance_list,min_sec_list)
    
if __name__ == '__main__':
    main()