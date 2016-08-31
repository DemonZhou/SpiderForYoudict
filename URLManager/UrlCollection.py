import string
class UrlGenerator:
    url = "http://www.youdict.com/ciyuan/"
    def __init__(self):
        pass
    def Generate(self):
        self.urlset = set()
        for i in string.ascii_lowercase:
            firsturl = UrlGenerator.url + "page/" + i + "/"
            for n in range(0, 100):
                secondurl = firsturl + str(n)
                self.urlset.add(secondurl)
        return self.urlset


