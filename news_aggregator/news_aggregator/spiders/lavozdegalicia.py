import scrapy


class LaVozDeGaliciaSpider(scrapy.Spider):
    name = "lavozdegalicia"
    allowed_domains = ["lavozdegalicia.es"]
    start_urls = [
        "https://www.lavozdegalicia.es/noticia/lavozdelasalud/tribu/2026/02/03/maria-salmeron-pediatra-especialista-salud-digital-cerebro-adolescente-sabe-autorregular/00031770136792841247972.htm"
    ]

    def parse(self, response):
        title = response.xpath("//h1[@class='headline mg-b-2']/text()").get()

        summary = response.xpath("//h3[@class='subtitle t-bld']/text()").get()

        date = response.xpath("//span[@class='sz-t-xs']/strong/text()").get()

        yield {
            "title": title.strip() if title else "",
            "date": date.strip() if date else "",
            "summary": summary.strip() if summary else "",
            "source": "La Voz de Galicia"
        }
