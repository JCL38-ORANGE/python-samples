import string

def on_file():
    urls = set()
    hurls = {}
    try:
        with open("data/post.log", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith('POST '):
                    verb, url, version = line.split()
                    urls.add(url)
        print(urls)
    except OSError as err:
        print("OS error: {0}".format(err))
