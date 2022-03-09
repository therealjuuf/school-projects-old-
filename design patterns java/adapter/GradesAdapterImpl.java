package com.company.adapter;



public class GradesAdapterImpl implements GradesAdapter{
    private Grades gradex;

    public GradesAdapterImpl(Grades lecture) {
       // this.gradex=lecture.getGrade();
        this.gradex=lecture;
    }

    @Override
    public String getGrade(){
        return convertGradeToLetter(gradex.getGrade());
    }

    private String convertGradeToLetter(String grade){
        String result;
        int gradeint = Integer.parseInt(grade);
        if(gradeint>=90) result="AA";
        else if(gradeint>=80) result="BA";
        else if(gradeint>=70) result="BB";
        else if(gradeint>=60) result="CB";
        else if(gradeint>=50) result="CC";
        else result="FF";
        return result;
    }
}
