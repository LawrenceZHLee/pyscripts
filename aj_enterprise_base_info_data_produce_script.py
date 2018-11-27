import random
import codecs

# 定义数据源
name1_list = ['上栗镇','桐木镇','金山镇','福田镇','彭高镇','赤山镇','鸡冠山乡','长平乡','东源乡','杨岐乡']
name2_list = ['富祥','吉祥','如意','大地','天花']
name3_list = ['花炮','鞭炮','黑火药','引线','烟花','爆竹','商贸','运输']
name4_list = ['公司','有限公司','有限责任公司','厂']
leixing_list = ['原材料生产','原材料运输','花炮生产']

# 获取四组数据长度
lens1 = len(name1_list)-1
lens2 = len(name2_list)-1
lens3 = len(name3_list)-1
lens4 = len(name4_list)-1
lens5 = len(leixing_list)-1


f = open('aj_enterprise_base_info_data_1000.csv', 'a',encoding='UTF-8')
r = 0
ent_id = 10000000000000000000000000000000
while r <= 1001:
    r += 1
    ent_id += 1
    name1rn = random.randint(0,lens1)
    name2rn = random.randint(0,lens2)
    name3rn = random.randint(0,lens3)
    name4rn = random.randint(0,lens4)
    leixingrn= random.randint(0,lens5)
    name1 = name1_list[name1rn]
    name2 = name2_list[name2rn]
    name3 = name3_list[name3rn]
    name4 = name4_list[name4rn]
    leixing = leixing_list[leixingrn]
    name = name1 + name2 + name3 + name4

    print(name)
    f.writelines('\n'+'"'+str(ent_id)+'","'+name+'","'+name1+'","'+leixing+'"')
    f.flush()
f.close()





