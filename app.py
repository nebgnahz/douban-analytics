#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sys

from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print >> sys.stderr, 'Usage: ', sys.argv[0], 'folder'
        exit(-1)

    print 'title, url, rating, my rating, date'

    path = sys.argv[1]
    pages = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    for p in pages:
        data = open(p).read()
        soup = BeautifulSoup(data, "lxml")

        for item in soup.find_all("div", {"class":"status-item"}):
            try:
                title_soup = item.find("div", {"class":"title"})
                title = title_soup.find("a").string
                url = title_soup.find("a")['href']
                public_rating = title_soup.find("strong", \
                                                {"class":"rating_num"}).string
                myrating_soup = item.find("span", {"class":"rating-stars"})
                if myrating_soup: ## I have watched it, extract my rating
                    my_rating = myrating_soup.string.count(unichr(9733))
                else:
                    continue
                    my_rating = -1
                date = item.find("span", {"class":"created_at"})['title']
                print title.encode("utf-8"), ',', url, ',',\
                    public_rating, ',', my_rating, ',', date
            except:
                pass
