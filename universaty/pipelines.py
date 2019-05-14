# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import importlib
importlib.reload(sys)
import pymysql
class UniversatyPipeline(object):
    def process_item(self, item, spider):
        for i in item:
            item[i][0]=str(item[i][0]).replace("\r\n\t\t\t\t"," ")
            print(item[i][0])
        filename='top.txt'
        # 1. 创建数据库连接对象
        con = pymysql.connect(host='localhost', port=3306,database='school', charset='utf8',user='school', password='12345678')
        try:
            # 2. 通过连接对象获取游标
            with con.cursor() as cursor:
                # 3. 通过游标执行SQL并获得执行结果
                result = cursor.execute(
                    'insert into school values (%s,%s, %s,%s,%s)',
                    (int(item['grade'][0]), item['school'][0], item['top'][0],item['start'][0],float(item['layout'][0]))
                )
            if result == 1:
                print('添加成功!')
            # 4. 操作成功提交事务
            con.commit()
        finally:
            # 5. 关闭连接释放资源
            con.close()
        with open(filename,'a',encoding='utf-8') as f:
            f.write(item['grade'][0].ljust(10, ' ')+item['school'][0].ljust(25, ' ')+item['top'][0].ljust(10, ' ')+item['start'][0].ljust(30, ' ')+item['layout'][0]+'\n')
        return item
