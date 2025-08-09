# Indian-Startup-Funding-Analysis
Here’s a professional **README.md** for your `Main.py` script:

---

# Startup Funding Analysis

This project analyzes Indian startup funding data from `startup_funding.csv` to uncover trends, top sectors, and leading investors. It uses **Pandas**, **Matplotlib**, and **Seaborn** for data cleaning, processing, and visualization.

---

## 📂 Project Structure

```
Main.py                # Main script for data analysis & visualization
startup_funding.csv    # Dataset containing startup funding details
```

---

## 📋 Features

* **Data Loading & Cleaning**

  * Reads the dataset using Pandas.
  * Renames columns for consistency.
  * Converts date fields to `datetime` format.
  * Removes missing or invalid entries.
  * Cleans numeric columns by removing currency symbols.

* **Trend Analysis**

  * Plots monthly funding trends.
  * Shows total funding amount over time.

* **Sector Analysis**

  * Identifies top industries by number of startups funded.
  * Displays results with a bar chart.

* **Investor Analysis**

  * Lists the top 20 investors by number of deals.
  * Visualizes with a horizontal bar chart.

---

## 📊 Visualizations

1. **Funding Trend Over Time (Monthly)**
   Shows how startup funding has evolved month by month.

2. **Top Sectors by Number of Fundings**
   Displays the top industries receiving startup investments.

3. **Top 20 Investors by Number of Investments**
   Highlights the most active investors.

---

## 🛠 Requirements

Install the following Python libraries before running the script:

```bash
pip install pandas matplotlib seaborn
```

---

## ▶️ How to Run

1. Place `Main.py` and `startup_funding.csv` in the same directory.
2. Open a terminal or command prompt in that directory.
3. Run:

```bash
python Main.py
```

---

## 📌 Notes

* The dataset path in the script is currently set to `/content/startup_funding.csv` (Google Colab style).
  Change it to your local path if running on your system:

  ```python
  df = pd.read_csv('startup_funding.csv')
  ```
* Missing or incorrectly named columns will be reported in the console.

---

## 📄 License

This project is open-source and available for educational and analytical purposes.

-
