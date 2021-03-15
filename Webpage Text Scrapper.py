from urllib.request import urlopen
import validators
import requests
from bs4 import BeautifulSoup as bs

URL = input("Enter the url : ")

valid=validators.url(URL)
if valid==True:
    print("Url is valid")
    
    try:
        response = requests.get(URL)
        print("Given URL is valid and exists on the internet.\nIt contains the following text:")
    except requests.ConnectionError as exception:
        print("Given URL does not exist on Internet")

    HTML_doc = urlopen(URL).read()
    bs_HTML = bs(HTML_doc, features="html.parser")

    for script in bs_HTML(["script", "style"]):
        script.extract()    # remove it

    text = bs_HTML.body.get_text(separator=' ')

    stripped_line = (line.strip() for line in text.splitlines())

    hlines = (phrase.strip() for line in stripped_line for phrase in line.split("  "))

    #Formatting and printing the final text 
    scraped_text = '\n'.join(phrase for phrase in hlines if phrase)
    print(scraped_text)

else:
    print("Invalid url")
