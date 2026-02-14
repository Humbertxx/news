# Financial News Scraper

A Python-based web scraper built with [Scrapy](https://scrapy.org/) to harvest financial news headlines, metadata, and article content from Yahoo Finance.

## Description

This project contains a spider named `FinNews` that:
1.  Navigates to Yahoo Finance news pages (currently configured for specific stock tickers).
2.  Extracts headlines, publication dates, and related tickers.
3.  Follows links to the full articles.
4.  Scrapes the main text content of the article.
5.  Outputs the data in a structured format CSV.

## Prerequisites

* **Python 3.x**
* **Scrapy** framework

## Installation

1.  **Clone the repository** (if applicable) or navigate to your project folder:
    ```bash
    cd sentiment
    ```

2.  **Install the required dependencies**:
    ```bash
    pip install scrapy
    ```

## Usage

To run the spider and save the output to a file, use the `scrapy crawl FinNews` command in your terminal.

### Run and save to CSV
``` data.csv ```
