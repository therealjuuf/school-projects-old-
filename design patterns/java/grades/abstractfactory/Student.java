package com.company.abstractfactory;

public class Student extends UserX {

    String StudentNumber;

    public Student(String name, String email, String StudentNumber){
        this.name=name;
        this.email=email;
        this.StudentNumber=StudentNumber;
    }


    @Override
    public String getUserInfo() {
        return "Student "+getName()+", student number: "+getStudentNumber()+", contact:"+ getEmail();
    }
    public void setStudentNumber(String StudentNumber) {
        this.StudentNumber=StudentNumber;
    }

    public String getStudentNumber() {
        return this.StudentNumber;
    }
}