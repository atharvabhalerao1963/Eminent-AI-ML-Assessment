from fastapi import FastAPI
from backend.schemas import (
    QuestionRequest,
    QuestionResponse
)

from rag.chain import HRPolicyAssistant

app = FastAPI(
    title="Enterprise HR Policy Assistant"
)

assistant = HRPolicyAssistant()


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post(
    "/ask",
    response_model=QuestionResponse
)
def ask_question(
    request: QuestionRequest
):

    result = assistant.ask(
        request.question
    )

    return {
        "answer": result["answer"],
        "sources": result["sources"]
    }