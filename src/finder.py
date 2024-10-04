from urllib.parse import urljoin
from time import time, sleep
from random import randint
from requests import get
from bs4 import BeautifulSoup
from typing import Union


class Advertising:
	def __init__(self):
		self.ad = None
		self.ads = []

	def set_ad(self, ad):
		self.ad = ad

	@staticmethod
	def get_ads(source_code):
		return source_code.find_all("div", class_='post-card-item-af972')

	def get_ad_url(self):
		a_tag = self.ad.find('a')
		if a_tag:
			return urljoin("https://divar.ir", a_tag.get("href"))

	def get_ad_title(self):
		title_element = self.ad.find('h2', class_='kt-post-card__title')
		if title_element:
			return title_element.text
		return 'Your URL'

	def get_ad_img(self):
		img = self.ad.find('img')
		if img:
			return img.attrs['data-src']
		return 'https://clipground.com/images/no-image-png-5.jpg'

	def find_all_ads(self, source_code):
		ads = self.get_ads(source_code)
		new_ads = []
		for ad in ads:
			self.set_ad(ad)
			ad_url = self.get_ad_url()
			if ad_url is None or ad_url in self.ads:
				continue

			new_ad = {
				'url': self.get_ad_url(),
				'title': self.get_ad_title(),
				'image': self.get_ad_img()
			}

			new_ads.append(new_ad)
			self.ads.append(ad_url)
		return new_ads


class AdFinder:
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}

	def __init__(self, url: str) -> None:
		self.url: str = url
		self.advertising = Advertising()	

	def set_crawling_time(self, minutes: Union[int, float]) -> None:
		self.crawling_time = minutes * 60

	def _send_request(self):
		return get(self.url, headers=self.headers)

	@staticmethod
	def _get_source_code(response):
		return BeautifulSoup(response.text, "html.parser")

	def _find_ads(self, source_code):
		return self.advertising.find_all_ads(source_code)

	def run(self):
		while True:
			response = self._send_request()
			source_code = self._get_source_code(response)
			ads = self._find_ads(source_code)
			count_ad = len(ads)
			print('Total ad count: %d' % count_ad)
			print('*' * 200)
			for ad in ads:
				print(f'title: {ad.get("title")} \n\nurl: {ad.get("url")} \n\nimage: {ad.get("image")}')
				print('-' * 200)
			sleep_seconds = self.crawling_time 
			print(f"Sleeping for {sleep_seconds} seconds...")
			sleep(sleep_seconds)