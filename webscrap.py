import requests
from bs4 import BeautifulSoup

response = requests.get("http://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")
pages = soup.select(".page-numbers")
max_page_num = 1
for page in pages:
    if page.getText().isdigit():
        page_num = int(page.getText())
        if max_page_num < page_num:
            max_page_num = page_num

print(max_page_num)
#for num in range(1, max_page_num+1):
for num in range(1, 10):
    url="https://stackoverflow.com/questions?tab=newest&page=" + str(num)
    response = requests.get(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    questions = soup.select(".question-summary")
    for question in questions:
        print(question.select_one(".question-hyperlink").getText())
        print(question.select_one(".vote-count-post").getText())

