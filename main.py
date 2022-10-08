enterQuery = input("What do you want to search?")
print(f"Searching for {enterQuery}")


from googlesearch import search
results = search(enterQuery, num_results=100)
for result in results:
    print(result)