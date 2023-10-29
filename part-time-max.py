import pandas as pd

df = pd.read_excel("バイト代2023ver.xlsx")
# print(df)


# 欠損値を最大値で埋めた場合
# df_max = df

# max_value = df["バイト代"].max()
# print(max_value)

# df_max.fillna(max_value, inplace=True)
# print(df_max)

# -------欠損地を9月の月収で埋めた場合--------
df_same_9month = df

df_same_9month.fillna(method="ffill", axis=0, inplace=True)
print(df_same_9month)

df_same_9month['rank'] = df_same_9month['Salary'].rank(ascending=True)
print(df_same_9month)
