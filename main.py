import sys
import requests

def get_url_html():
    url = 'https://pythongreen.netlify.app/'
    response = requests.get(url)
    html_content = response.text
    return html_content

def test1():
    print("Python 路徑：", sys.executable)
    html_content = get_url_html()
    print(html_content)
    
if __name__ == '__main__':
    test1()