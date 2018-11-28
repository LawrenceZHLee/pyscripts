import random
import codecs
import time

# 定义数据源
ent_list = ['彭高镇天花运输有限责任公司','鸡冠山乡吉祥运输公司','东源乡如意运输有限公司','杨岐乡吉祥运输有限公司']

# 获取数组数据长度
lensent = len(ent_list)-1

f = open('3.车辆表数据_data_200.csv', 'w',encoding='UTF-8')
r = 0
car_id = 30000000000000000000000000000000
start = time.mktime((2000,1,1,0,0,0,0,0,0))    #生成开始时间戳
end = time.mktime((2017,12,31,23,59,59,0,0,0))      #生成结束时间戳
while r <= 201:
    r += 1
    car_id += 1
    entrn = random.randint(0, lensent)

    nm1 = random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    nm2 = random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    nm3 = random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    nm4 = random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    nm5 = random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    usedate = time.strftime("%Y-%m-%d", time.localtime(random.randint(start, end)))

    ent = ent_list[entrn]
    name = '赣J'+ nm1 + nm2 + nm3 + nm4 + nm5

    print(name)
    f.writelines('\n'+'"'+str(car_id)+'","'+name+'","'+ent+'","'+usedate+'"')
    f.flush()
f.close()





