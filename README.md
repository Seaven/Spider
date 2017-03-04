#定向爬虫 抓取指定网页信息  
 
Usage:
    python spider_main.py -c spider.conf  

配置文件spider.conf:  

[spider] 
url_list_file: ./urls ; 种子文件路径  
output_directory: ./output ; 抓取结果存储目录  
max_depth: 1 ; 最大抓取深度(种子为0级)  
crawl_interval: 1 ; 抓取间隔. 单位: 秒  
crawl_timeout: 1 ; 抓取超时. 单位: 秒  
target_url: .*.(htm|html)$ ; 需要存储的目标网页URL pattern(正则表达式)  
thread_count: 8 ; 抓取线程数  

种子文件每行一条链接，例如:  
http://www.baidu.com   
http://www.sina.com.cn   


##Patch 1:
thread_task.py --制定多线程执行的任务  
config_load.py --读取爬虫配置文件  
spider.py      --实现爬虫脚本，将url种子文件中的url分配给多个线程分别爬取数据  
url_manage.py  --爬虫url去重set表  
spider_main.py --爬虫运行入口  


##Patch 2:
与Patch 1区别在于爬虫目标url的管理机制  
Patch 1为先分任务，爬虫独自管理url.  
Patch 2为url_manage统一管理url，爬虫排队从url_manage获取目标url  
由于爬虫读取网页有时间和抓取间隔，Patch 2的处理方式下，如果线程数多于初始url数量，可能会造成由于部分线程未分到url直接结束运行  