

# https://stackoverflow.com/questions/12944678/using-unicodedata-normalize-in-python-2-7/12947127#12947127
from unidecode import unidecode

def post_create(post):

    """
    Creates Jekyll compatible HTML file!
    """


    # used to convert wordpress date format into Jekyll date format
    date_ref = {
    'Jan': '1',
    'Feb': '2',
    'Mar': '3',
    'Apr': '4',
    'May': '5',
    'Jun': '6',
    'Jul': '7',
    'Aug': '8',
    'Sep': '9',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
    }


    post_front_matter = """---\nlayout: [the_layout]\ntitle: [the_title]\n---"""

    ignore = [u"Contact", u"Contact form 1"]
    special = [u"About", u"Forty-Eight"]

    # make sure page is required
    if post['title'] not in ignore:

        # regular post
        if post['title'] not in special:

            date = unidecode(post['date']).replace(",", "").split(" ")

            year = date[3]
            month = date_ref[date[2]]
            day = date[1]

            # if post date year is -0001 then it is a draft post
            jekyll_dir = '_drafts/' if year == '-0001' else '_posts/'

            # using regex would have been nicer
            title = unidecode(post['title']).replace("/", "").replace(":", "").replace(" ", "-")

            file_name = "-".join((year, month, day, title)) + ".html"

            # create new file
            f = open('root/' + jekyll_dir + file_name, 'w')

            post_front_matter = post_front_matter.replace("[the_layout]", "post").replace("[the_title]", title)

            if post['catogories']:
                post_front_matter = post_front_matter[:-3] + 'tags: '
                for cat in posts['categories']:
                    post_front_matter += cat + ' '
                post_front_matter += '\n---'

            space = '\n'

            f.write(post_front_matter + space + unidecode(post['text']))

            f.close()


        #elif page['title'] == u"About":





