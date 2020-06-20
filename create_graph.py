import matplotlib.pyplot as plt
import dateutil.parser
import requests
import os
import argparse


class TagNotFound(Exception):
    pass


def load_tag(tag):
    """Loads every posts in a tag and return them"""
    posts = []
    page = 1
    while True:
        print(f"Loading page {page}")
        url = f"https://danbooru.donmai.us/posts.json?page={page}&tags={tag}&limit=200"
        response = requests.get(url)
        res_json = response.json()
        if len(res_json) == 0:
            break
        else:
            posts.extend(res_json)
        page += 1

    return posts


def create_graph(tag, precision=0):
    """Creates a graph from the given tag"""
    posts = load_tag(tag)
    data = {}

    for post in posts:
        date = dateutil.parser.parse(post["created_at"])
        date_string = f"{date.year}"
        if precision == 1:
            date_string += f"-{date.month}"
        if precision == 2:
            date_string += f"-{date.month}-{date.day}"
        if date_string not in data:
            new_dict = {date_string: 1}
            data.update(new_dict)
        else:
            data[date_string] += 1

    dates = []
    values = []
    for x in sorted(data):
        dates.append(x)
        values.append(data[x])

    plt.bar(dates, values)
    plt.title(f"Posts tagged with {tag}")
    plt.xlabel("Date")
    plt.ylabel("Nb. of posts")
    fig = plt.gcf()
    fig.set_size_inches(len(dates), 10.5, forward=True)
    fig.tight_layout()
    if not os.path.exists('output'):
        os.makedirs('output')
    fig.savefig(f"./output/{tag}.png", dpi=100, bbox_inches='tight', pad_inches=0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a graph from a Danbooru tag')
    parser.add_argument('tag', metavar='TAG', type=str,
                        help='the tag to search')
    parser.add_argument('-p', '--precision', type=int, default=0,
                        help="0 = Year, 1 = Year-Month, 2 = Year-Month-Day")
    args = parser.parse_args()
    if len(requests.get(f"https://danbooru.donmai.us/posts.json?page=1&tags={args.tag}").json()) == 0:
        raise TagNotFound("Couldn't find this tag. Are you sure it exists ?")

    create_graph(args.tag, args.precision)
