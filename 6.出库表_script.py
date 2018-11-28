import random
import codecs
import time

# 定义数据源
ent_list = ['彭高镇天花运输有限责任公司','鸡冠山乡吉祥运输公司','东源乡如意运输有限公司','杨岐乡吉祥运输有限公司']
name1_list = ['总厂','药厂','分厂','原料厂','']
name2_list = ['库房','原料仓库','成品仓库','仓库']
name3_list = ['101-1','96-1','101-2','98栋','（虚拟仓库）']
# 获取数组数据长度
lens1 = len(name1_list)-1
lens2 = len(name2_list)-1
lens3 = len(name3_list)-1
lensent = len(ent_list)-1

f = open('6.出库表数据_data_20000.csv', 'w',encoding='UTF-8')
r = 0
out_id = 60000000000000000000000000000000
start = time.mktime((2000,1,1,0,0,0,0,0,0))    #生成开始时间戳
end = time.mktime((2017,12,31,23,59,59,0,0,0))      #生成结束时间戳
while r <= 20001:
    r += 1
    out_id += 1
    entrn = random.randint(0, lensent)
    name1rn = random.randint(0, lens1)
    name2rn = random.randint(0, lens2)
    name3rn = random.randint(0, lens3)
    ent = ent_list[entrn]
    name1 = name1_list[name1rn]
    name2 = name2_list[name2rn]
    name3 = name3_list[name3rn]
    stockname = name1 + name2 + name3
    outdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(random.randint(start, end)))
    outmount = random.randint(40, 90)

    print(stockname)
    f.writelines('\n'+'"'+str(out_id)+'","'+ent+'","'+stockname+'","'+outdate+'","'+str(outmount)+'"')
    f.flush()
f.close()





