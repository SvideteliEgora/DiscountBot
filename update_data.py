import time
import gspread
import functions
import json
import schedule
import threading


def job():
    gc = gspread.service_account(filename="venv/google_sheets_auth_data.json")
    sh_connection = gc.open_by_url('https://docs.google.com/spreadsheets/d/17SIijNnjvkGk1-gxV5sBIdxZA3lHdNfWHqi-cQNFw-Q')
    worksheet1 = sh_connection.sheet1
    list_of_lists = worksheet1.get_all_values()

    data = functions.json_converter(list_of_lists)
    print('Я отработал!')

    with open("data.json", "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def schedule_job():
    while True:
        schedule.run_pending()
        time.sleep(1)


# Запускаем задачу каждые 20 секунд
schedule.every(20).seconds.do(job)


# Запускаем цикл проверки в отдельном потоке
check_thread = threading.Thread(target=schedule_job)
check_thread.start()

while True:
    pass
