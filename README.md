# CBdatascraper
CB data scraper is meant to be a scraping script for retrieving official exchange rates from Central Banks' websites.
This maybe come for use for those companies which have to keep track in case of international invoicing.

## Installation
CBdatascraper is meant to be used with Selenium and Firefox. Installation instructions are the following.

### Reqirements
sudo pip3 install beautifulsoup4 selenium
apt-get install xvfb #as per http://www.alittlemadness.com/2008/03/05/running-selenium-headless/
-- driver --
https://github.com/mozilla/geckodriver/releases
$export PATH=$PATH:/path/to/drier

### Additional Commands
Xvfb :10 -ac & # as per this https://medium.com/@griggheo/running-selenium-webdriver-tests-using-firefox-headless-mode-on-ubuntu-d32500bb6af2

