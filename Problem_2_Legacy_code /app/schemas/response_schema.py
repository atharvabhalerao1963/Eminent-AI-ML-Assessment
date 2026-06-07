from pydantic import BaseModel


class FlaggedTransactionResponse(BaseModel):
    """
    Represents a flagged transaction
    returned by the API.
    """

    user_id: str
    amount: float
    status: str


class AnalyzeLogsResponse(BaseModel):
    """
    Response returned by
    POST /analyze-logs
    """

    total_flagged: int
    flagged_users: list[FlaggedTransactionResponse]