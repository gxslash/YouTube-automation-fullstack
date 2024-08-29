import requests
from uuid import uuid4
from io import BytesIO
from PIL import Image
from playwright.sync_api import sync_playwright

MAX_IMAGE_COUNT = 10

class ImageScraper:
    
    def __init__(self, search_key, headless=False) -> None:
        print(f'[INFO] Gathering image links for {search_key}')
        self._headless = headless
        self._init_url = self._build_images_url(search_key)
        self._image_count = 0
        self._downloaded_image_urls = []

    def _start_browsing(self, pw, headless):
        browser = pw.chromium.launch(headless=headless)
        page = browser.new_page()
        page.goto(self._init_url)
        page.wait_for_timeout(1000)
        return page
    
    def _get_image_url(self):
        image = self._page.query_selector("img.detail__media__img-thumbnail.js-detail-img.js-detail-img-thumb")
        image_url = "https:" + image.get_attribute("src")
        return image_url

    def _find_clickable_images(self):
        return self._page.query_selector_all("div.tile.tile--img.has-detail")

    def _build_images_url(self, search_key):
        return f'https://duckduckgo.com/?q={search_key}&t=h_&iax=images&ia=images'
    
    def _download_image(self, url):
        response = requests.get(url)
        image_bytes = None
        if response.status_code == 200:
            print("Image downloaded")
            image_bytes = response.content
            self._image_count += 1
            self._downloaded_image_urls.append(url)
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
        return image_bytes
    
    def _is_enough(self):
        if self._image_count > MAX_IMAGE_COUNT:
            return True
        return False
    
    def scrape(self):
        with sync_playwright() as pw:
            self._page = self._start_browsing(pw, self._headless)
            for image in self._find_clickable_images():
                image.click()
                self._page.wait_for_timeout(500)
                url = self._get_image_url()
                if url in self._downloaded_image_urls:
                    continue
                image_bytes = self._download_image(url)
                save_image(image_bytes)
                if self._is_enough():
                    break

def save_image(image_bytes):
    image = Image.open(BytesIO(image_bytes))
    image.save(f"./images/downloaded_image_{uuid4()}.jpg")
