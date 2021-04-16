from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
def data_scrape():

    scrape_site = "https://redplanetscience.com/"

    browser.visit(scrape_site)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs (html, 'html.parser')
    #display (soup)

    find_title = soup.find_all ("div",class_="content_title")
    #find_title

    find_title = find_title[13].text
    #find_title

    find_para = soup.find_all ("div",class_="article_teaser_body")
    #find_para

    find_para = find_para[13].text
    #find_para

    get_pic = "https://spaceimages-mars.com/"
    browser.visit(get_pic)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs (html, 'html.parser')

    #display (soup)

    print_image = soup.find("a",class_="showimg fancybox-thumbs")["href"]
    #print (print_image)

    url = get_pic+print_image
    #print (url)

    get_data = "https://galaxyfacts-mars.com/"
    html_read = pd.read_html(get_data)
    #display (html_read)

    table = html_read [1]
    #table

    table.columns=["facts", "value"]
    back_html = table.to_html(index=False)
    #back_html

    pic_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(pic_url)
    html = browser.html
    soup = bs (html,'html.parser')

    #display (soup)

    item_name = []
    desc = soup.find_all("div",class_="description")
    for i in desc:
        title=i.find("h3").text
        find_url = i.find("a")["href"]
        full_url = "https://astrogeology.usgs.gov/"+find_url
        browser.visit (full_url)
        content = browser.html
        soup = bs (content,'html.parser')
        find_link = "https://astrogeology.usgs.gov/"+soup.find("img", class_="wide-image")["src"]
        item_name.append ({"title":title,"img_url": find_link})
    #print_pic = soup.find("a", class_="itemLink product-item")["href"]
    #print (item_name)

    mars_data = {}
    mars_data["title"]=find_title
    mars_data["paragraph"]=find_para
    mars_data["image"]=url
    mars_data["mars_facs"]=back_html
    mars_data["hemisphere_image"]=item_name
    return mars_data



