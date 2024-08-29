from scraper import ImageScraper

def main():
    search_key = '"bursa" site:www.pinterest.com'
    number_of_images = 10                # Desired number of images
    headless = False                     # True = No Chrome GUI

    scraper = ImageScraper(search_key, headless)
    scraper.scrape() 

if __name__ == '__main__':
    main()