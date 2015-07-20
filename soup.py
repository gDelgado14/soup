"""
        https://beautiful-soup-4.readthedocs.org/en/latest/

from bs4 import BeautifulSoup


#Create a soup object to traverse XML
soup = BeautifulSoup(open("wordpress.xml"), "xml")

items = soup.find_all('content:encoded')
#items = soup.find_all('item')

#thingers = items[45].contents

#content = items.find_all('content')

print(items)

# navigate through each item tag
for item in items:

    post = item.find_all("content:encoded")

    print(post)



"""


"""

    Initial code drawn from: https://code.activestate.com/recipes/551792-convert-wordpress-export-file-to-multiple-html-fil/

"""


import string, os, sys, getopt
from xml.dom import minidom
from jekyll import post_create

dom = minidom.parse("wordpress.xml")

blog = []  # list that will contain all posts

for node in dom.getElementsByTagName('item'):
    post = dict()

    #print node

    # only work on posts:
    # for something to be a post it must have a <title> attr
    # as well as a <content:encoded> attr
    # everything else is metadata

    if node.getElementsByTagName('title')[0].firstChild is not None and \
    node.getElementsByTagName('content:encoded')[0].firstChild is not None:

        post["title"] = node.getElementsByTagName('title')[0].firstChild.data
        post["date"] = node.getElementsByTagName('pubDate')[0].firstChild.data
        post["author"] = node.getElementsByTagName('dc:creator')[0].firstChild.data
        post["id"] = node.getElementsByTagName('wp:post_id')[0].firstChild.data
        post["text"] = node.getElementsByTagName('content:encoded')[0].firstChild.data

        # Get the categories
        tempCategories = []
        for subnode in node.getElementsByTagName('category'):
             tempCategories.append(subnode.getAttribute('nicename'))
        categories = [x for x in tempCategories if x != '']
        post["categories"] = categories

        # Add post to the list of all posts
        blog.append(post)

    # find image links and save to 'downloads' directory
    elif node.getElementsByTagName('wp:attachment_url')[0].firstChild is not None:

for page in blog:

    post_create(page)

    #print page

    #print str(page['text'])



