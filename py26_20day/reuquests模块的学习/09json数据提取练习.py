"""
============================
Author:柠檬班-木森
Time:2020/2/19   22:00
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import jsonpath

data = {'code': 200,
        'data': [{'uid': 9436, 'title': '早报：全国新型肺炎确诊31161例；孙宇晨已与巴菲特共进晚餐；特斯拉关闭中国所有门店',
                  'photo': 'https://static-image.xfz.cn/1581035484_149.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1564640994_620.jpg',
                             'authors': [{'author_id': 2244, 'name': '史素云'}]}, 'is_original': True,
                  'article_type': '热点', 'intro': '福布斯发布香港富豪榜，李嘉诚跌落蝉联21年首富宝座', 'source': '小饭桌',
                  'time': '2020-02-07 08:31:24', 'keywords': ['新型肺炎', '巴菲特', '特斯拉']},
                 {'uid': 9435, 'title': '“现金流不够半年建议休眠，疫情过后再重启”丨6位投资人给的创业者生存指南',
                  'photo': 'https://static-image.xfz.cn/1580995460_596.png',
                  'author': {'photo': 'https://static-image.xfz.cn/1552965456_492.jpg',
                             'authors': [{'author_id': 500, 'name': '饭桌君'}]}, 'is_original': True,
                  'article_type': '干货分享', 'intro': '变局中CEO该如何开源节流、稳定军心？', 'source': '小饭桌',
                  'time': '2020-02-06 21:25:50', 'keywords': ['疫情', '创业']},
                 {'uid': 9434, 'title': '早报：全国新型肺炎确诊28018例；特斯拉拟推出拼车应用；耐克关闭中国约一半直营店',
                  'photo': 'https://static-image.xfz.cn/1580949870_822.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1564640994_620.jpg',
                             'authors': [{'author_id': 2244, 'name': '史素云'}]}, 'is_original': True,
                  'article_type': '热点', 'intro': '每日优鲜与西贝、眉州东坡展开人力调配合作', 'source': '小饭桌',
                  'time': '2020-02-06 08:44:30', 'keywords': ['新型肺炎', '特斯拉', '迪士尼', '每日优鲜']},
                 {'uid': 9433, 'title': '重磅！疫情如何影响经济',
                  'photo': 'https://static-image.xfz.cn/1580877662_20.jpeg',
                  'author': {'photo': 'https://static-image.xfz.cn/1552965456_492.jpg',
                             'authors': [{'author_id': 500, 'name': '饭桌君'}]}, 'is_original': False,
                  'article_type': '热点',
                  'intro': '短期来看，线下服务业遭受重创，中小企业首当其冲，机电产品和劳动密集型产品出口受到影响，这些负面影响不容轻视，应慎重对待，但不必担心中国经济的长期发展趋势，还应看到消费场景加速向线上转型、新技术带来服务业创新、制造业数字化智能化改造提速等积极变化。',
                  'source': '', 'time': '2020-02-05 12:41:02', 'keywords': ['肺炎疫情']},
                 {'uid': 9432, 'title': '抗疫！青松基金携手被投企业在行动！',
                  'photo': 'https://static-image.xfz.cn/1580873705_441.png',
                  'author': {'photo': 'https://static-image.xfz.cn/1552965456_492.jpg',
                             'authors': [{'author_id': 500, 'name': '饭桌君'}]}, 'is_original': False,
                  'article_type': '热点', 'intro': '全民一心，相信还将有更多的个人、企业、组织加入到这场战役。', 'source': '',
                  'time': '2020-02-05 12:07:32', 'keywords': ['肺炎疫情']},
                 {'uid': 9431, 'title': '早报：全国新型肺炎确诊24324例；洲际交易所或将收购eBay；马斯克全球富豪排名第一',
                  'photo': 'https://static-image.xfz.cn/1580863007_637.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1564640994_620.jpg',
                             'authors': [{'author_id': 2244, 'name': '史素云'}]}, 'is_original': True,
                  'article_type': '热点', 'intro': '蛋壳公寓：针对无法返城的租客，计划返还租金', 'source': '小饭桌',
                  'time': '2020-02-05 08:36:47', 'keywords': ['新型肺炎', '马斯克', '蛋壳公寓']},
                 {'uid': 9430, 'title': '迎战肺炎疫情，这里有四个企业生存锦囊丨致全体桌友',
                  'photo': 'https://static-image.xfz.cn/1580817563_793.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1552965456_492.jpg',
                             'authors': [{'author_id': 500, 'name': '饭桌君'}]}, 'is_original': True,
                  'article_type': '热点', 'intro': '疫情过后，行业和公司迎来爆发的内在动力是创业者在最困难时期的信心与坚持', 'source': '小饭桌',
                  'time': '2020-02-04 19:59:52', 'keywords': ['肺炎疫情']},
                 {'uid': 9429, 'title': '早报：全国新型肺炎确诊20438例；高盛、亚马逊或向中小企业发放贷款；特斯拉股价大涨',
                  'photo': 'https://static-image.xfz.cn/1580776581_210.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1564640994_620.jpg',
                             'authors': [{'author_id': 2244, 'name': '史素云'}]}, 'is_original': True,
                  'article_type': '热点', 'intro': '盒马联合云海肴等解决现阶段餐饮行业待岗人员收入问题', 'source': '小饭桌',
                  'time': '2020-02-04 08:36:21', 'keywords': ['新型肺炎', '特斯拉', '高盛', '亚马逊']},
                 {'uid': 9428, 'title': '早报：全国新型肺炎确诊17205例；火神山医院工程完工；上交所：上市公司可申请延期披露财报',
                  'photo': 'https://static-image.xfz.cn/1580690341_124.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1564640994_620.jpg',
                             'authors': [{'author_id': 2244, 'name': '史素云'}]}, 'is_original': True,
                  'article_type': '热点', 'intro': '美团单车发起“无差别消毒”，所有共享单车全部进行消毒', 'source': '小饭桌',
                  'time': '2020-02-03 08:39:01', 'keywords': ['新型肺炎', '美团', '三星', '作业帮']},
                 {'uid': 9427, 'title': '5位湖北农村人自述：肺炎阴影笼罩下的疫区春节',
                  'photo': 'https://static-image.xfz.cn/1580471498_876.png',
                  'author': {'photo': 'https://static-image.xfz.cn/1552965456_492.jpg',
                             'authors': [{'author_id': 500, 'name': '饭桌君'}]}, 'is_original': True,
                  'article_type': '热点', 'intro': '武汉周边疫区会不会“灯下黑”', 'source': '小饭桌',
                  'time': '2020-01-31 19:55:08', 'keywords': ['新型肺炎']},
                 {'uid': 9426, 'title': '凯辉基金携手法国11家企业集团驰援武汉，捐赠急需医疗物资、共渡难关！',
                  'photo': 'https://static-image.xfz.cn/1580276292_446.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1552965456_492.jpg',
                             'authors': [{'author_id': 500, 'name': '饭桌君'}]}, 'is_original': False,
                  'article_type': '热点', 'intro': '凯辉大家庭的成员企业也纷纷向疫情地区发起捐款及物资捐赠。', 'source': '小饭桌',
                  'time': '2020-01-29 13:38:12', 'keywords': ['凯辉', '拼多多', '京东', '壹米滴答', '美年大健康']},
                 {'uid': 9425, 'title': '早报：武汉全市离汉通道暂时关闭；淘宝禁售“野味”；工信部紧急协调口罩生产   ',
                  'photo': 'https://static-image.xfz.cn/1579740386_982.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1577153468_501.jpg',
                             'authors': [{'author_id': 2245, 'name': '柴容'}]}, 'is_original': True,
                  'article_type': '热点', 'intro': '字节跳动正为TikTok业务寻找一位新的CEO', 'source': '小饭桌',
                  'time': '2020-01-23 08:46:26', 'keywords': ['武汉“封城”', '淘宝野味', '口罩', '趣头条', '字节跳动']},
                 {'uid': 9424, 'title': '早报：医保局：为新型肺炎患者采取特殊报销；淘宝所有口罩绝不允许涨价；滴滴给司机发放口罩和消毒液',
                  'photo': 'https://static-image.xfz.cn/1579653248_916.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1552965456_492.jpg',
                             'authors': [{'author_id': 500, 'name': '饭桌君'}]}, 'is_original': True,
                  'article_type': '热点', 'intro': '星巴克早餐或将供应人造肉', 'source': '小饭桌',
                  'time': '2020-01-22 08:34:08', 'keywords': ['医保局', '淘宝口罩', '滴滴司机']},
                 {'uid': 9423, 'title': '早报：美团联创王慧文年底退休；马化腾出售500万股腾讯股份；字节跳动回应飞聊团队解散',
                  'photo': 'https://static-image.xfz.cn/1579566730_810.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1577153468_501.jpg',
                             'authors': [{'author_id': 2245, 'name': '柴容'}]}, 'is_original': True,
                  'article_type': '热点', 'intro': '故宫博物院院长就奔驰开进宫事件致歉，副院长、保卫处处长停职', 'source': '小饭桌',
                  'time': '2020-01-21 08:32:11', 'keywords': ['美团王慧文', '马化腾', '字节跳动']},
                 {'uid': 9422, 'title': '曾由中国宽带之父投资组建，它和Oracle、SAS“抢饭碗”，靠给银行卖软件年营收过亿',
                  'photo': 'https://static-image.xfz.cn/1579487114_781.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1577153468_501.jpg',
                             'authors': [{'author_id': 2245, 'name': '柴容'}]}, 'is_original': True,
                  'article_type': '创业案例', 'intro': 'BI逐步转向AI的过程中，复杂的商业流程经算法重构', 'source': '小饭桌',
                  'time': '2020-01-20 10:28:24', 'keywords': ['大数据', 'AI技术']},
                 {'uid': 9421, 'title': '早报：SpaceX成功测试飞船逃生能力；“木兰”创作者回应：研发没有使用经费；乐天创始人去世',
                  'photo': 'https://static-image.xfz.cn/1579480948_674.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1577153468_501.jpg',
                             'authors': [{'author_id': 2245, 'name': '柴容'}]}, 'is_original': True,
                  'article_type': '热点', 'intro': '马斯克：未来或利用海上船只回收载人龙飞船', 'source': '小饭桌',
                  'time': '2020-01-20 08:42:28', 'keywords': ['SpaceX', '木兰项目', '乐天创始人', '京东']},
                 {'uid': 9419, 'title': '早报：LV总裁取代亚马逊创始人成新首富；WhatsApp全面停止广告；前美国副总统炮轰扎克伯格',
                  'photo': 'https://static-image.xfz.cn/1579393463_666.jpg',
                  'author': {'photo': 'https://static-image.xfz.cn/1577153468_501.jpg',
                             'authors': [{'author_id': 2245, 'name': '柴容'}]}, 'is_original': False,
                  'article_type': '热点', 'intro': '马云谈“企二代”靠老子：不用证明比别人强，有老子就是运气', 'source': '小饭桌',
                  'time': '2020-01-19 08:24:23', 'keywords': ['福布斯世界首富', 'WhatsApp', '魅族']},
                 {'uid': 9418, 'title': '百福控股再获弘毅投资7.8亿港元融资',
                  'photo': 'https://static-image.xfz.cn/1578934569_333.png',
                  'author': {'photo': 'https://static-image.xfz.cn/1552965456_492.jpg',
                             'authors': [{'author_id': 500, 'name': '饭桌君'}]}, 'is_original': False,
                  'article_type': '融资消息', 'intro': '弘毅投资与百福控股收购和投资了十四个知名餐饮品牌。', 'source': '小饭桌',
                  'time': '2020-01-14 08:30:29', 'keywords': ['白富控股', '弘毅投资', '餐饮']},
                 {'uid': 9416, 'title': '早报：蚂蚁金服或先于百度等在港股上市；京东物流外部收入占比超40%；亚马逊员工泄露客户数据',
                  'photo': 'https://static-image.xfz.cn/1578793786_241.jpg',
                  'author': {'photo': '', 'authors': [{'author_id': 2238, 'name': '月耳'}]},
                  'is_original': True, 'article_type': '热点', 'intro': '唱吧推出音乐创作者分成计划，称将在2020年投入一个亿',
                  'source': '小饭桌', 'time': '2020-01-12 09:50:05', 'keywords': ['蚂蚁金服', '百度']},
                 {'uid': 9415, 'title': '早报：小红书正寻求4~5亿美元融资；瑞幸咖啡募集7.78亿美元；唱吧被指抄袭唱鸭',
                  'photo': 'https://static-image.xfz.cn/1578707375_431.jpg',
                  'author': {'photo': '', 'authors': [{'author_id': 2238, 'name': '月耳'}]},
                  'is_original': True, 'article_type': '热点', 'intro': 'OYO被称将在中国和印度裁员数千人', 'source': '小饭桌',
                  'time': '2020-01-11 09:45:17', 'keywords': ['小红书', '唱吧', '瑞幸咖啡']}]}

uid = jsonpath.jsonpath(data, "$.data[15]..uid")
print(uid)

# 如果没有提取到数据 返回的是False

# json类型的数据

# []:叫做数组

# {}：叫做对象

# python类型的数据和json的区别
# json类型的数据

# []:json叫做数组,python中叫列表
# {}：json叫做对象,python叫字典
# json       python
# false  --->  False
# true   --->  True
# null   --->  None
import json

s = """
[111,{
    "status": false,
    "code": true,
    "data": null,
    "msg": "登录成功"
}]
"""
# 将字符串中的json,转换对应的python数据(列表或字典)
res = json.loads(s)
print(res)
dic = {'status': False, 'code': True, 'data': None, 'msg': '登录成功'}

# 将python中的字典或列表，转换为对应的json字符串
res3 = json.dumps(dic)
print(res3,type(res3))