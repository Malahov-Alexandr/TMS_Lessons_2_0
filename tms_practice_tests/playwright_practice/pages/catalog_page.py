class CatalogPage:
    def __init__(self, page):
        self.page = page

    def select_by_text(self, category):
        self.page.get_by_text(category, exact=True).click()

    def select_by_role(self, category):
        self.page.get_by_role("link", name=category).first.click()
