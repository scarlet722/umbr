class Item:
    count = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Item.count += 1

class Book(Item):
    def __init__(self, title, price, pages, author):
        super().__init__(title, price)
        self.pages = pages
        self.author = author

    def getprice(self):
        return f"책 제목: {self.title}, 가격: {self.price}원, 페이지 수: {self.pages}페이지, 저자: {self.author}"

class Magazine(Item):
    def __init__(self, title, price, issue_month):
        super().__init__(title, price)
        self.issue_month = issue_month

    def getprice(self):
        return f"잡지 제목: {self.title}, 가격: {self.price}원, 발행 월: {self.issue_month}"

if __name__ == "__main__":
    book1 = Book('소나기', 10000, 124, '황순원')
    book2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
    book3 = Book('난쏘공', 12000, 112, '조세희')
    magazine1 = Magazine('보그', 11000, '9월')
    magazine2 = Magazine('싱글즈', 13000, '8월')

    print(book1)
    print(book2)
    print(book3)
    print(magazine1)
    print(magazine2)
    print('총', Item.count, '권')
