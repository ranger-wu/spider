from urllib.request import urlopen
from urllib.request import Request
from urllib.request import urlopen
'''
分页搜索的思路:
第一步:去哪里爬: 找到目标地址
第二步:获取目标页面
第三步:保存页面

针对以上三步:分别定义三个函数:  def tieba()/  def get_html / def save_html
'''

def tieba():
    kw = int(input('请输入内容:'))
    page = int(input('请输入页数:'))
    url = 'http://tieba.baidu.com/f? pn=100'
# http://tieba.baidu.com/f?kw=%E5%B0%9A%E5%AD%A6%E5%A0%82&ie=utf-8&pn=100
#上面是原来要爬取的地址,现在将url里的搜索内容[kw]给踢出来,方便执行后面的for循环
# 现在将要输入的内容kw 跟 页数page 放在args字典里,再将args传到目标地址url
#可以实现效果:通过输入的内容跟页数 找到对应的内容









def  get_html():
    pass





def  save_html():
    pass




if __name__=='__main__':
    tieba()




