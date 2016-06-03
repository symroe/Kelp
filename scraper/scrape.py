from urllib.parse import urlencode
import re
import os
import json

import requests
from bs4 import BeautifulSoup


class GCloudScraper(object):

    def __init__(self):
        self.base_url = "https://www.digitalmarketplace.service.gov.uk"
        self.has_next = True


    def _get_request(self, path, params=None):
        path = path.strip('/')
        url = "{}/{}".format(self.base_url, path)
        if params:
            url = "{}?{}".format(url, urlencode(params))
        print(url)
        return requests.get(url)

    def get_results(self, page=1):
        req = self._get_request('g-cloud/search', {'page': page})
        soup = BeautifulSoup(req.content, 'html.parser')
        self.has_next = bool(soup.find('li', {'class': 'next'}))
        return soup

    def parse_results_to_urls(self, results):
        return [link['href']for link in
            results.findAll('a', href=re.compile('g-cloud/services/[\d]+'))]

    def get_result_page(self, result_url):
        service_id = result_url.split('/')[-1]
        if os.path.exists('data/{}.json'.format(service_id)):
            return None
        req = self._get_request(result_url)
        return BeautifulSoup(req.content, 'html.parser')

    def parse_result_page_to_json(self, page):
        data = {}
        data['company_name'] = page.find(
            'header', {'class': 'page-heading-smaller'}
            ).find('p', {'class': "context"}).text
        data['service_name'] = page.find(
            'header', {'class': 'page-heading-smaller'}
            ).find('h1').text
        data['service_id'] = page.find(
            'div', {'class': 'service-id'}
            ).text.strip('\n')
        data['page_content'] = page.find(
            'main', {'id': 'content'}
            ).prettify()
        return data

    def save_page(self, data, service_id):
        with open('data/{}.json'.format(service_id), 'w') as data_file:
            data_file.write(json.dumps(data))


if __name__ == "__main__":
    g = GCloudScraper()
    page = 1
    while g.has_next:
        for link in g.parse_results_to_urls(g.get_results(page)):
            result_page = g.get_result_page(link)
            if result_page:
                data = g.parse_result_page_to_json(result_page)
                g.save_page(data, data['service_id'])
        page += 1
