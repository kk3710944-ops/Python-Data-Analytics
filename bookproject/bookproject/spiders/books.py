
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):
        for book in response.css("article.product_pod"):
            yield {
                "title": book.css(
                    "h3 a::attr(title)"
                ).get(),
                "price": book.css(
                    ".price_color::text"
                ).get(),
                "availability": "".join(
    book.css(".availability::text").getall()
).strip(),
            }

        next_page = response.css(
            "li.next a::attr(href)"
        ).get()

        if next_page:
            yield response.follow(
                next_page,
                callback=self.parse
            )
