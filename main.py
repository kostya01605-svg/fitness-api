from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

engine = create_engine("sqlite:///./fitness.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Workout(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    trainer = Column(String)
    time = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/workouts")
def get_workouts(db: Session = Depends(get_db)):
    return db.query(Workout).all()

@app.post("/workouts")
def add_workout(name: str, trainer: str, time: str, db: Session = Depends(get_db)):
    workout = Workout(name=name, trainer=trainer, time=time)
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return {"message": "Тренировка добавлена!", "workout": workout}