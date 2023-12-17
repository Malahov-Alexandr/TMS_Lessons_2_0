class HomePage:


    def __init__(self, page):
        self.page = page

    def go_to(self,url):
        self.page.goto(url)

    def goto_catalog(self):
        self.page.get_by_role("link", name="Каталог").click()
