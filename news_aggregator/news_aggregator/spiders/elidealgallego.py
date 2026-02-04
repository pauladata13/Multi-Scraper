import scrapy

class ElIdealGallegoSpider(scrapy.Spider):
    name = "elidealgallego"
    allowed_domains = ["elidealgallego.com"]
    start_urls = [
        "https://www.elidealgallego.com/a-coruna/2026-02-03/un-corrimiento-de-tierra-en-a-coruna-provoca-el-corte-de-la-principal-via-de-acceso-al-coliseum-y-carrefour-834388.html"
    ]

    def parse(self, response):
        title = response.css("h1.c-detail__title::text").get()
        date = response.css("div.authors__signature__date::text").get()
        summary = response.css("h2.c-detail__summary::text").get()

        yield {
            "title": title.strip() if title else "",
            "date": date if date else "",
            "summary": summary.strip() if summary else "",
            "source": "El Ideal Gallego"
        }
