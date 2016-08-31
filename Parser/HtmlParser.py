from bs4 import BeautifulSoup
from DBManager.DBApi import DB
''' 解析网页'''
'''
    单词呈现方式
    <h2><a>word</a>zhmeaning</h2>
    <p></p>....cont(content)....<p></p>
'''
class Parser:
    def __init__(self):
        self.db = DB()

    def Parse(self,htmldoc):
        if htmldoc is None :
            return None
        soup = BeautifulSoup(htmldoc,'html.parser')
        titles = soup.find_all('h2')
        if titles is None :
            return None
        for title in titles:
            zhmeaning = title.get_text().split('：')[-1]
            word = title.find('a').get_text()
            cont = ''
            content = title.find_next_sibling()
            while(content != None and content.name != 'h2'):
                cont += content.get_text()
                content = content.find_next_sibling()
            self.db.Add(word=word,zhmeaning= zhmeaning,cont=cont)
