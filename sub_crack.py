
# # !/usr/bin/python3

# Old One
# import requests

# domain = input("Enter domain: ")
# file = open("wordlist.txt", "r")

# content = file.read()

# subdomains = content.splitlines()

# for subdomain in subdomains:
#     url1 = f"http://{subdomain}.{domain}"
#     url2 = f"https://{subdomain}.{domain}"
#     try:
#         requests.get(url1)
#         print(f"Discovered URL: {url1}")
#         requests.get(url2)
#         print(f"Discovered URL{url2}")
#     except requests.ConnectionError:
#         pass



#!/usr/bin/python3

# New One

import requests
from concurrent.futures import ThreadPoolExecutor

def discover_url(subdomain, domain):
    url1 = f"http://{subdomain}.{domain}"
    url2 = f"https://{subdomain}.{domain}"
    try:
        requests.get(url1)
        print(f"Discovered URL: {url1}")
        requests.get(url2)
        print(f"Discovered URL: {url2}")
    except requests.ConnectionError:
        pass

if __name__ == "__main__":
    domain = input("Enter domain: ")
    file = open("wordlist.txt", "r")

    content = file.read()

    subdomains = content.splitlines()

    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
        # Use executor.map to apply the function to each subdomain in parallel
        executor.map(lambda subdomain: discover_url(subdomain, domain), subdomains)

