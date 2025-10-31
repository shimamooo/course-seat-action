from bs4 import BeautifulSoup
import json
import sys
from courses.base_course import BaseCourse


class COMPSCI185(BaseCourse):
    def __init__(self):
        super().__init__(
            "https://classes.berkeley.edu/content/2026-spring-compsci-185-001-lec-001"
        )

    def parse_html(self, html):
        soup = BeautifulSoup(html, "html.parser")
        stats_div = soup.select_one("div.stats")
        if not stats_div:
            print("No stats div found")
            sys.exit(1)

        stats = {}
        for child in stats_div.find_all("div", recursive=False):
            label_tag = child.find("strong")
            if not label_tag:
                continue

            label = label_tag.get_text(strip=True).rstrip(":").lower()
            text_after = label_tag.next_sibling
            if text_after:
                try:
                    value = int(text_after.strip())
                    stats[label] = value
                except ValueError:
                    continue
        return self.extract_data(stats)

    def extract_data(self, data_json):
        try:
            enrolled = stats["enrolled"]
            waitlisted = stats["waitlisted"]
            capacity = stats["capacity"]
            waitlist_max = stats["waitlist_max"]

            available = waitlisted_max - waitlisted > 0
            message = (
                f"Enrolled: {enrolled}/{capacity}, "
                f"Waitlisted: {waitlisted}/{waitlist_max}."
            )

            return available, message

        except KeyError:
            print("Missing required data")
            sys.exit(1)
