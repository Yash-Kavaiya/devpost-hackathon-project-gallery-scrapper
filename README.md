
# Devpost Scraper

This is a Python script that uses Selenium to scrape data from a Devpost page. It extracts the name, description, and link of each project on the page and saves the data to a CSV file.

## Installation

1. Install ChromeDriver and add it to your system's PATH.
2. Install the required Python packages:

```
pip install selenium pandas
```

## Usage

To run the script for a single Devpost domain, run the `app.py` script and enter the domain when prompted:

```
python app.py
```

To run the script for multiple Devpost domains, create a text file with one domain per line (e.g. `devpost.txt`), and run the `run_app.sh` shell script:

```
./run_app.sh
```

The shell script will read the Devpost domains from the `devpost.txt` file and run the `app.py` script for each domain.

## Configuration

The script can be configured by modifying the following variables:

* `options`: Chrome options for the WebDriver.
* `extract_data()`: The function that extracts data from a single page.

## Dependencies

* ChromeDriver: A separate executable that Selenium WebDriver uses to control Chrome.
* Selenium: A Python library for controlling a web browser through the WebDriver API.
* pandas: A Python library for data manipulation and analysis.
