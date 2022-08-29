package cookieos_security_auth;

import java.util.*;

public class Authenticator {
    public boolean authenticate() {
        Scanner scanner = new Scanner();

        boolean r = false;
        for(int i = 0; i < 6; i++) {
            System.out.print("\nEnter password: ");
            String password1 = sc.nextLine;

            if(password1.equals(password0)) {
                System.out.print("\nAuthorization succesfull.");
                boolean r = true;
            } else {
                System.out.print("\nIncorrect password.")
            }
        }

        return r;
    }
}