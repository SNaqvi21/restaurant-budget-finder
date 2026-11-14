print("RELEVANT FOOD OUTLETS")
# The objective was to retrieve food outlet/resturant info from
# an online API to identify which restaurants were affordable
# within a given budget & return their names.

# 1. I had to call an API to retrieve food outlets in the city.
# 2. Retrieves all results even when spread across multiple pages.
# 3. Checks the estimated cost of for two people,
# 4. Includes outlets costing <= the budget(maxCost)
# 5. Returns their name in the same order as the API.
# e.g for Denver with maxCost of 50, exp output =>BKC Dive Vedge

# python library that allows my program to comm with
# websites + APIs using HTTP
import requests


# preparing the program, url stores the API endpoint
# result[] empty list in which budget outlets will be added
# page=1 creates int var tracks which API page currently requesting
def getRelevantFoodOutlets(city, maxCost):
    url = (
        "https://jsonmock.hackerrank.com"
        "/api/food_outlets"
    )
    result = []
    page = 1

# Because we need to request unknown num of pages, the API will
# tell us how many exist using the while loop/break.
# requests.get() sends HTTP GET request
# params is a python dict & converts K-V into URL query paramaters:
# ?city=Denver&page=1 the .json()method converts JSON response into
# python objects, typically a dict containing lists + other dicts
# result is stored in the variable response.
    while True:
        response = requests.get(
            url,
            params={"city": city, "page": page}
        ).json()

# response["data"] accesses list of restaurants in JSON response.
# the for loop examines each restaurant individually and checks
# if the estimated cost is within budget.
# then add/append restaurant name to the end of the list.
        for outlet in response["data"]:
            if outlet["estimated_cost"] <= maxCost:
                result.append(outlet["name"])

# An API contains records, rather than returning all at once
        # it returns results into smaller groups/pages
# response["total_pages"] tells us how many pages exist
# when all pages have been processed, the loop breaks.
# otherwise/else page += 1 increases page num by 1.
        if page >= response["total_pages"]:
            break

        page += 1

# the completed list returns back to code that called function
    return result

if __name__ == "__main__":
    city = input("Enter city: ")
    budget = int(input("Maximum cost: "))

    outlets = getRelevantFoodOutlets(
        city, budget
    )

    for name in outlets:
        print(name)