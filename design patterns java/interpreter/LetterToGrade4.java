package com.company.interpreter;

import com.company.interpreter.Expression;

public class LetterToGrade4 implements Expression{
    private String grade;

    public LetterToGrade4(String grade) {
        this.grade = grade;
    }

    @Override
    public String interpret(InterpreterContext ic){
        return ic.LetterToGrade4_Grade(grade);
    }
}
