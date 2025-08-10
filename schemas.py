from pydantic import BaseModel
from datetime import date
from typing import Optional


class SurgicalCaseBase(BaseModel):
    patient_id: str
    diagnosis: str
    procedure: str
    pre_op_notes: Optional[str] = None
    intra_op_notes: Optional[str] = None
    post_op_notes: Optional[str] = None
    follow_ups_due: Optional[str] = None

class SurgicalCaseCreate(SurgicalCaseBase):
    pass

class SurgicalCase(SurgicalCaseBase):
    id:int
    ai_summary: Optional[str] = None
    status:str


model_config = {
    "from_attributes": True
}