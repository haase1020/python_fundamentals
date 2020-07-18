import requests


def create_query(languages, min_stars=50000):
    query = f"starts:>{min_stars} "

    for language in languages:
        query += f"language: {language} "

    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):

    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    query = create_query(languages)
    parameters = {"q": query, "sort": "stars", "order": "desc"}

    response = requests.get(gh_api_repo_search_url, params=parameters)

    response_json = response.json()["items"]
    return response_json


if __name__ == "__main__":
    # have a main method here

    languages = ["Python", "Javascript", "Ruby"]
    query = create_query(languages)
    print("query is: ", query)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"{name} is a {language} repo with {stars} number of stars")
