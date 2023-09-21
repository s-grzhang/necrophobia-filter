'''
In this example we iterating over 4 search queries,
doing pagination on each query until results is present,
and extracting original size image + optionally saving locally
'''

import urllib.request
from serpapi import GoogleSearch
import json

def serpapi_get_google_images():
    image_results = []

    for query in ['sahelanthropus tchadensis reconstruction','Orrorin tugenensis reconstruction','Ardipithecus reconstruction','Australopithecus reconstruction', 'Kenyanthropus platyops reconstruction','Paranthropus reconstruction','Homo habilis reconstruction','Homo rudolfensis reconstruction', 'Homo erectus reconstruction','Homo antecessor reconstruction', 'Homo heidelbergensis reconstruction','Homo naledi reconstruction','Homo neanderthalensis reconstruction', 'Homo floresiensis reconstruction',]:
        # search query parameters
        params = {
            "engine": "bing",  # search engine. Google, Bing, Yahoo, Naver, Baidu...
            "q": query,  # search query
            "tbm": "isch",  # image results
            "num": "30",  # number of images per page
            "ijn": 0,  # page number: 0 -> first page, 1 -> second...
            "api_key": "00df3a2537529a981ad15222adf6c4e2cfed0c5677f613d3dd4785b2e495997b",  # https://serpapi.com/manage-api-key
            # other query parameters: hl (lang), gl (country), etc
        }

        search = GoogleSearch(params)  # where data extraction happens

        images_is_present = True
        while images_is_present:
            results = search.get_dict()  # JSON -> Python dictionary

            # checks for "Google hasn't returned any results for this query."
            if "error" not in results:
                for image in results["images_results"]:
                    if image["original"] not in image_results:
                        image_results.append(image["original"])

                # update to the next page
                params["ijn"] += 1
            else:
                print(results["error"])
                images_is_present = False

    # -----------------------
    # Downloading images

    for index, image in enumerate(results["images_results"], start=1):
        print(f"Downloading {index} image...")

        opener = urllib.request.build_opener()
        opener.addheaders = [("User-Agent",
                              "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")]
        urllib.request.install_opener(opener)

        urllib.request.urlretrieve(image["original"], f"SerpApi_Images/original_size_img_{index}.jpg")

    print(json.dumps(image_results, indent=2))
    print(len(image_results))