📸 Instagram Follower Bot

A Python automation bot that logs into Instagram, finds followers of a target account, and follows them automatically.
Built with Selenium and environment variable management via .env.

🚀 Features

🔑 Login securely with Instagram credentials (from .env)

🎯 Target any Instagram account to extract followers

🤖 Auto-follow users from that account’s follower list

🛡 Credentials are hidden (no hardcoding passwords)

🧩 Modular design with InstaFollower class

🛠 Tech Stack

Python 3

Selenium – browser automation

dotenv – credential management

Chrome WebDriver

⚙️ Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/DebanilBora/Instagram-follower-bot.git
cd insta-follower-bot

2️⃣ Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install selenium python-dotenv

4️⃣ Download ChromeDriver

Install Google Chrome

Download matching ChromeDriver: https://chromedriver.chromium.org/downloads

Add it to your PATH or project folder

5️⃣ Setup .env file

Create a .env file in the project root with your Instagram credentials:

INSTA_USER=your_username
INSTA_PASS=your_password
TARGET_ACCOUNT=chefsteps

▶️ Usage

Run the bot:

python main.py


Steps the bot performs:

✅ Logs into Instagram

🔍 Navigates to the target account’s followers

📥 Scrolls & fetches followers

🤝 Follows them automatically

⚠️ Disclaimer

This project is for educational purposes only.
Automating Instagram actions may violate Instagram’s Terms of Service
.
Use responsibly on test/dummy accounts.

🏷 Tags

#Python #Selenium #Automation #Instagram #Bot
