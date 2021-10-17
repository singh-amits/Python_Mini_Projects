import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
# votes = soup.select('.score') [for the score]
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        # title = item.getText() [can use instead of above line]
        href = links[idx].get('href', None)
        #href = item.get('href', None)
        votes = subtext[idx].select('.score')
        # points = votes[idx].getText() [when doing it for points exclusively]
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            # print(points) [to print points]
            # hn.append(title) [only for the title]
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    # return hn [When returnin the hacker news normally and below is with the sorting by votes]
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
