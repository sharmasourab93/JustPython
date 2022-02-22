

def format_header(fn):
    def wrapped(self=None):
        return '<div class="page_header">' + fn(self) + '</div>'
    
    return wrapped


class MyPage:
    
    def __init__(self):
        self.page_name = ''
        
    def create_page(self):
        page_header = self.create_header()
        print(page_header)
        
    @format_header
    def create_header(self):
        return "Page Header: {0}".format(self.page_name)
    
    
if __name__ == '__main__':
    page = MyPage()
    page.page_name = 'My Page'
    page.create_page()
