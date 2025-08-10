from sqlalchemy import Column,Integer,String,Text,Date
from .database import Base

class SurgicalCase(Base):
    __tablename__ = "surgical_cases"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String(10), index=True)
    diagnosis = Column(String(20))
    procedure = Column(String(25))
    pre_op_notes = Column(Text, nullable=True)
    intra_op_notes = Column(Text, nullable=True)
    post_op_notes = Column(Text, nullable=True)
    follow_ups_due = Column(Date, nullable=True)
    ai_summary = Column(Text, nullable = True)
    status = Column(String(20), default="pending")