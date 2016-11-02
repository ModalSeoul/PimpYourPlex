import cfscrape
import argparse

# cfscrape - bypasses cloudflare
scraper = cfscrape.create_scraper()

# argparse - Loads and parses args
parser = argparse.ArgumentParser(description='args')
parser.add_argument('-c', '--count', help='Amount of episodes')
parser.add_argument('-t', '--title', help='Title of show')

"""
e.g:
    print(args.count)
"""
args = parser.parse_args()
