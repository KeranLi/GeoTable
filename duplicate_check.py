import pandas as pd

# 读取Excel文件
df = pd.read_excel('./dup_experiment_data.xlsx')

# 根据"Web Lin"、"Published Sample_ID"和"Sample&Grain"这三列进行重复项筛选
df_duplicates_removed = df.drop_duplicates(subset=['Web Link', 'Published Sample_ID', 'Sample&Grain'])

# 保存筛选后的结果到新的Excel文件
df_duplicates_removed.to_excel('duplicates_removed.xlsx', index=False)