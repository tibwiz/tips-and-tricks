class Containter:
    def is_registered(self,site:str):
        s = Site('main')
        print(site,s.site)


class Site:
    def __init__(self, site:str):
        self.__site = site

    @property
    def site(self):
        return self.__site;

c = Containter()
c.is_registered(site='main')