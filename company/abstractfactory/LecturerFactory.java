package com.company.abstractfactory;
import com.company.abstractfactory.Lecturer;
import com.company.abstractfactory.UserAbstractFactory;

public class LecturerFactory implements UserAbstractFactory{
    private String name;
    private String email;
    private String Degree;

    public LecturerFactory(String name, String email, String Degree){
        this.name=name;
        this.email=email;
        this.Degree=Degree;
    }

    @Override
    public UserX createUser(){
        return new Lecturer(name,email,Degree);
    }
}
