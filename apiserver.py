from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

DATABASE_URL = "sqlite:///./test.db"  # Change this for MySQL/PostgreSQL
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class Calculation(Base):
    __tablename__ = "calculations"
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String)
    num1 = Column(Integer)
    num2 = Column(Integer)
    result = Column(Integer)

Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    result = num1 + num2
    query = "INSERT INTO calculations (operation, num1, num2, result) VALUES ('add', :num1, :num2, :result)"
    await database.execute(query=query, values={"num1": num1, "num2": num2, "result": result})
    return {"result": result}

@app.get("/history")
async def get_history():
    query = "SELECT * FROM calculations"
    results = await database.fetch_all(query=query)
    return results
