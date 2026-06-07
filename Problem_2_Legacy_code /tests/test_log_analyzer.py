from io import StringIO

from app.services.log_analyzer import LogAnalyzer


def test_parse_valid_line():
    analyzer = LogAnalyzer()

    result = analyzer.parse_line(
        "2026-06-01,user123,15000,ERROR"
    )

    assert result == (
        "user123",
        15000.0,
        "ERROR"
    )


def test_parse_invalid_amount():
    analyzer = LogAnalyzer()

    result = analyzer.parse_line(
        "2026-06-01,user123,ABC,ERROR"
    )

    assert result is None


def test_parse_malformed_line():
    analyzer = LogAnalyzer()

    result = analyzer.parse_line(
        "INVALID_LINE"
    )

    assert result is None


def test_analyze_flagged_transactions():
    analyzer = LogAnalyzer()

    sample_logs = StringIO(
        "\n".join([
            "2026-06-01,user123,15000,ERROR",
            "2026-06-01,user456,5000,ERROR",
            "2026-06-01,user789,25000,SUCCESS",
            "2026-06-01,user999,18000,ERROR",
        ])
    )

    results = list(
        analyzer.analyze(sample_logs)
    )

    assert len(results) == 2

    assert results[0].user_id == "user123"
    assert results[1].user_id == "user999"