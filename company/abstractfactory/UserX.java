package com.company.abstractfactory;

public abstract class UserX {
    String name;
    String email;
    public abstract String getUserInfo();
    public void setName(String UserName){
        this.name=UserName;
    }
    public void setEmail(String UserEmail){
        this.email=UserEmail;
    }
    public String getName(){
        return this.name;
    }
    public  String getEmail(){
        return this.email;
    }


}


