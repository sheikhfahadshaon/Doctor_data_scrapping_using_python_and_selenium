# Doctor Data Scraper

This Python script scrapes doctor information from the [Doctor Bangladesh](https://www.doctorbangladesh.com) website based on department and location preferences.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Requirements](#requirements)
- [Contributing](#contributing)

## Features
- Scrapes doctor workplace and name based on the provided specialization and location.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/doctor-data-scraper.git
    ```
2. Install the required libraries if you haven't already
    ```bash
    pip install pandas selenium chromedriver-autoinstaller
    ```
3. Run the script:
    ```bash
        python main.py
    ```
4. Follow the on-screen prompts to specify the department and location for the doctor data you want to scrape.

5. The scraped doctor data will be saved in an Excel file named {department}_{location}_doctor_data.xlsx in the same directory.

## Requirements
* Python 3.x
* pandas
* selenium
* chromedriver-autoinstaller

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
