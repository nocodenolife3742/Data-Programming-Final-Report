import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import os


# function to remove unused labels
def remove_unused_labels(data: pd.DataFrame):
    unused_labels = ['學校統計處代碼', '學期', '設立別', '學校類別', '學校統計', '處代碼', '系所代碼', '系所名稱',
                     '學制班別', '性別', '學制班別(日間)']
    for label in unused_labels:
        if label not in data.columns:
            continue
        data = data.drop(label, axis=1)
    return data


def main():
    # create folder if not exist
    if not os.path.exists('./data'):
        os.makedirs('./data')

    # define categories and urls
    categories = ['延修', '休學', '退學']
    urls = [
        "https://udb.moe.edu.tw/download/udata/static_file/%E5%AD%B84.%E6%97%A5%E9%96%93%E5%AD%B8%E5%A3%AB%E7%8F%AD%E4%BB%A5%E4%B8%8B%E7%94%B3%E8%AB%8B%E5%BB%B6%E9%95%B7%E4%BF%AE%E6%A5%AD%E5%B9%B4%E9%99%90%E4%B9%8B%E5%BB%B6%E4%BF%AE%E7%94%9F%E6%95%B8-%E4%BB%A5%E3%80%8C%E7%B3%BB(%E6%89%80)%E3%80%8D%E7%B5%B1%E8%A8%88.csv",
        "https://udb.moe.edu.tw/download/udata/static_file/%E5%AD%B813-1.%E6%96%BC%E5%AD%B8%E5%B9%B4%E5%BA%95%E8%99%95%E6%96%BC%E4%BC%91%E5%AD%B8%E7%8B%80%E6%85%8B%E4%B9%8B%E4%BA%BA%E6%95%B8-%E4%BB%A5%E3%80%8C%E7%B3%BB(%E6%89%80)%E3%80%8D%E7%B5%B1%E8%A8%88(110%E5%AD%B8%E5%B9%B4%E5%BA%A6%E4%BB%A5%E5%89%8D).csv",
        "https://udb.moe.edu.tw/download/udata/static_file/%E5%AD%B814-1.%E9%80%80%E5%AD%B8%E4%BA%BA%E6%95%B8-%E4%BB%A5%E3%80%8C%E7%B3%BB(%E6%89%80)%E3%80%8D%E7%B5%B1%E8%A8%88(110%E5%AD%B8%E5%B9%B4%E5%BA%A6%E4%BB%A5%E5%89%8D).csv"
    ]

    # download data
    datum = {}
    for url, category in zip(urls, categories):
        data = pd.read_csv(url, low_memory=False)
        data = remove_unused_labels(data)
        data.replace('...', 0, inplace=True)
        datum[category] = data

    # TODO : 這裡merge爛了QWQ
    # split data by year
    for year in range(106, 111):  # 106 ~ 110
        merged_data = pd.DataFrame()
        for category in categories:
            data = datum[category]
            data = data[data["學年度"] == year]
            data = data.drop(["學年度"], axis=1)
            data = data.astype({col: int for col in data.columns[1:]})  # convert to int, ignore the first column
            data = data.groupby("學校名稱").sum().reset_index()
            merged_data = pd.concat([merged_data, data], ignore_index=True)
        merged_data.fillna(0, inplace=True)
        merged_data = merged_data.astype({col: int for col in merged_data.columns[1:]})
        merged_data = merged_data.groupby("學校名稱").sum().reset_index()
        merged_data.to_csv(f'./data/{year}.csv', index=False)


if __name__ == '__main__':
    main()
