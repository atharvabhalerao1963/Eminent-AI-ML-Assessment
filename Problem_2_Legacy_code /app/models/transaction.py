from dataclasses import dataclass


@dataclass
class Transaction:
    """
    Represents a flagged transaction extracted
    from the log file.
    """

    user_id: str
    amount: float
    status: str