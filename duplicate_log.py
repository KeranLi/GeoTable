import argparse
import pandas as pd
import numpy as np
from tqdm import tqdm

def duplicate_check_log(excel_file):
   # 从Excel文件中读取数据，存储在 num, txt, 和 raw1 中
   df = pd.read_excel(excel_file, engine='openpyxl', sheet_name=1)

   # 初始化计数器
   n_repeat = 0
   n_no_repeat = 0

   # 定义用于存储重复行的索引的变量
   index_repeat1 = []
   index_repeat2 = []

   # 定义用于存储非重复行的索引的变量
   index_no_repeat = []

# 循环遍历数据行
   for i in tqdm(range(2, len(df) - 1)):  # 使用tqdm显示进度
      repeat = 0
      # 与后续行比较以查找重复数据
      for j in range(i + 1, len(df)):  # 修复循环范围
          # 比较列7（title）、列12（sample）和列41（point）的值
          if (df.iloc[i, 7] == df.iloc[j, 7]) and (df.iloc[i, 12] == df.iloc[j, 12]) and (df.iloc[i, 41] == df.iloc[j, 41]):
              # 如果列8的值包含于另一行的列8（DOI），标记为重复
              if ((df.iloc[i, 8].apply(lambda x: np.isin(x, df.iloc[j, 8]).any())).any()) or ((df.iloc[j, 8].apply(lambda x: np.isin(x, df.iloc[i, 8]).any())).any()):
                  repeat = 1
                  n_repeat += 1

                  # 存储重复行的索引
                  index_repeat1.append(i)
                  index_repeat2.append(j)
                  break
      # 如果没有找到重复行，将其标记为非重复行
      if not repeat:
          n_no_repeat += 1
          # 存储非重复行的索引
          index_no_repeat.append(i)

   # 为数据添加行号列
   row_numbers = np.arange(1, len(df) + 1)
   df_repeat = pd.concat([pd.DataFrame(index_repeat1), df.iloc[index_repeat1, :]], axis=1)
   df_repeat.columns = ['row_number'] + list(df.columns)
   df_repeat.insert(1, 'row_number', row_numbers[index_repeat1])

   df_no_repeat = pd.concat([pd.DataFrame(index_no_repeat), df.iloc[index_no_repeat, :]], axis=1)
   df_no_repeat.columns = ['row_number'] + list(df.columns)
   df_no_repeat.insert(1, 'row_number', row_numbers[index_no_repeat])