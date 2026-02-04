import scrapy

custom_settings = {
    "DOWNLOAD_DELAY": 1,
    "ROBOTSTXT_OBEY": False
}

class LaOpinionCorunaSpider(scrapy.Spider):
    name = "laopinioncoruna"
    allowed_domains = ["laopinioncoruna.es"]
    start_urls = [
        "https://www.laopinioncoruna.es/galicia/2026/02/03/mercado-inmobiliario-estalla-pisos-medio-126405751.html"
    ]

    def parse(self, response):
        title = response.xpath("//h1[@data-aida-title]/text()").get()
        date_modified = response.xpath("//time[@itemprop='dateModified']/@datetime").get()
        subtitle = response.xpath("//h2[@data-aida-subtitle]/text()").get()

        yield {
            "title": title.strip() if title else "",
            "date": date_modified if date_modified else "",
            "subtitle": subtitle.strip() if subtitle else "",
            "source": "La Opinión A Coruña"
        }
