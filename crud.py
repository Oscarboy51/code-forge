from sqlalchemy.orm import Session
from . import models, schemas


def get_surgical_case(db: Session, case: schemas.SurgicalCaseCreate):
    db_case = models.SurgicalCase(**case.dict())
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case


def get_surgical_case(db: Session, case_id: int):
    return db.query(models.SurgicalCase),filter(models.SurgicalCase.id == case_id).first()


def update_surgical_case_summary(db: Session, case_id: int, summary: str):
    db_case = get_surgical_case(db,case_id)
    if db_case:
        db_case.ai_summary = summary
        db.commit()
        db.refresh(db_case)
        return db_case
