package com.company.interpreter;

public class InterpreterContext{

    public String ScoreToLetter_Grade(int GradeInteger){
        String result = "HARF KARŞILIĞI BULUNAMADI!";
        if(GradeInteger <= 100 && GradeInteger >=0){
            if(GradeInteger>=90) result="AA";
            else if(GradeInteger>=80) result="BA";
            else if(GradeInteger>=70) result="BB";
            else if(GradeInteger>=60) result="CB";
            else if(GradeInteger>=50) result="CC";
            else result="FF";
        }
        return result;
    }

    public String LetterToGrade4_Grade(String GradeLetter) {
        String result="4'LÜK SİSTEMDE KARŞILIĞI BULUNAMADI";
        switch (GradeLetter) {
            case "AA":
                result = "4.0";
                break;
            case "BA":
                result = "3.5";
                break;
            case "BB":
                result = "3.0";
                break;
            case "CB":
                result = "2.5";
                break;
            case "CC":
                result = "2.0";
                break;
            case "FF":
                result = "0.0";
                break;
        }
        return result;
    }
}
