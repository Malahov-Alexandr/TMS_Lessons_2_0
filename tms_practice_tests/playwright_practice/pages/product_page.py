class ProductPage:
    def __init__(self, page):
        self.page = page

    def get_title(self):
        return self.page.locator("#modalSet").get_by_text("Салон штор «Виджи дизайн»").text_content()

    def get_address(self):
        return self.page.locator("#modalSet").get_by_text("ул. Шафарнянская, 18-19").text_content()

    def say_to_admin_text(self):
        return (self.page.locator("#modalSet").
                get_by_text("Пожалуйста, сообщите администратору, что нашли этот телефон на Blizko.by").text_content())