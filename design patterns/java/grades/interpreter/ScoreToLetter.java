package com.company.interpreter;

public class ScoreToLetter implements Expression{
    private int grade;

    public ScoreToLetter(int grade) {
        this.grade = grade;
    }

    @Override
    public String interpret(InterpreterContext ic){
        return ic.ScoreToLetter_Grade(grade);
    }
}
