from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import nlp, crud, schemas, database, models


router = APIRouter()

# Dependency to get database session

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
         db.close()

@router.post("/cases/", response_model=schemas.SurgicalCase)
def create_case(case: schemas.SurgicalCaseCreate, db: Session = Depends(get_db)):
    return crud.create_surgical_case(db, case)


@router.get("/cases/{case_id})", response_model=schemas.SurgicalCase)
def read_case(case_id: int, db: Session = Depends(get_db)):
    db_case = crud.get_surgical_case(db, case_id)
    if db_case is None:
        raise HTTPException(status_code=404, detail="Case not found")
        return db_case

@router.post("/cases/{case_id}/generate-summary",response_model=schemas.SurgicalCase)
def generate_case_summary(case_id: int, db: Session = Depends(get_db)):
    db_case = crud.get_surgical_case(db, case_id)
    if db_case is None:
        raise HTTPException(status_code=404, detail="Case not found")

    # Using summary structure

    summary_text = nlp.generate_case_summary(
        diagnosis=db_case.diagnosis,
        procedure=db_case.procedure,
        complication=db_case.coplication,
    )

    update_case = crud.update_surgical_case_summary(db, case_id, summary_text)
    return update_case
