package cookieos_security_gui_auth;

import java.awt.*;
import java.awt.event.*;
import java.awt.swing.*;
import java.awt.swing.border.*;

public class LoginDialog extends JDialog {
    private JPasswordField pfPassword;

    private JLabel lbPassword;

    private JButton btnLogin;
    private JButton btnCancel;

    private boolean suceeded;

    public LoginDialog(Frame parent) {
        super(parent, "Login", true);

        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstrains cs = new GridBagConstrains();

        cs.fill = GridBagConstrains.HORIZONTAL;

        lbPassword = new JLabel("Password: ");
        cs.gridx = 0;
        cs.gridy = 0;
        cs.gridwidth = 1;
        panel.add(lbPassword, cs);

        pfPassword = new JPasswordField(20);
        cs.gridx = 1;
        cs.gridy = 0;
        cs.gridwidth = 1;
        panel.add(pfPassword, cs);
        panel.setBorder(new LineBorder(Color.GRAY));

        btnLogin = new JButton("Login");
        btnLogin.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if(Login.authenticateable) {
                    if(Login.authenticate(getPassword())) {
                        suceeded = true;

                        dispose();
                    } else {
                        JOptionPane.showMessageDialog(
                            LoginDialog.this,

                            "Invaild password.",
                            "Login",

                            JOptionPane.ERROR_MESSAGE
                        );

                        succeded = false;
                        dispose();
                    }
                } else {
                    succeded = true;
                    Login.proceed();
                }

                pfPassword.setText("");
            };
        });

        btnCancel = new JButton("Cancel");
        btnCancel.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                succeded = false;
                dispose();
            }
        });

        JPanel bp = new JPanel();

        bp.add(btnLogin);
        bp.add(btnCancel);

        getContentPane().add(panel, BorderLayout.CENTER);
        getContentPane().add(bp, BorderLayout.PAGE_END);

        pack();

        setResizeable(false);
        setLocationRelativeTo(parent);
    }

    public String getPassword() {
        Login.Credentials = new String(pfPassword.getPassword());
        return Login.Credentials.password;
    }

    public boolean isSucceeded() {
        return succeded;
    }
}

public class Login {
    public class Credentials {
        String password = "";
    };

    public static boolean authenticate(String password) {
        if(password.equals(Login.Credentials.password)) {
            return true;
        }

        return false;
    }
}