import requests
from urllib.request import urlretrieve
import shutil
import json
import re
import os

ranking_list = []


class Crawl(object):
    # 获取排行榜
    def get_rankings_json(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/96.0.4664.9 Safari/537.36'}
        self.good_list = []  # 保存好评率的列表
        self.name_list = []  # 保存商品名称的列表
        self.jd_id_list = []  # 保存京东ID的列表
        response = requests.get(url,headers=headers)  # 发送网络请求，获取服务器响应
        json_str = str(response.json())  # 将请求结果的json转为字符串
        dict_json = eval(json_str)  # 将json字符串信息转换为字典，方便提取信息
        jd_id_str = ''
        if os.path.exists('img_download'):
            shutil.rmtree('img_download')
            os.makedirs('img_download')
        for index, i in enumerate(dict_json['products']):
            id = i['wareId']  # 京东号码
            J_id = 'J_' + i['wareId']  # 京东ID，添加J_作为获取价格参数
            self.jd_id_list.append(id)  # 将京东ID添加至列表
            name = i['wareName']  # 商品名称
            self.name_list.append(name)  # 将商品名称添加至列表
            good = i['goodRate']  # 好评率
            self.good_list.append(str(good) + '%')  # 将好评率添加至列表
            jd_id_str = jd_id_str + J_id + ','  # 拼接京东ID字符串
            if index <= 10:
                # 图片地址
                imgPath = 'https://img14.360buyimg.com/n1/s320x320_' + i['imgPath']
                # 根据下标命名图片名称
                urlretrieve(imgPath, 'img_download/' + str(index) + '.jpg')
        return jd_id_str

    # 获取价格
    def get_price(self, id):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/96.0.4664.9 Safari/537.36'}
        ranking_list.clear()  # 清空排行榜的列表
        # 获取价格的网络请求地址
        price_url = 'https://p.3.cn/prices/mgets?type=1&skuIds={id_str}'
        # 将京东ID作为参数发送获取商品的网络请求
        response = requests.get(price_url.format(id_str=id), headers=headers)
        price = response.json()  # 获取价格JSON数据，该数据为list类型
        for index, item in enumerate(price):
            # 商品名称
            name = self.name_list[index]
            # 商品价格
            jd_price = item['p']
            # 每个商品的ID
            jd_id = self.jd_id_list[index]
            # 好评率
            good = self.good_list[index]
            # 将所有数据添加到列表
            ranking_list.append((index + 1, name, jd_price, jd_id, good))
        return ranking_list

    # 获取评价内容，score参数差评为1，中评为2，好评为3,0为全部
    def get_evaluation(self, score, id):
        # 创建头部信息
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/96.0.4664.9 Safari/537.36'}
        # 评价请求地址参数，callback为对应书名的JSON的ID
        # productID书名对应的京东ID
        # score是评价等级参数
        # sortType类型，6为时间排序，5为推荐排序
        # pageSize每页显示评价10条
        # page页数
        params = {
            'callback': 'fetchJSON_comment98',
            'productId': id,
            'score': score,
            'sortType': 6,
            'page': 0,
            'pageSize': 10,
            'isShadowSku': 0,
            'fold': 1,
        }
        # 评价请求网址
        url = 'https://club.jd.com/comment/skuProductPageComments.action'
        # 发送请求
        evaluation_response = requests.get(url, params=params, headers=headers)
        if evaluation_response.status_code == 200:
            evaluation_response = evaluation_response.text
            try:
                # 去除JSON外层的括号与名称
                t = re.search(r'({.*})', evaluation_response).group(0)
            except Exception as e:
                print('评价的JSON数据匹配异常！')
            j = json.loads(t)  # 加载JSON数据
            commentSummary = j['comments']
            for comment in commentSummary:
                # 评价内容
                c_contetn = comment['content']
                # 时间
                c_time = comment['creationTime']
                # 京东昵称
                c_name = comment['nickName']
                # 评价类型 1差评 2-3中评 4-5好评
                c_score = comment['score']
            if len(commentSummary) == 0:
                # 返回无
                return '无'
            else:
                # 根据不同需求返回不同的值
                return commentSummary[0]['creationTime']
