
class go:
    def __init__(self,name):
        self.name = name
    class waiting_zone:
        def __init__(self,name):
            self.name = name
        @classmethod
        def deck(self):
            print("test")
if __name__ == "__main__":
    a=go.waiting_zone.deck()
    a