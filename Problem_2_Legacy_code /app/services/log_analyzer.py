from typing import Generator, Optional, TextIO

from app.core.logger import get_logger
from app.models.transaction import Transaction


class LogAnalyzer:
    """
    Service responsible for analyzing
    large transaction log files.
    """

    def __init__(self) -> None:
        self.logger = get_logger(__name__)

    def parse_line(
        self,
        line: str
    ) -> Optional[tuple[str, float, str]]:
        """
        Parse a single log line.

        Returns:
            tuple(user_id, amount, status)
            OR
            None if the line is malformed.
        """

        line = line.strip()

        if not line:
            self.logger.warning(
                "Empty line encountered. Skipping."
            )
            return None

        parts = line.split(",")

        if len(parts) != 4:
            self.logger.warning(
                f"Malformed log line skipped: {line}"
            )
            return None

        try:
            _, user_id, amount, status = parts

            return (
                user_id,
                float(amount),
                status
            )

        except ValueError:
            self.logger.warning(
                f"Invalid amount value in line: {line}"
            )
            return None

    def analyze(
        self,
        file_obj: TextIO
    ) -> Generator[Transaction, None, None]:
        """
        Analyze log records and yield flagged transactions.

        Time Complexity:
            O(n)
            where n is the number of lines.

        Space Complexity:
            O(1)
            Generator-based processing ensures
            only one line is processed at a time.

        Legacy Code:
            Time  : O(n)
            Space : O(n)

        Refactored Version:
            Time  : O(n)
            Space : O(1)
        """

        self.logger.info(
            "Started log analysis."
        )

        for line in file_obj:

            # FastAPI UploadFile provides bytes.
            # Convert bytes to string before parsing.
            if isinstance(line, bytes):
                line = line.decode("utf-8")

            parsed_data = self.parse_line(line)

            if parsed_data is None:
                continue

            user_id, amount, status = parsed_data

            if status == "ERROR" and amount > 10000:

                self.logger.info(
                    f"Flagged transaction detected for user {user_id}"
                )

                yield Transaction(
                    user_id=user_id,
                    amount=amount,
                    status="flagged"
                )

        self.logger.info(
            "Completed log analysis."
        )