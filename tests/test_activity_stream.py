from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import yaml

from biocypher_docs.activity_stream import (
    ACTIVITY_STREAM_MARKER,
    on_page_markdown,
    render_activity_stream,
    select_recent_events,
)


def event(
    event_date: str,
    title: str,
    summary: str,
    url: str,
) -> dict:
    return {
        "sub_title": event_date,
        "title": "Timeline category",
        "content": summary,
        "landing": {
            "title": title,
            "summary": summary,
            "url": url,
        },
    }


class ActivityStreamTests(unittest.TestCase):
    def test_selects_latest_non_future_events(self) -> None:
        events = [
            event("2026-07-19", "Future", "Not yet", "https://example.com/future"),
            event("2025-12-01", "Older", "Older event", "https://example.com/older"),
            event("2026-06-15", "Newest", "Newest event", "/community/workshop/"),
            event("2026-05-01", "Middle", "Middle event", "https://example.com/middle"),
        ]

        selected = select_recent_events(
            events,
            today=date(2026, 7, 18),
            limit=2,
        )

        self.assertEqual(
            [item["landing"]["title"] for item in selected],
            ["Newest", "Middle"],
        )

    def test_renders_year_groups_and_link_behavior(self) -> None:
        events = [
            event("2026-06-15", "Workshop", "Shared practices.", "/community/workshop/"),
            event("2025-12-01", "Hackathon", "Systems biology.", "https://example.com/repo"),
        ]

        rendered = render_activity_stream(events)

        self.assertIn(ACTIVITY_STREAM_MARKER, rendered)
        self.assertIn("<h3>2026</h3>", rendered)
        self.assertIn("<h3>2025</h3>", rendered)
        self.assertIn('datetime="2026-06-15"', rendered)
        self.assertIn('href="/community/workshop/"', rendered)
        self.assertIn('href="https://example.com/repo"', rendered)
        self.assertEqual(rendered.count('target="_blank"'), 1)
        self.assertLess(rendered.index("Workshop"), rendered.index("Hackathon"))

    def test_page_marker_is_replaced_from_yaml(self) -> None:
        events = [
            event("2020-06-15", "Timeline fixture", "From YAML.", "/fixture/"),
        ]

        with TemporaryDirectory() as directory:
            timeline_path = Path(directory) / "timeline.yaml"
            timeline_path.write_text(yaml.safe_dump(events), encoding="utf-8")
            with patch(
                "biocypher_docs.activity_stream.TIMELINE_PATH",
                timeline_path,
            ):
                rendered = on_page_markdown(
                    f"before\n{ACTIVITY_STREAM_MARKER}\nafter"
                )

        self.assertIn("Timeline fixture", rendered)
        self.assertIn("From YAML.", rendered)
        self.assertIn('href="/fixture/"', rendered)
        self.assertNotIn(
            f"{ACTIVITY_STREAM_MARKER}\nafter",
            rendered,
        )


if __name__ == "__main__":
    unittest.main()
