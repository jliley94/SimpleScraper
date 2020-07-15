import requests
import re
import SimpleScraper
import SimpleEmail

requestedColor = "150"
requestedSize = "S"
link = "https://www.nastygal.com/gb/take-the-easy-option-jumper-and-pant-lounge-set/AGG53129.html?color=150"
match = "//div[contains(@class, 'size-attribute')] //li[contains(@class, 'selectable') and contains(@class, 'variation-value')] //span[contains(@class, 'swatchanchor')]"

elementArray = SimpleScraper.ScrapeHTML(link, match)

# loop through html to check for required elements and values
for element in elementArray:
    # For each element we can easily get back the URL
    if (element.get('data-href') != None):
        print(element.get('data-href'))
        # get color from url attribute
        color = re.search("(?<=color=).[^&]*",
                          element.get('data-href')).group()
        print(color)
        if (requestedColor == color):
            print("color match..")
            # get size from title string
            if(requestedSize == element.get('title')[-1:]):
                print("We have a match!!!")
                # send notification
                SimpleEmail.send_simple_message(
                    "SimpleScarper Detected new stock", "Your NastyGal alert has been triggered. Link: {}".format(link))
