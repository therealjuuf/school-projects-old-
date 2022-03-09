package com.company.abstractfactory;
import com.company.abstractfactory.Student;
import com.company.abstractfactory.UserAbstractFactory;

public class StudentFactory implements UserAbstractFactory{
    private String name;
    private String email;
    private String StudentNumber;

    public StudentFactory(String name, String email, String StudentNumber){
        this.name=name;
        this.email=email;
        this.StudentNumber=StudentNumber;
    }

    @Override
    public UserX createUser(){
        return new Student(name,email,StudentNumber);
    }
}
