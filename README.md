# 🏠 Web Scraper to Form Automation

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Parsing-59666C?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A Python automation tool that scrapes real estate property listings from a Zillow clone and automatically submits the extracted data into a Google Form using Selenium — end-to-end, with zero manual input.

---

## 📌 What It Does

1. **Scrapes** property listings (address, price, link) from a Zillow clone site using `requests` + `BeautifulSoup`
2. **Automates** Google Form submission for every listing using `Selenium`
3. **Handles errors gracefully** — skips failed entries and continues processing

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| HTTP Requests | ![Requests](https://img.shields.io/badge/requests-2.x-FF6B6B?style=flat-square&logo=python&logoColor=white) |
| HTML Parsing | ![BS4](https://img.shields.io/badge/BeautifulSoup4-parsing-59666C?style=flat-square&logo=python&logoColor=white) |
| Browser Automation | ![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=flat-square&logo=selenium&logoColor=white) |
| Target Site | [Zillow Clone](https://appbrewery.github.io/Zillow-Clone/) |

---

## 📂 Project Structure

```
web-scraper-to-form-automation/
│
├── main.py         # Core script: scraping + form automation
├── README.md
└── LICENSE
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/qusai-Kagalwala/web-scraper-to-form-automation.git
cd web-scraper-to-form-automation
```

### 2. Install dependencies

```bash
pip install requests beautifulsoup4 selenium
```

### 3. Install ChromeDriver

Make sure [ChromeDriver](https://chromedriver.chromium.org/downloads) is installed and matches your Chrome browser version.

### 4. Configure the Google Form URL

In `main.py`, replace the `FORM_URL` value with your own Google Form link:

```python
FORM_URL = "https://forms.gle/your-form-link-here"
```

> ⚠️ **Important:** Your Google Form must have exactly **3 text fields** in this order:
> 1. Address
> 2. Price
> 3. Property Link

---

## 🚀 Usage

```bash
python main.py
```

The script will:
- Scrape all listings from the Zillow clone
- Open Chrome automatically
- Submit each listing to your Google Form
- Print a ✅ or ❌ status for each entry

**Sample output:**
```
Links: 30, Addresses: 30, Prices: 30
✅ Submitted entry 1
✅ Submitted entry 2
❌ Error on listing 5: element not found
✅ Submitted entry 6
...
```

---

## 🔍 How It Works

### Step 1 — Scraping

```python
soup = BeautifulSoup(response.text, "html.parser")

all_links     = [link["href"] for link in soup.select(".StyledPropertyCardDataWrapper a")]
all_addresses = [addr.get_text().strip() for addr in soup.select(".StyledPropertyCardDataWrapper address")]
all_prices    = [price.get_text().split("+")[0] for price in soup.select(".PropertyCardWrapper span") if "$" in price.text]
```

### Step 2 — Form Automation

```python
driver.get(FORM_URL)
inputs = driver.find_elements(By.XPATH, '//input[@type="text"]')

inputs[0].send_keys(address)   # Address field
inputs[1].send_keys(price)     # Price field
inputs[2].send_keys(link)      # Link field

submit_button.click()
```

Selenium uses **explicit waits** (`WebDriverWait`) instead of `sleep()` for reliability, with a 2-second delay between submissions to avoid rate limiting.

---

## 💡 Key Implementation Notes

- **User-Agent spoofing** — mimics a real browser to avoid being blocked by the scraping target
- **Explicit waits** — more robust than `time.sleep()` for dynamic page loading
- **Error handling** — `try/except` per listing ensures one failure doesn't crash the whole run
- **`detach=True`** — Chrome stays open after the script ends for inspection

---

## 🧠 Skills Demonstrated

- Web scraping with `BeautifulSoup` + CSS selectors
- Browser automation with `Selenium` WebDriver
- DOM interaction: locating elements by XPath, filling inputs, clicking buttons
- Graceful error handling in automation pipelines
- Data extraction and cleaning (price parsing, address normalization)

---

## 📋 Requirements

```
requests
beautifulsoup4
selenium
```

> Python 3.7+ recommended. ChromeDriver must match your installed Chrome version.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Qusai Kagalwala**

[![GitHub](https://img.shields.io/badge/GitHub-qusai--Kagalwala-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/qusai-Kagalwala)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-qusai--kagalwala-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/qusai-kagalwala/)
[![DevVault](https://img.shields.io/badge/DevVault-Portfolio-FF6B35?style=for-the-badge&logo=github&logoColor=white)](https://github.com/qusai-Kagal/DevVault)
