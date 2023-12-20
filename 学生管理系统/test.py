import os.path
import time
from itertools import filterfalse
import httpx
from lxml import etree
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
def metadata_parser(path):
    def pattern1():
        with open(path, encoding="utf-8") as fp:
            tree = etree.HTML(fp.read())
        return tree.xpath("//td//a/text()")
    def pattern2():
        with open(path, encoding="utf-8") as fp:
            tree = etree.HTML(fp.read())
        new_dic=[]

        for href in tree.xpath("//article//a/@href"):
            if not "video" in href:
                new_dic.append(href.split("?")[-1] )

        old_dic=list(zip(new_dic,tree.xpath("//article//a/text()")))
        old_dic.sort(key=lambda x:(x[0]))
        return [dic [1] for dic in old_dic]
    def pattern3():

        return ["シリーズ" for _ in range(25)]
    return  pattern2()

target="kurokage"
pattern1_str="https://loli.teen.jp/{}/images/{:02d}/{:02d}.jpg"
def downloader(index,fname):
    i = 0

    while True:
        i+=1
        fpath = "{}/{:02d} {}".format(target, index, fname)
        ffullpath = "{}/{:03d}.jpg".format(fpath, i)

        if not os.path.exists(fpath):
            os.makedirs(fpath)
        if os.path.exists(ffullpath):
            print("文件存在")
            continue
        with  httpx.Client(follow_redirects=False) as hc:
            res = hc.get(
                pattern1_str.format(
                    target,index, i))
            if res.status_code == 200:
                print(res.url)
                with open(ffullpath, 'wb') as fp:
                    fp.write(res.content)
            else:
                print("下载错误", res.url)
                break

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=8) as pool:
        results=[]
        for index,fname in enumerate(metadata_parser(fr"D:\programer\github\python_practice\学生管理系统\db\{target}.html")):
            index+=1
            result=pool.submit(downloader, index, fname)
            results.append(result)
        wait(results)



