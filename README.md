# danbooru-graph
A small script that creates a timeline showing the uploading intensity for a given tag.

# Requirements
**At least** Python 3.7, I haven't tried with older versions so your milleage may vary.

# Installation
1. Clone the Repo
2. Create a virtual environment in the repo: `python3 -m venv venv`
3. Install the requirements: `pip install -r requirements.txt`

#How to use
Run the script with `python danbooru-graph.py [--precision] TAG`.

The output will be generated in the **./output** folder

### Arguments
**TAG**: _Required._ The danbooru tag you want to search.

**--precision, -p**: _Optional._ determines if you want to sort the graph by year (0), year-month (1), or year-month-day (2).

### Example
`python danbooru-graph.py -p 1 suzuhara_lulu`

![Example picture](https://i.imgur.com/PkmQHcC.png)