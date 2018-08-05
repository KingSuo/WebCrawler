# -*- coding: utf-8 -*-
import os
import json
import requests
from bs4 import BeautifulSoup


class WebCrawler(object):
    def __init__(self):
        base_path, _ = os.path.split(__file__)
        save_path = os.path.join(base_path, "File")
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        self.save_path = save_path

    def get_urls(self, url):
        result = requests.get(url)
        soup = BeautifulSoup(result.content, "html.parser")
        print(soup)
        _, filename = os.path.split(url.split("://")[1])
        # with open(os.path.join(self.save_path, "%s.txt" % filename), "w") as fd:
        #     fd.writelines(soup)


def clean(string):
    result = string.split("td")
    return result


if __name__ == "__main__":
    # web_crawler = WebCrawler()
    # url = "https://github.com/kubernetes-client/python/tree/master/kubernetes"
    # web_crawler.get_urls(url)

    soup = BeautifulSoup(open("/home/kingsuo/workspace/git/WebCrawler/File/kubernetes.txt"))
    # print(soup.prettify())
    print(soup.find_all("tr")[16:])
    for i in soup.find_all("tr")[16:]:
        print(i.em.string)
        print(i.strong.string)
        print(i.a)
    # j = 0
    # for i in map(clean, soup.find_all("tr")[16:]):
    #     j += 1
    #     if j >= 5:
    #         break
    #     print(i)
    print(len(soup.find_all("tr")[16:]))
    # print(len(soup.find_all("em")[1:]))
    print(len([i for i in soup.find_all("strong")[6:] if
               "GET" not in i and "POST" not in i and "DELETE" not in i and "PATCH" not in i and "PUT" not in i]))
