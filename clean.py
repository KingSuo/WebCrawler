import os
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
import re

import json

import requests
from bs4 import BeautifulSoup


class Clean:
    def __init__(self):
        pass

    def clean(self):
        new_dict = {}
        with open("F:\workspace\git\WebCrawler\File\kubernetes.json") as fp:
            data = json.load(fp)
        for key in data.keys():
            api_vision = data[key][1]
            new_dict[api_vision] = {}
        for key in data.keys():
            api_vision = data[key][1]
            method = data[key][0]
            object_type = method.split("_", 1)[1]
            new_dict[api_vision][object_type] = {}
        for key in data.keys():
            method = data[key][0]
            api_vision = data[key][1]
            fun, object_type = method.split("_", 1)
            new_dict[api_vision][object_type][fun] = method

        print(new_dict["AdmissionregistrationV1alpha1Api"])
        with open("F:\workspace\git\WebCrawler\File\K8s_API.json", "w") as fp:
            json.dump(new_dict, fp, indent=4)

    def get_urls(self):
        new_list = set()
        with open("F:\workspace\git\WebCrawler\File\kubernetes.json") as fp:
            urls = json.load(fp)
        for key in urls.keys():
            new_list.add(key.split("#")[0])
        with open(r"F:\workspace\git\WebCrawler\File\urls.txt", "w") as fp:
            for url in new_list:
                fp.write(url + '\n')
        return urls

    def generate_urls(self):
        with open(r"F:\workspace\git\WebCrawler\File\urls.txt") as fp:
            return fp.read().split('\n')

    def save_html(self, html_data, filename):
        with open(r"F:\workspace\git\WebCrawler\File\HTML\%s.html" % filename, "w", encoding="utf-8") as fp:
            fp.writelines(str(html_data))
            print("Save html file OK!")

    def get_html(self, url):
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        filename = url.split("/")[-1].split(".md")[0]
        self.save_html(str(soup), filename)

    def regular(self, html_data):
        r = re.compile(
            r'<h3><a aria-hidden="true" class="anchor" href="#parameters[\s\S]*<h3><a aria-hidden="true" class="anchor" href="#authorization')
        result = r.findall(html_data)
        new = result[0].split("<h3><a aria-hidden=\"true\" class=\"anchor\" href=\"#para")[1:]
        has_parameters = [
            False if "<p>This endpoint does not need any parameter.</p>" in i.split("Parameters</h3>", 1)[1] else True
            for i in new]
        print(has_parameters)
        return has_parameters

    def get_parameters(self, html_path):
        with open(html_path, encoding="utf-8") as fp:
            soup = BeautifulSoup(fp, "html.parser")
        with open(r"F:\workspace\git\WebCrawler\File\HTML\ApiregistrationV1Api.html", encoding="utf-8") as fp:
            has_parameters = self.regular(fp.read())
        tables = soup.find_all("table")
        tr = tables[0].find_all("tr")
        methods = [i.td.a["href"].split('#')[-1] for i in tr[1:]]
        keys = {}
        for i in range(len(methods)):
            if has_parameters[i]:
                keys[methods[i]] = {}
            else:
                keys[methods[i]] = None
        parameters = tables[1:]
        # print(parameters[0])
        # print(len(parameters))
        sub_tbodys = [i.tbody for i in parameters]
        sub_trs = [i.find_all("tr") for i in sub_tbodys]
        print(sub_trs[0])
        print(len(sub_trs[0]))
        print(len(sub_trs))

    def save_parameters(self, ):
        pass


if __name__ == "__main__":
    c = Clean()
    html_path = r"F:\workspace\git\WebCrawler\File\HTML\ApiregistrationV1Api.html"
    c.get_parameters(html_path)

    # with open(r"F:\workspace\git\WebCrawler\File\HTML\ApiregistrationV1Api.html", encoding="utf-8") as fp:
    #     c.regular(fp.read())
