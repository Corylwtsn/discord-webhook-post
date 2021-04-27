import requests
import os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

def main():
    webhook_url = os.getenv('WEBHOOK_URL', default=None)
    if webhook_url == None:
        logging.fatal('WEBHOOK_URL is missing')
    message = os.getenv('MESSAGE', default=None)
    if message == None:
        logging.fatal('MESSAGE is missing')
    if webhook_url == None or message == None:
        exit(1)
    req_body = {
        'content': message
    }
    req_headers = {
        'Content-Type': 'application/json'
    }
    req = requests.post(webhook_url, headers=req_headers, json=req_body)
    if not req:
        logging.error("Unable to complete request")
        logging.debug(req.text)

if __name__ == "__main__":
    main()