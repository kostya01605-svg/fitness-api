from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Workout(BaseModel):
    name: str
    trainer: str
    time: str

workouts = []

@app.get("/")
def read_root():
    return {"message": "Система записи на тренировки"}

@app.get("/workouts")
def get_workouts():
    return workouts

@app.post("/workouts")
def add_workout(workout: Workout):
    workouts.append(workout)
    return {"message": "Тренировка добавлена!", "workout": workout}