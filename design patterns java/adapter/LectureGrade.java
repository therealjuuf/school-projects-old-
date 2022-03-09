package com.company.adapter;

public class LectureGrade implements Grades{
    public String grade;
    @Override
    public String getGrade(){
        return grade;
    }

    @Override
    public void setGrade(String grade){
        this.grade=grade;
    }
}
