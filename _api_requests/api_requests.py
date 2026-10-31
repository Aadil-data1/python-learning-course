import requests # # Import the requests library so Python can send HTTP requests to websites/APIs


 # Search settings sent to the API as part of the web address (query parameters)
params = {
    "title" : "The Lord of the Rings",  # the book title we want to search for

    "limit" : 5   # return at most 5 results
}

try:
    # timeout=10 stops the program from waiting forever if the server is slow.

  response = requests.get("https://openlibrary.org/search.json", params = params, timeout = 10)  # servers response stored into response

 #Raise an HTTPError if the server replied with an error code (404, 500, etc.)
  response.raise_for_status()

 

  data = response.json()   # convert the reply from json into python dictionary


  for doc in data["docs"]:
   print(doc["title"], doc.get("author_name"))

except requests.exceptions.Timeout:
    # The server took longer than 10 seconds to reply
    print("The request timed out. Check your connection and try again.")

except requests.exceptions.RequestException:
    print(" There was a problem with API request")

