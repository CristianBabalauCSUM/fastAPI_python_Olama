from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from model import generate_prompt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Schedule(BaseModel):
    title: str
    description: str
    location: str
    start: str
    end: str
    duration: int
    time: str
    type: list[str]

class UserScheduleRequest(BaseModel):
    today: list[Schedule]
    otherSchedule: list[Schedule]


@app.post("/schedule")
async def prompt(userSchedule: UserScheduleRequest):
    print("userSchedule")
    newSchedule = generate_prompt(userSchedule.today, userSchedule.otherSchedule)
    print("newSchedule")
    return {"suggestions": newSchedule}

@app.get('/')
async def root():
    return {"message": "Hello World"}


