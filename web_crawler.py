import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to fetch a web page
def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error if the request fails
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Function to extract links from a page
def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()

    # Find all anchor tags with href attributes
    for anchor in soup.find_all('a', href=True):
        link = urljoin(base_url, anchor['href'])  # Handle relative URLs
        links.add(link)

    return links

# Main function to crawl a single page
def crawl(url):
    html = fetch_page(url)
    if html:
        links = extract_links(html, url)
        print(f"Found {len(links)} links on {url}:")
        for link in links:
            print(link)

if __name__ == "__main__":
    # Start crawling from this URL
    start_url = "https://www.linkedin.com/"  # Replace with the URL you want to crawl
    crawl(start_url)
