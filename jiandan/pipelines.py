# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib
from jiandan import settings

class JiandanPipeline(object):
    def process_item(self, item, spider):
        dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)  # 存储路径
        print('dir_path', dir_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['image_urls']:
            list_name = image_url.split('/')
            file_name = list_name[len(list_name) - 1]  # 图片名称
            # print 'filename',file_name
            file_path = '%s/%s' % (dir_path, file_name)
            # print 'file_path',file_path
            if os.path.exists(file_name):
                continue


            with open(file_path, 'wb') as file_writer:
                headers = ('Referer', settings.DEFAULT_REQUEST_HEADERS['Referer'])  # 防盗链，修改访问来源
                opener = urllib.request.build_opener()
                opener.addheaders = [headers]
                data = opener.open(image_url).read()
                file_writer.write(data)
            file_writer.close()
        return item
