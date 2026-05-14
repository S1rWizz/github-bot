<div align="center">
  <img src="https://capsule-render.vercel.sh/content?type=waving&color=0:415a77,50:778da9,100:e0e1dd&height=220&section=header&text=🟢%20GitHub%20Bot&fontSize=50&fontColor=ffffff&animation=fadeIn" width="100%" />
  
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

## 🚀 About the Project

This is a lightweight automation tool designed to keep your GitHub contribution graph active. By automating daily code updates to a designated repository, it helps maintain your green activity streaks effortlessly while you practice your coding skills.

---

## 💻 Installation & Usage

Follow these steps to get the bot running locally on your machine:

### 1. Download the Project
* Click the green **Code** button at the top right of this repository page.
* Click **Download ZIP** and extract the files to a folder on your computer.

### 2. Install the Dependencies
Open your terminal or command prompt inside the project folder and install the required modules by running:
```bash
pip install pygithub python-dotenv
```

### 3. Setup Your Token
To give the bot access to your repository:
* Go to your GitHub **Profile Picture** &rarr; **Settings** &rarr; **Developer settings**.
* Click **Personal access tokens** &rarr; **Tokens (classic)** *(Avoid the newer fine-grained/filtered ones)*.
* Click **Generate new token (classic)**, check the `repo` permission box, and copy the generated token.

### 4. Create the Environment File
Create a new file named exactly `.env` in the project root folder. Copy, paste, and update the following details:

```env
tok=ghp_YourActualTokenHere
repo_name=YOUR_REPOSITORY_NAME
content=Practise Questions for leetcode, hackerrank, and unstop
commit_message=Updated README
```

> ⚠️ **Crucial Security Check:** Ensure your `.gitignore` file includes `.env` so you don't accidentally push your private token to your public history!

### 5. Run the Bot
Once everything is set up, launch the script from your terminal:
```bash
python main.py
```

---

## 📂 Customization Fields

<table width="100%">
  <thead>
    <tr>
      <th width="30%" align="left">🔧 Variable Name</th>
      <th width="70%" align="left">📝 What it Does & How to Customize</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>tok</code></td>
      <td>Your secure GitHub Personal Access Token (Classic).</td>
    </tr>
    <tr>
      <td><code>repo_name</code></td>
      <td>The precise name of the target repository you want the bot to update (preferably choose its <code>README.md</code>).</td>
    </tr>
    <tr>
      <td><code>content</code></td>
      <td><strong>Completely Customizable!</strong> Write whatever text or practice code logs you want to inject inside the repository file on each run.</td>
    </tr>
    <tr>
      <td><code>commit_message</code></td>
      <td><strong>Completely Customizable!</strong> Type the exact text you want to show up as the message in your GitHub commit history log.</td>
    </tr>
  </tbody>
</table>

---

<div align="center">
  <img src="https://capsule-render.vercel.sh/content?type=slice&color=778da9&height=30&section=footer" width="100%" />
</div>

<p align="right">
  <sub>Built to keep the daily streak active. Happy automated coding! 🚀</sub>
  <br />
  ⚡ <i>Maintained by <b><a href="https://github.com/SirWizz">@SirWizz</a></b></i>
</p>