# Chinese-clans

25/5/13 

add some raw data in github

creat tow .py for writing code

[zhejiang_genealogy.py](raw data/test/zhejiang_genealogy.py)
[zhejiang_genealogy_test.py](raw data/test/zhejiang_genealogy_test.py)
[test.py](raw data/test/test.py)

creat one .ipynb for visualization
[zhejiang_genealogy_test.ipynb](raw data/test/zhejiang_genealogy_test.ipynb)

实现了单页抓取的功能。
需要解决数据字段不完全问题

25/5/14

解决了字段不完全的问题
实现了指定起始页数，多页抓取的功能。
接下来进行共计5187页的抓取

25/5/19
因为网站加载延迟，无法大规模抓取
改善代码，监测当前页数

25/5/20
通过对照前后页第一行数据，解决了无法大规模抓取的问题
进行共计5187页的实际抓取
代码文件为 [grasp_genealogy.py](genealogy A/grasp_genealogy.py)

25/5/20
收集了5174页数据
接下来需要合并，整理过滤

25/5/22
清理好了文件

制作面板数据
顺序为
[panel_genealogy_省市县.py](genealogy%20B/panel_genealogy_%E7%9C%81%E5%B8%82%E5%8E%BF.py)
[panel_genealogy_cleaned_省市县.py](genealogy%20B/panel_genealogy_cleaned_%E7%9C%81%E5%B8%82%E5%8E%BF.py)
[panel_genealogy_cleaned_省市.py](genealogy%20B/panel_genealogy_cleaned_%E7%9C%81%E5%B8%82.py)
[panel_genealogy_cleaned_省.py](genealogy%20B/panel_genealogy_cleaned_%E7%9C%81.py)











