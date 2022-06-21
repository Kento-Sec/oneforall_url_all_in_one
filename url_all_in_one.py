import os
import pandas as pd
import argparse
import sys

parser = argparse.ArgumentParser(description="oneforall辅助工具,汇总多个csv表中的url")
parser.add_argument("-p", "--path", type=str, metavar="path", help="csv目标路径 eg:\"/XX/XX\"")
args = parser.parse_args()

if len(sys.argv) != 3:
    print(
        "[-]  参数错误！\neg1:>>>python url_all_in_one.py -p 存在csv文件的目标路径 ")
    
path1 = args.path

for filename in os.listdir(path1):
    # 是csv文件
    if filename.endswith(".csv"):
        file_path1 = path1 + "/" + filename
        print(file_path1)
        path_size = os.path.getsize(file_path1)
        if path_size != 0:
            # 读取csv可能会编码错误  还可加参数 engine="python" 或者指定编码 encoding="ISO-8859-1"就可以解决
            df1 = pd.read_csv(file_path1,engine="python",encoding='ISO-8859-1')
            # 索引指定列的数据
            df2 = df1[['url']]
            print(df2)
            df2.to_csv("url.csv",
                        index=False, mode='a+', header=False,encoding="gb2312")
    elif path_size == 0:
        print(file_path1+" 文件是空的～～～～")
    else :
        print(file_path1+" 文件格式不是csv～～～～")
        pass

        
print("完成！")
