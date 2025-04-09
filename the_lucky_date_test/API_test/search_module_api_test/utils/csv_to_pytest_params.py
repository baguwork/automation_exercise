import pandas as pd

def convert_xlsx_to_pytest_data(file_path):
    df = pd.read_excel(file_path)

    result = []
    for _, row in df.iterrows():
        limit = int(row["limit"]) if row["limit"] == int else row["limit"]
        criteria = {
            "ageFrom": int(row["age from"]) if row["age from"] == int else row["age from"],
            "ageTo": int(row["age to"]) if row["age to"] == int else row["age to"],
            "country": "" if str(row["country"]).lower() == "nan" or str(row["country"]).strip() == "" else row["country"],
            "onlyOnline": str(row["onlyOnline"]).lower() == "true"
        }

        result.append((criteria, limit))
    with open('C:/Users/baggu/PycharmProjects/QA/the_lucky_date_test/API_test/search_module_api_test/test/test_data.py', 'a') as f:
        f.write("test_data_positive = " + repr(result))

    return result

# Пример вызова
file_path = r"C:\Users\baggu\Downloads\table_decision_positive_search_filter_test_data.xlsx"
data = convert_xlsx_to_pytest_data(file_path)
print(data)

