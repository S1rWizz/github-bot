  <p align="center">
    <strong>Auto-create commits to seamlessly keep your contribution graph green and glowing. 😉</strong>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/API-PyGitHub-green?style=for-the-badge&logo=github&logoColor=white" alt="PyGitHub" />
    <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License" />
  </p>
</div>

---

## 🚀 Overview

A lightweight automation script that updates a targeted repository file (preferably your `README.md`) on demand. Perfect for tracking consistency, testing out automation workflows, or just keeping that contribution streak beautifully unbroken. 

---

## 🛠️ Step-by-Step Configuration

### 1. Grab Your Personal Access Token (PAT)
To talk to the GitHub API, you need a classic token to act as your passkey:
* Go to your **Profile Picture** &rarr; **Settings** &rarr; **Developer settings**.
* Click on **Personal access tokens** &rarr; **Tokens (classic)** *(Avoid the newer fine-grained/filtered ones)*.
* Generate a new token and give it the required permissions (checking the `repo` scope is usually plenty).
* Copy it immediately!

### 2. Set Up the Configuration File
Create a file named exactly `.env` in your project's main directory and fill it out like this:

```env
tok=ghp_YourActualTokenHere
repo_name=YOUR_REPOSITORY_NAME
content=Practise Questions for leetcode, hackerrank, and unstop
commit_message=Updated README