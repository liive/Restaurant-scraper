import requests
from bs4 import BeautifulSoup

# define headers for the HTTP request to avoid being blocked as a bot
headers = {
    "Accept": "text/htm;,application/xhtml+xml,application/xml;q=0.9,image/avif,iamge/webp/image/apng",
    "Accept-Encoding": "gzip,deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Cache-Control": "max-age=0,no-cache,no-store",
    "Upgrade-Insecure-Requests": "1",
}

# define url to scrape
url = "https://www.yellowpages.ca/search/si/1/restaurants/Toronto+ON"

# define function to scrape the data from the yellow pages website
def scraper_yellow_pages():

    # send a HTTP GET request to the URL with the headers defined above
    response = requests.get(url, headers=headers)

    # parse the HTML content of the response using BeautifulSoup
    response = BeautifulSoup(response.content, "html.parser")

    # initialize an empty dictionary to store the results
    result_dict = {
        "business_name": [],
        "tripadvisor_rating": [],
        "tripadvisor_number_reviews": [],
        "phone_number": [],
        "yp_number_ofratings": [],
        "yp_star_ratings": [],
        "street_address": [],
        "locality": [],
        "region": [],
        "postalcode": [],
    }

    # loop through the first 3 pages of search results
    for i in range(1, 4, 1):

        # construct the URL for the current page of search results
        page = requests.get(
            f"https://www.yellowpages.ca/search/si/{i}/restaurants/Toronto+ON",
            headers=headers,
        )

        # parse the HTML contect of the current page using BeautifulSoup
        soup = BeautifulSoup(page.content, "html.parser")

        # find all the listings on the current page
        container = soup.find_all("div", attrs={"class": "listing__content__wrapper"})
        for c in container:

            # extract the business name
            business_name = c.find_all(
                "a", attrs={"class": "listing__name--link listing__link jsListingName"}
            )
            if business_name:
                for j in business_name:
                    if j:
                        result_dict["business_name"].append(j.text)
                    else:
                        result_dict["business_name"].append("Error")
            else:
                result_dict["business_name"].append(None)

            # extract the TripAdvisor rating
            tripadvisor_rating = c.find_all("img", attrs={"class": "tripAdvisorImg"})
            if tripadvisor_rating:
                for j in tripadvisor_rating:

                    if j:
                        result_dict["tripadvisor_rating"].append(j.get("src"))
                    else:
                        result_dict["tripadvisor_rating"].append(j.get("data-src"))

            else:
                result_dict["tripadvisor_rating"].append(None)

            # extract the number of TripAdvisor reviews
            tripadvisor_number_reviews = c.find(
                "span", attrs={"class": "listing__link listing-quote"}
            )
            if tripadvisor_number_reviews:

                result_dict["tripadvisor_number_reviews"].append(
                    tripadvisor_number_reviews.text
                )
            else:
                result_dict["tripadvisor_number_reviews"].append(None)

            # extract the phone number
            phone_number = c.find_all("li", attrs={"class": "mlr__submenu__item"})
            if phone_number:
                for j in phone_number:
                    if j:
                        result_dict["phone_number"].append(j.text)
                    else:
                        result_dict["phone_number"].append(j.text)
            else:
                result_dict["phone_number"].append(None)

            # extract the number yellow pages ratings
            yp_number_ofratings = c.find_all(
                "a", attrs={"class": "listing__ratings__count listing__link"}
            )

            if yp_number_ofratings:
                for j in yp_number_ofratings:
                    if j:

                        result_dict["yp_number_ofratings"].append(j.text.strip()[1:-1])
                    else:
                        result_dict["yp_number_ofratings"].append(j.text.strip()[1:-1])

            else:
                result_dict["yp_number_ofratings"].append(None)

            # extract the yellow pages star ratings
            yp_star_ratings = c.find_all(
                "span", attrs={"class": "ypStars jsReviewsChart"}
            )
            if yp_star_ratings:
                for j in yp_star_ratings:
                    if j:
                        result_dict["yp_star_ratings"].append(j.get("title"))
                    else:
                        result_dict["yp_star_ratings"].append(yp_star_ratings)
            else:
                result_dict["yp_star_ratings"].append(None)

            # extract the street adress
            street_address = c.find_all("span", attrs={"itemprop": "streetAddress"})
            if street_address:
                for j in street_address:

                    if j:
                        result_dict["street_address"].append(j.text)
                    else:
                        result_dict["street_address"].append(j.text)

            else:
                result_dict["street_address"].append(None)

            # extract the locality
            locality = c.find_all("span", attrs={"itemprop": "addressLocality"})
            if locality:
                for j in locality:

                    if j:
                        result_dict["locality"].append(j.text)
                    else:
                        result_dict["locality"].append(j.text)
            else:
                result_dict["locality"].append(None)

            # extract the region
            region = c.find_all("span", attrs={"itemprop": "addressRegion"})
            if region:
                for j in region:

                    if j:
                        result_dict["region"].append(j.text)
                    else:
                        result_dict["region"].append(j.text)
            else:
                result_dict["region"].append(None)

            # extract the postal code
            postalcode = c.find_all("span", attrs={"itemprop": "postalCode"})
            if postalcode:
                for j in postalcode:

                    if j:
                        result_dict["postalcode"].append(j.text)
                    else:
                        result_dict["postalcode"].append(j.text)
            else:
                result_dict["postalcode"].append(None)

    # return the dictionary of the results
    return result_dict

