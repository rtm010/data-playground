from time import sleep
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    """Main script for downloading COVID-19 reports from WHO website using Selenium"""
    n = 3  # number of reports to download, starting with latest
    download_timer = 10  # set seconds to wait for download to finish (per file)
    who_reports_url = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/"
    link_text_starts_with = "Situation report"

    root_folder = Path(__file__).resolve().parent.parent
    data_folder = root_folder / "data"
    raw_data_folder = data_folder / "raw"

    for folder in [data_folder, raw_data_folder]:
        if not folder.exists():
            folder.mkdir()

    browser = open_chrome(str(raw_data_folder))
    browser.get(who_reports_url)

    links = browser.find_elements_by_partial_link_text(link_text_starts_with)

    for i, link in enumerate(links):
        link.click()
        sleep(download_timer)

        if i + 1 >= n:
            break

    browser.close()

    print("\nFinished downloading files")
    print(f"Files are saved in {raw_data_folder}\n")
    return


def open_chrome(default_download_folder):
    """Start Chrome with required configuration for downloading PDFs"""
    options = Options()

    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": default_download_folder,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "plugins.always_open_pdf_externally": True,
        },
    )

    return webdriver.Chrome(options=options)


if __name__ == "__main__":
    main()
