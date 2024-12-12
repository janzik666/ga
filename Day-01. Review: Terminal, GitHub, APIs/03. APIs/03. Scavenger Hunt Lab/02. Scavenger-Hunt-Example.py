""" scavenger-hunt-example-solution.py """
import requests

LOCALE = "us_EN"
MAXINPUT = 5

while True:
    try:
        quantity = max(
            min(int(input("How many books would you like to read? ")), MAXINPUT), 1)
        break
    except SyntaxError:
        print("Please enter an integer.")

url = f"https://fakerapi.it/api/v1/books?_quantity={quantity}&_LOCALE={LOCALE}"
books = requests.get(url, timeout=10)
parsed_books_result = books.json()["data"]
for x in parsed_books_result:
    print(f'{x["title"]} by {x["author"]}. Published {x["published"]}')
print("\nWhy don't you read one of these books? Because they don't exist!")
