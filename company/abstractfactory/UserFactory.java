package com.company.abstractfactory;
import com.company.abstractfactory.UserX;
public class UserFactory {
    public static UserX getUser(UserAbstractFactory factory){
        return factory.createUser();
    }
}
