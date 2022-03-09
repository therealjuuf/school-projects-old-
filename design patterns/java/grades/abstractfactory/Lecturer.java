package com.company.abstractfactory;

public class Lecturer extends UserX {
    String Degree;

    public Lecturer(String name, String email, String Degree){
        this.name=name;
        this.email=email;
        this.Degree=Degree;
    }

    @Override
    public String getUserInfo() {
        return getDegree()+" "+getName()+", contact:"+ getEmail();
    }

    public void setDegree(String Degree) {
        this.Degree=Degree;
    }

    public String getDegree() {
        return this.Degree;
    }


}






