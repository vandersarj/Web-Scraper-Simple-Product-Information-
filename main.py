import requests
from bs4 import BeautifulSoup

def scrape_product_info(url):
  # Make a GET request to the target URL
  response = requests.get(url)
  
  # Check for successful response status code
  if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Identify elements containing product information (replace with selectors specific to the target website)
    product_title = soup.find("h1", class_="product-title")  # Replace with appropriate class/id selector
    product_price = soup.find("span", class_="product-price")  # Replace with appropriate class/id selector
    product_description = soup.find("div", class_="product-description")  # Replace with appropriate class/id selector
    
    # Extract data from the identified elements (if found)
    if product_title:
      title = product_title.text.strip()
    else:
      title = "N/A"
    if product_price:
      price = product_price.text.strip()
    else:
      price = "N/A"
    if product_description:
      description = product_description.text.strip()
    else:
      description = "N/A"
    
    # Return product information dictionary
    return {
      "title": title,
      "price": price,
      "description": description
    }
  else:
    print(f"Error: Failed to access the URL. Status code: {response.status_code}")
    return None

def main():
  # Get user input for target URL
  url = input("Enter the URL of a product page: ")
  
  # Scrape product information
  product_info = scrape_product_info(url)
  
  # Display scraped information (if successful)
  if product_info:
    print("Scraped Product Information:")
    print(f"Title: {product_info['title']}")
    print(f"Price: {product_info['price']}")
    print(f"Description: {product_info['description']}")
  else:
    print("Failed to scrape product information.")

if __name__ == "__main__":
  main()
