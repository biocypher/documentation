"""Build the landing-page activity stream from the ecosystem timeline."""

from collections.abc import Iterable, Mapping
from datetime import date
from html import escape
from pathlib import Path
import re
from typing import Any

import yaml


ACTIVITY_STREAM_MARKER = "<!-- recent-work-from-timeline -->"
TIMELINE_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "assets"
    / "timeline"
    / "biocypher_timeline.yaml"
)
RECENT_EVENT_LIMIT = 8

_MARKDOWN_LINK = re.compile(r"\[([^]]+)]\(([^)]+)\)")


def _parse_event_date(event: Mapping[str, Any]) -> date:
    value = event["sub_title"]
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value))


def _plain_summary(content: str) -> str:
    lines = [
        line.strip()
        for line in content.splitlines()
        if line.strip() and not line.lstrip().startswith("[:octicons-")
    ]
    text = " ".join(lines)
    return _MARKDOWN_LINK.sub(r"\1", text)


def _first_content_link(content: str) -> str:
    match = _MARKDOWN_LINK.search(content)
    return match.group(2) if match else ""


def _landing_fields(event: Mapping[str, Any]) -> tuple[str, str, str]:
    landing = event.get("landing") or {}
    content = str(event.get("content") or "")
    title = str(landing.get("title") or event.get("title") or "Recent work")
    summary = str(landing.get("summary") or _plain_summary(content))
    url = str(landing.get("url") or _first_content_link(content))
    return title, summary, url


def select_recent_events(
    events: Iterable[Mapping[str, Any]],
    *,
    today: date | None = None,
    limit: int = RECENT_EVENT_LIMIT,
) -> list[Mapping[str, Any]]:
    """Return the latest dated events that have already happened."""

    cutoff = today or date.today()
    past_events = [event for event in events if _parse_event_date(event) <= cutoff]
    return sorted(past_events, key=_parse_event_date, reverse=True)[:limit]


def render_activity_stream(events: Iterable[Mapping[str, Any]]) -> str:
    """Render recent timeline entries in the landing-page activity layout."""

    parts = [
        ACTIVITY_STREAM_MARKER,
        '<div class="tx-activity-stream" aria-label="BioCypher ecosystem activity timeline">',
    ]
    active_year: int | None = None

    for event in events:
        event_date = _parse_event_date(event)
        if event_date.year != active_year:
            if active_year is not None:
                parts.append("</div>")
            active_year = event_date.year
            parts.extend(
                [
                    '<div class="tx-activity-group">',
                    f"<h3>{active_year}</h3>",
                ]
            )

        title, summary, url = _landing_fields(event)
        safe_title = escape(title)
        safe_summary = escape(summary)
        safe_date = escape(event_date.isoformat(), quote=True)
        display_date = event_date.strftime("%b %Y")

        if url:
            safe_url = escape(url, quote=True)
            external = url.startswith(("http://", "https://"))
            target = ' target="_blank" rel="noopener noreferrer"' if external else ""
            parts.append(f'<a class="tx-activity-row" href="{safe_url}"{target}>')
            closing_tag = "</a>"
        else:
            parts.append('<div class="tx-activity-row">')
            closing_tag = "</div>"

        parts.extend(
            [
                f'<time datetime="{safe_date}">{display_date}</time>',
                "<span>",
                f"<strong>{safe_title}</strong>",
                safe_summary,
                "</span>",
                closing_tag,
            ]
        )

    if active_year is not None:
        parts.append("</div>")
    parts.append("</div>")
    return "\n".join(parts)


def on_page_markdown(markdown: str, **_: Any) -> str:
    """Replace the landing-page marker during every MkDocs build."""

    if ACTIVITY_STREAM_MARKER not in markdown:
        return markdown

    events = yaml.safe_load(TIMELINE_PATH.read_text(encoding="utf-8")) or []
    recent_events = select_recent_events(events)
    return markdown.replace(
        ACTIVITY_STREAM_MARKER,
        render_activity_stream(recent_events),
        1,
    )
