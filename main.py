class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def info(self):
        print(f"Site {self.name} has link {self.url} has {self.pages} pages.")

    def add_page(self):
        title = input("Input title of page: ")
        content = input("Input content of page: ")
        date = input("Input date of creation: ")
        page = WebPage(title, content, date)
        self.pages.append(title)
        print(f"Page {title} about {content} was added on {date}")

    def create_site(self):
        new_name = input("Input new title of site: ")
        url = input("Input new url of site: ")
        site = WebSite(self.name, self.url)
        print(f"Site {new_name} was created with link {url}")
        return site

    def delete_page(self, page_name):
        for page in self.pages:
            if page.title == page_name:
                self.pages.remove(page)
                print(f"Page {page.title} was removed")
            else:
                print("Page was not found")


class WebPage():
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

    def info(self):
        print(f"Page {self.title} about {self.content} was added on {self.date}")


while True:
    print("Press 1 to output sites info.")
    print("Press 2 to add page.")
    print("Press 3 to create new site.")
    print("Press 4 to delete page.")
    print("Press 5 to output page info.")
    print("Press 6 to exit.")

    command = int(input("What do you want to do?: "))
    if command == 1:
        site_1 = WebSite("site_1", "url_1.com")
        site_1.info()
    elif command == 2:
        site_1 = WebSite("site_1", "url_1.com")
        site_1.add_page()
    elif command == 3:
        site_1 = WebSite("site_1", "url_1.com")
        site_1.create_site()
    elif command == 4:
        site_1 = WebSite("site_1", "url_1.com")
        name = input("Input page name: ")
        site_1.delete_page(name)
    elif command == 5:
        page = WebPage("title_1", "content_1", "06.06.2024")
        page.info()
    elif command == 6:
        break
    else:
        print("Wrong command")


