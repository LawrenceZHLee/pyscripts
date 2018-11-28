import random
import codecs
import time
import datetime
from phone_id_generator import  createphone,gennerator

# 定义数据源

name1_list = ['赵','钱','孙','李','周','吴','郑','王','林','杨','柳','刘','孙','陈','江','阮','侯','邹','高','彭','徐']
name2_list = ['伯','仲','叔','季','方','正','端','凝','启','延','宗','庆','统','承','宏','绪','基','贤','继','盛','显','扬','先','业','邦','家','之','光','文','章','炳','耀','永','世','其','昌']
name3_list = ['经','纶','承','祖','泽','光','裕','振','家','声','肇','建','洪','模','永','宗','支','裔','代','荣']
leixing_list = ['驾驶员','押运员']
addr_list = ['上栗镇','桐木镇','金山镇','福田镇','彭高镇','赤山镇','鸡冠山乡','长平乡','东源乡','杨岐乡']
ent_list = ['彭高镇天花运输有限责任公司','鸡冠山乡吉祥运输公司','东源乡如意运输有限公司','杨岐乡吉祥运输有限公司']

# 获取数组数据长度
lensname1 = len(name1_list)-1
lensname2 = len(name2_list)-1
lensname3 = len(name3_list)-1
lensleixing = len(leixing_list)-1
lensaddr = len(addr_list)-1
lensent = len(ent_list)-1


f = open('2.人员表数据_data_600.csv', 'w',encoding='UTF-8')
r = 0
psn_id = 20000000000000000000000000000000
start = time.mktime((2000,1,1,0,0,0,0,0,0))    #生成开始时间戳
end = time.mktime((2017,12,31,23,59,59,0,0,0))      #生成结束时间戳
while r <= 601:
    r += 1
    psn_id += 1
    name1rn = random.randint(0,lensname1)
    name2rn = random.randint(0,lensname2)
    name3rn = random.randint(0,lensname3)
    leixingrn = random.randint(0,lensleixing)
    addrrn= random.randint(0,lensaddr)
    entrn = random.randint(0, lensent)

    name1 = name1_list[name1rn]
    name2 = name2_list[name2rn]
    name3 = name3_list[name3rn]
    leixing = leixing_list[leixingrn]
    addr = addr_list[addrrn]
    ent = ent_list[entrn]
    name = name1 + name2 + name3
    phone = createphone()
    id = gennerator()
    borndate = datetime.datetime.strptime(id[6:14],'%Y%m%d')
    bornstr = borndate.strftime("%Y-%m-%d")
    enterdate = time.strftime("%Y-%m-%d",time.localtime(random.randint(start,end)))

    # print(name)
    f.writelines('\n'+'"'+str(psn_id)+'","'+name+'","'+addr+'","'+leixing+'","'+ent+'","'+phone+'","'+id+'","'+bornstr+'","'+enterdate+'"')
    f.flush()
f.close()