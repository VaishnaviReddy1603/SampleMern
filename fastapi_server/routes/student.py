from fastapi import APIRouter
from database import student_collection
from model import Student_model
student_router=APIRouter(prefix="/student",tags=["student"])
#localhost:8000/student/addStudent
@student_router.post("/addStudent")
def addStudent(stu:Student_model):
    result=student_collection.insert_one(stu.model_dump())
    #model_dump used to convert class fields into dict
    return "student insertion success"
#localhost:8000/student/getStudent
@student_router.get("/getStudent")
def getStudent():
    return "getstudent method called"
#localhost:8000/student/updateStudent
@student_router.put("/updateStudent")
def updateStudent():
    return "update student method called"
#localhost:8000/student/deleteStudent
@student_router.delete("/deleteStudent")
def deleteStudent():
    return "delete student method called"
  