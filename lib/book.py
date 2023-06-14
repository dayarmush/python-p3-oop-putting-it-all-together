#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count = 0):
        self.title = title
        self.page_count = page_count

    def set_page(self, page):
        if type(page) == int:
            self._page_count = page
        else:
            print('page_count must be an integer')

    def get_page(self):
        return self._page_count
    
    page_count = property(get_page, set_page)

    def turn_page(self):
        return print("Flipping the page...wow, you read fast!")
        
    
        