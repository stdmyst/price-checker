from datetime import datetime

import notion_client, price_check
import time
import json


def main():
    kind = {"stocks": "https://www.tinkoff.ru/invest/stocks/",
            "etfs": "https://www.tinkoff.ru/invest/etfs/"}

    with open("files/settings.json", encoding="UTF-8") as f:
        settings = json.load(f)
    access_token = settings["access_token"]
    db_id = settings["db_id"]
    
    notion = notion_client.NotionClient(access_token=access_token)
    db = notion.query_db(db_id)
    
    for el in db["results"]:
        page_id = el["id"]
        el_kind = el["properties"]["Kind"]["rich_text"][0]["text"]["content"]
        el_ticket = el["properties"]["Ticker"]["rich_text"][0]["text"]["content"]
        url = kind[el_kind.lower()] + el_ticket.lower()
        new_data = {"properties": {"Current price": {"number": price_check.get_price(url)}, 
                               "Update date": {"date": {"start": str(datetime.today()), 
                                                        "time_zone": "Europe/Moscow"}}}}
        notion.update_page(page_id, json.dumps(new_data))
        

if __name__ == "__main__":
    main()
