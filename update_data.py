import functions
import json
import gspread


def update_data() -> None:
    gc = gspread.service_account(filename="venv/google_sheets_auth_data.json")
    sh_connection = gc.open_by_url('https://docs.google.com/spreadsheets/d/17SIijNnjvkGk1-gxV5sBIdxZA3lHdNfWHqi-cQNFw-Q')
    worksheet1 = sh_connection.sheet1
    list_of_lists = worksheet1.get_all_values()

    data = functions.json_converter(list_of_lists)

    with open("data.json", "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

