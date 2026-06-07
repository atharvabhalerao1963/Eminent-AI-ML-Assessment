from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.response_schema import (
    AnalyzeLogsResponse,
    FlaggedTransactionResponse
)
from app.services.log_analyzer import LogAnalyzer


router = APIRouter()

analyzer = LogAnalyzer()


@router.post(
    "/analyze-logs",
    response_model=AnalyzeLogsResponse
)
async def analyze_logs(
    file: UploadFile = File(...)
) -> AnalyzeLogsResponse:
    """
    Analyze uploaded log file and return
    flagged transactions.
    """

    try:

        flagged_users = []

        flagged_transactions = analyzer.analyze(
            file.file
        )

        for transaction in flagged_transactions:

            flagged_users.append(
                FlaggedTransactionResponse(
                    user_id=transaction.user_id,
                    amount=transaction.amount,
                    status=transaction.status
                )
            )

        return AnalyzeLogsResponse(
            total_flagged=len(flagged_users),
            flagged_users=flagged_users
        )

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=f"Failed to analyze log file: {str(exc)}"
        )