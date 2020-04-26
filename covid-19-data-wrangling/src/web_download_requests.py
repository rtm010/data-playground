import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def main():
    """Main script for downloading COVID-19 reports from WHO website using Requests"""
    n = 3  # number of reports to download, starting with latest
    who_reports_url = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/"
    link_text_starts_with = "Situation report"

    root_folder = Path(__file__).resolve().parent.parent
    data_folder = root_folder / "data"
    raw_data_folder = data_folder / "raw"

    for folder in [data_folder, raw_data_folder]:
        if not folder.exists():
            folder.mkdir()

    print(f"Sending GET request to {who_reports_url}")
    r = requests.get(who_reports_url)
    print("Request completed\n")

    if not r.status_code == 200:
        raise requests.HTTPError("HTTP status code is not 200 (OK)")

    soup = BeautifulSoup(r.text, "html.parser")

    print("Searching for links on the web page...")
    links = soup.find_all("a", limit=n, string=re.compile(f"^{link_text_starts_with}"))
    print(f"Found {len(links)} links (n = {n})\n")

    base_url = "https://www.who.int"
    for i, link in enumerate(links):
        download_link = base_url + link["href"]

        m = re.search(r"/([\w\d\-\.]+)\?", link["href"])
        if m:
            filename = m.group(1)
        else:
            filename = f"WHO_report_{i}.pdf"

        print(f"Downloading report from {download_link}")
        r = requests.get(download_link)
        print("Report downloaded\n")

        print(f"Saving file as {filename}\n")
        with open(raw_data_folder / filename, "wb") as fout:
            fout.write(r.content)

    return


if __name__ == "__main__":
    main()
