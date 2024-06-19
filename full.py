# 2. THE ranking
name_converter = {
    "National Taiwan University (NTU)": "國立臺灣大學",
    "National Tsing Hua University": "國立清華大學",
    "National Chiao Tung University": "國立陽明交通大學",
    "National Taiwan University of Science and Technology (Taiwan Tech)": "國立臺灣科技大學",
    "Taipei Medical University": "臺北醫學大學",
    "National Cheng Kung University (NCKU)": "國立成功大學",
    "China Medical University, Taiwan": "中國醫藥大學",
    "National Taiwan Normal University": "國立臺灣師範大學",
    "Chang Gung University": "長庚大學",
    "Kaohsiung Medical University": "高雄醫學大學",
    "National Central University": "國立中央大學",
    "National Chengchi University": "國立政治大學",
    "National Sun Yat-Sen University": "國立中山大學",
    "National Yang-Ming University": "國立陽明大學",
    "Asia University, Taiwan": "亞洲大學",
    "Chung Yuan Christian University": "中原大學",
    "Feng Chia University": "逢甲大學",
    "Fu Jen Catholic University": "輔仁大學",
    "I-Shou University": "義守大學",
    "National Chung Cheng University": "國立中正大學",
    "National Chung Hsing University": "國立中興大學",
    "National Dong Hwa University": "國立東華大學",
    "National Taipei University": "國立臺北大學",
    "National Taipei University of Technology": "國立臺北科技大學",
    "National Taiwan Ocean University": "國立臺灣海洋大學",
    "Yuan Ze University": "元智大學",
    "National University of Tainan": "國立臺南大學",
}

for year in range(106, 111):  # 106 ~ 110
    data = pd.read_csv(f'./data/{year + 1911}_rankings.csv')
    data["rank"] = data["rank"].str.replace(r"=", "")  # remove "=" in renk column
    data = data[~data["rank"].str.contains(r"\+")]  # filter out all "rank" with "+"
    data = data[data["location"] == "Taiwan"]
    data = data[["rank", "name", "scores_overall"]]
    data["name"] = data["name"].map(name_converter)  # convert name to Chinese
    data.to_csv(f'./data/{year}_taiwan_ranking.csv', index=False)
