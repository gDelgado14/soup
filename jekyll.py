




def post_create(post):

    """
    Creates Jekyll compatible HTML file!
    """

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


    post_front_matter = """---
    layout: [the_layout]
    title: [the_title]
    ---"""

    ignore = [u"Contact", u"Contact form 1"]
    special = [u"About", u"Forty-Eight"]

    # make sure page is required
    if page['title'] not in ignore:





        # regular post
        if page['title'] not in special:

            date = str(post['date']).replace(",", "").split(" ")

            year = date[3]
            month = date_ref[date[2]]
            day = date[1]


            title = str(my_dict['title']).replace(" ", "-")

            file_name = "-".join((year,month,day,title)) + ".html"


            """
                ##############################

                write:
                    - front matter
                    - page['text']

                into a file named 'file_name'

                then save to _posts directory

                ##############################
            """

            """
                merge file: https://gist.github.com/gDelgado14/dd7c7b7332d766b0740c
            """


        elif page['title'] == u"About":







