enterQuery = input("What do you want to search?")
print(f"Searching for {enterQuery}")

# from googlesearch import search
# results = search(enterQuery, num_results=100)
# for result in results:
#     print(result)

# from bing-image-downloader import google_images_download   #importing the library
#
# response = google_images_download.googleimagesdownload()   #class instantiation
#
# arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
# paths = response.download(arguments)   #passing the arguments to the function
# print(paths)   #printing absolute paths of the downloaded images

from bing_image_downloader import downloader

downloader.download(enterQuery, limit=100, output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60)