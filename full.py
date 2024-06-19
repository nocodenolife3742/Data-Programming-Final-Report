import requests
import json

nid_table = {
    2023: 3816281,
    2024: 3897789
}


def main():
    response = requests.get(
        "https://www.timeshighereducation.com/json/rankings"
        "/world_university_rankings_2024_0__91239a4509dc50911f1949984e3fb8c5.json"
    )
    data = json.loads(response.text)
    for node in data['score_nodes']:
        print(node['title'], node['overall_score'])


if __name__ == '__main__':
    main()
