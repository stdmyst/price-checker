import requests

class NotionClient():
    def __init__(self, access_token, notion_version="2022-06-28"):
        self.access_token = access_token
        self.headers = {"Authorization": f"Bearer {access_token}",
           "Content-Type": "application/json",
           "Notion-Version": notion_version}
        self.notion_base_url = "https://api.notion.com/v1/"
        
    def retrieve_db(self, db_id):
        page_url = self.notion_base_url + "databases/" + db_id
        res = requests.request("GET", page_url, headers=self.headers)
        print(res.status_code)
        return res.json()
    
    def query_db(self, db_id):
        page_url = f"{self.notion_base_url}databases/{db_id}/query"
        res = requests.request("POST", page_url, headers=self.headers)
        print(res.status_code)
        return res.json()
    
    def update_page(self, page_id, data):
        page_url = self.notion_base_url + "pages/" + page_id
        res = requests.request("PATCH", page_url, headers=self.headers, data=data)
        print(res.status_code)
        
    def update_db(self, db_id, data):
        page_url = self.notion_base_url + "databases/" + db_id
        res = requests.request("PATCH", page_url, headers=self.headers, data=data)
        print(res.status_code)
        
    def update_block(self, page_id, data):
        page_url = self.notion_base_url + "blocks/" + page_id + "/children"
        res = requests.request("PATCH", page_url, headers=self.headers, data=data)
        print(res.status_code)
