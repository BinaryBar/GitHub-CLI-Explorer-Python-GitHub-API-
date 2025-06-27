import requests

def fetch_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def display_user_info(user):
    print(f"\n👤 Name: {user.get('name')}")
    print(f"🔗 Profile: {user.get('html_url')}")
    print(f"📦 Public Repositories: {user.get('public_repos')}")
    print(f"👥 Followers: {user.get('followers')} | Following: {user.get('following')}")
    print(f"📍 Location: {user.get('location')}\n")

def display_repos_info(repos):
    print("📁 Repositories:\n")
    for repo in repos:
        print(f"- {repo['name']}: ⭐ {repo['stargazers_count']} | 🍴 {repo['forks_count']}")
        print(f"  📚 Language: {repo['language']} | 🔗 {repo['html_url']}")
        print()

if __name__ == "__main__":
    print("🔍 GitHub CLI Explorer")
    username = input("Enter GitHub username: ").strip()

    user = fetch_user(username)
    if not user:
        print("❌ User not found!")
    else:
        display_user_info(user)
        repos = fetch_repos(username)
        if repos:
            display_repos_info(repos)
        else:
            print("⚠️ No public repositories found.")
