package com.company;
import com.company.abstractfactory.*;
import com.company.adapter.*;
import com.company.interpreter.*;

public class Main {

    public static void main(String[] args) {
	// write your code here
        /*
        Student student = new Student();
        student.setName("stu1");
        student.setEmail("stu1@gmail.com");
        student.setStudentNumber("123123");
        System.out.println(student.getUserInfo());

        Lecturer lecturer = new Lecturer();
        lecturer.setName("lecturer");
        lecturer.setEmail("lecturer@gmail.com");
        lecturer.setDegree("Prof.dr.");
        System.out.println(lecturer.getUserInfo());
        */

        AbstractFactoryTester();
        AdapterTester();
        InterpreterTester();

    }

    private static void AbstractFactoryTester(){
        UserX student = UserFactory.getUser(new StudentFactory("msk","msk@gmail.com","12345645"));
        UserX lecturer = UserFactory.getUser(new LecturerFactory("lectu","lectu@gmail.com","Prof.dr"));

        System.out.println("");
        System.out.println("---ABSTRACT FACTORY TEST START---");
        System.out.println(lecturer.getUserInfo());
        System.out.println(student.getUserInfo());
        System.out.println("---ABSTRACT FACTORY TEST END---");
    }

    private static void AdapterTester(){
        Lecture lecture = new Lecture("LecturerNamexxx");

        lecture.setGrade("90");

        GradesAdapter adaptedLecture = new GradesAdapterImpl(lecture);

        System.out.println("");
        System.out.println("---ADAPTER TEST START---");
        System.out.println("Orijinal Not: "+lecture.getGrade());
        System.out.println("Adapte Edilerek Oluşturulan Harf Notu: "+adaptedLecture.getGrade());
        System.out.println("---ADAPTER TEST END---");
    }

    private static void InterpreterTester(){
        String lettergrade="50 Harf Notu Karşılığı";
        String scoregrade = "BB 4'lük Sistem Karşılığı";
        InterpreterClient ic = new InterpreterClient(new InterpreterContext());

        System.out.println("");
        System.out.println("---INTERPRETER TEST START---");
        System.out.println(lettergrade+" = "+ic.interpret(lettergrade));
        System.out.println(scoregrade+" = "+ic.interpret(scoregrade));
        System.out.println("---INTERPRETER TEST END---");
    }


}
