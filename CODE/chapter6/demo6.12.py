dict1 = {
    'title':'欧瑞学院',
    'website':'https://geekori.com',
    'description':'从事在线IT课程研发和销售'    
    }
dict2 = {
    'title':'欧瑞科技',
    'products':['欧瑞学院','博客','读书频道','极客题库','OriUnity'],
    'description':'从事在线IT课程研发和销售，工具软件研发'
    }
dict1.update(dict2)
for item in dict1.items():
    print("key = {key}  value = {value}".format(key = item[0],value = item[1]))
