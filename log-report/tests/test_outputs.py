import json
from pathlib import Path

import pytest

REPORT_PATH = Path("/app/report.json")

# Expected values are derived from environment/access.log (6 request lines,
# 3 distinct client IPs, /index.html requested 3 times).
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


@pytest.fixture(scope="module")
def report() -> dict:
    assert REPORT_PATH.exists(), "no /app/report.json found"
    with REPORT_PATH.open() as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json must contain a JSON object"
    return data


def test_report_is_valid_json_object(report: dict):
    """The report exists and is a JSON object."""
    assert report is not None


def test_total_requests(report: dict):
    """total_requests matches the number of request lines in the log."""
    assert report.get("total_requests") == EXPECTED_TOTAL_REQUESTS, (
        f"total_requests should be {EXPECTED_TOTAL_REQUESTS}, "
        f"got {report.get('total_requests')!r}"
    )


def test_unique_ips(report: dict):
    """unique_ips matches the number of distinct client IPs in the log."""
    assert report.get("unique_ips") == EXPECTED_UNIQUE_IPS, (
        f"unique_ips should be {EXPECTED_UNIQUE_IPS}, "
        f"got {report.get('unique_ips')!r}"
    )


def test_top_path(report: dict):
    """top_path is the most-requested path in the log."""
    assert report.get("top_path") == EXPECTED_TOP_PATH, (
        f"top_path should be {EXPECTED_TOP_PATH!r}, got {report.get('top_path')!r}"
    )
