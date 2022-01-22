import requests
import re


def get_quote(name=None, category="dev"):
    url = f"https://api.chucknorris.io/jokes/random?category={category}"
    quote = requests.get(url).json()["value"]

    if name:
        quote = re.sub("Norris'\s", "Norris's ", quote, flags=re.I)
        quote = re.sub("(Chuck.?Norris|Chuck|Norris)", name.title(), quote, flags=re.I)

    return quote


def get_gh_user_info(username):
    url = f"https://api.github.com/users/{username}"
    return requests.get(url).json()


if __name__ == "__main__":
    print(get_quote())
