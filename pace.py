
input_distance=input("距離を入力してください")
input_min=input("何分？")
input_sec=input("何秒？")

min_sec=int(input_min)*60+int(input_sec)
warukazu=int(input_distance)/100
handred_1=min_sec/warukazu #100mのタイム
	
distance_list=list((range(100,int(input_distance)+100,100))) #100mごとに要素を作成
time_list=list(range(int(handred_1),int(handred_1*warukazu)+int(handred_1),int(handred_1))) #100mごとのタイムの要素作成
	
def pacekeisan():
	 for output_distance in distance_list: #距離出力(100mごと)
	   print(str(output_distance)+'m')
	 for output_time in time_list:  #タイム出力(100mごと)
	  if output_time<60: #秒、分変換
	    output_result=str(output_time)+'秒'
	    print(output_result)
		

	  else:
	    fun,byo=divmod(output_time,60)
	    fun=int(fun)
	    byo=int(byo)
	    output_result=str(fun)+'分'+str(byo)+'秒'
	    print(output_result)


if int(input_distance)<100:
	  print('100以上の値を入力してください')
else:
	  pacekeisan()


	
	
	

