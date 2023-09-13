# Web Crawler

## Overview

The Web Crawler is a powerful cybersecurity tool that allows you to crawl the web, exploring links and sublinks, and displaying all the discovered links. This tool is designed to help cybersecurity professionals and web developers gain insight into the structure of websites and identify potential vulnerabilities.

## Features

- **Web Crawling:** The tool starts at a specified URL and recursively crawls through links and sublinks on web pages.

- **Link Display:** All discovered links are displayed in an organized and user-friendly format, making it easy to analyze and assess the website's structure.

- **Customizable Crawling:** You can customize the depth of the crawl and set other parameters to tailor the tool's behavior to your specific needs.

- **Export Results:** Save the crawled links to a file for further analysis or documentation.

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/sbmmahato/webcrawler.git
   ```

2. Change to the project directory:

   ```shell
   cd web-crawler
   ```

## Usage

### Basic Usage

To start a basic web crawl, use the following command:

```shell
python3 webcrawler.py https://example.com
```

Replace `https://example.com` with the URL you want to start crawling from. The tool will start the crawl and display the discovered links on the terminal.

The file with the list of the crawled websites then gets saved in web-crawler/recon/{folder named as the domain}/crawler_output.txt


## Credit

This project is made by Subham Mahato.

## Contributions

Contributions to this project are welcome. Feel free to open issues or submit pull requests to help improve this tool.

## Disclaimer

This tool is intended for educational and cybersecurity research purposes only. Ensure you have proper authorization before using it on any website or network you do not own or have permission to scan.

## Contact

For questions or inquiries, you can contact the project maintainer at sbmwork07@gmail.com.

Happy crawling! 🕷️🌐
