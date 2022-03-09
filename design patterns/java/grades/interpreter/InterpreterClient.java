package com.company.interpreter;

public class InterpreterClient {
    public InterpreterContext ic;

    public InterpreterClient(InterpreterContext i){
        this.ic=i;
    }

    public String interpret(String str){
        Expression exp = null;
        //create rules for expressions
        if(str.contains("Harf Notu Karşılığı")){
            exp=new ScoreToLetter(Integer.parseInt(str.substring(0,str.indexOf(" "))));
        }else if(str.contains("4'lük Sistem Karşılığı")){
            exp=new LetterToGrade4((str.substring(0,str.indexOf(" "))));
        }else return str;

        return exp.interpret(ic);
    }
}
