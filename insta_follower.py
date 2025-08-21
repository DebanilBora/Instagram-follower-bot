import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException

from dotenv import load_dotenv
import time


load_dotenv()

INSTA_USER = os.getenv("INSTA_USER")
INSTA_PASS = os.getenv("INSTA_PASS")
TARGET_ACCOUNT = os.getenv("TARGET_ACCOUNT", "chefsteps")
SCROLLS = 5


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()  # requires ChromeDriver installed
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        wait = WebDriverWait(self.driver, 20)

        # Accept cookies if popup appears
        try:
            cookie_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Only allow essential cookies']"))
            )
            cookie_btn.click()
        except:
            pass

        # Fill in login form
        user_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        pass_input = self.driver.find_element(By.NAME, "password")

        user_input.send_keys(username)
        pass_input.send_keys(password)
        pass_input.send_keys(Keys.ENTER)

        # Handle "Save login info" popup
        try:
            not_now_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not now')]"))
            )
            not_now_btn.click()
        except:
            pass

        # Handle notifications popup
        try:
            notif_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )
            notif_btn.click()
        except:
            pass

        print("✅ Logged in successfully.")

    def find_followers(self, target_account, scrolls=5):
        self.driver.get(f"https://www.instagram.com/{target_account}/")
        wait = WebDriverWait(self.driver, 20)

        try:
            print("🔎 Looking for followers link...")

            # Try different UI strategies
            try:
                followers_link = wait.until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "followers"))
                )
            except:
                try:
                    followers_link = wait.until(
                        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/followers')]"))
                    )
                except:
                    followers_link = wait.until(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'followers')]/.."))
                    )

            followers_link.click()
            print("✅ Opened followers list")
        except Exception as e:
            print("❌ Could not click followers link:", e)
            return

        # Wait for modal
        try:
            modal = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
            )
            print("✅ Followers modal appeared.")
        except Exception as e:
            print("❌ Followers modal did not appear:", e)
            return

        # Scroll modal
        for i in range(scrolls):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            print(f"📜 Scrolled {i + 1} times")
            time.sleep(2)

    def follow(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            buttons = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@role='dialog']//button[normalize-space()='Follow']"))
            )
            print(f"✅ Found {len(buttons)} follow buttons.")
        except:
            print("❌ Could not find follow buttons.")
            return

        for button in buttons:
            try:
                button.click()
                print("👉 Followed a user.")
                time.sleep(1)
            except ElementClickInterceptedException:
                print("⚠️ Intercepted — trying to close popup.")
                try:
                    cancel_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                    cancel_btn.click()
                    print("❎ Closed popup.")
                except:
                    print("❌ Failed to close popup.")
            except StaleElementReferenceException:
                print("⚠️ Stale element — skipping.")


if __name__ == "__main__":
    bot = InstaFollower()
    bot.login(INSTA_USER, INSTA_PASS)
    bot.find_followers(TARGET_ACCOUNT, SCROLLS)
    bot.follow()
