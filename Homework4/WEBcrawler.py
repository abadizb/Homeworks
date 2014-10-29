import urllib.request
from urllib.error import URLError
import re
import os
import pickle
import sys

Tuple=()
List=[]
def visit_url(url, domain, Tuple, List):
    global crawler_backlog
    if(len(crawler_backlog)>10):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1

    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")
            regexp_title = re.compile('<title>(?P<title>.*)</title>')
            regexp_url = re.compile("http://"+domain+"[/\w+]*")
            result = regexp_title.search(content_string, re.IGNORECASE)
            
            if result:
                title = result.group("title")
                title=title[26:]
                title_list=title.split()
                for title_word in title_list:
                    Tuple=(url, title)
                    List.append(Tuple)



            for (urls) in re.findall(regexp_url, content_string):
                    if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                        crawler_backlog[urls] = 0
                        visit_url(urls, domain, Tuple, List)

                        
    except URLError as E:
        print("error")

    x = open("raw_data.txt","bw")
    pickle.dump(List,x)
    x.close

crawler_backlog = {}
seed = "http://www.newhaven.edu/"
crawler_backlog[seed]=0
visit_url(seed,"www.newhaven.edu" , Tuple, List)

#visit_url()


