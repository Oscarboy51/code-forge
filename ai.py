from fastapi import APIRouter
from pydantic import BaseModel
from .. import nlp

router = APIRouter()

class CaseData(BaseModel):
    diagnosis: str
    procedure: str
    complications: str = None

@router.post("/api/ai/summarize")
async def summarize_notes(case: CaseData):


    # Calling NLP function:
    summary = nlp.generate_case_summary(
        diagnosis=case.diagnosis,
        procedure=case.procedure,
        complications=case.complications
    )
    return {"summary": summary}

    import logging

    loging.error(f"Error generating summary: {e}")

    raise HTTPException(status_code=500, detail=f"Error generating summary: {e}")
