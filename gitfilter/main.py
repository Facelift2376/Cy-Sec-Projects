from github import Github

github_token = "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"

g = Github(github_token)

def search_github_repositories(keyword, num_results=10):
    try:
        repositories = g.search_repositories(query=keyword, sort="stars", order="desc")
        for repo in repositories[:num_results]:
            print(f"Repository Name: {repo.name}")
            print(f"Owner: {repo.owner.login}")
            print(f"Description: {repo.description}")
            print(f"Stars: {repo.stargazers_count}")
            print(f"URL: {repo.html_url}")
            print("=" * 50)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    search_keyword = input("Enter a keyword or topic to search for on GitHub: ")
    num_results = int(input("Enter the number of results to fetch: "))

    search_github_repositories(search_keyword, num_results)
