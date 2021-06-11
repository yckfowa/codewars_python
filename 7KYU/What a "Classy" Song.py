
class Song():
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.listeners= []


    def how_many(self, list)->int:
        count = 0
        for el in list:
            el = el.lower()
            if el not in self.listeners:
                self.listeners.append(el)
                count+=1
        return count
