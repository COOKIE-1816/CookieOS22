package cookieos_security_changepassword_gui;

import java.awt.*;
import java.awt.event.*;
import java.awt.swing.*;
import java.awt.swing.border.*;

public class Dialog extends JDialog {
    private JPasswordField pfCurrentPassword;
    private JPasswordField pfNewPassword;
    private JPasswordField pfReEnterPassword;

    private JLabel lbCurrentPassword;
    private JLabel lbNewPassword;
    private JLabel lbReEnterPassword;

    private boolean succeded;

    public Dialog(Frame parent) {
        super(parent, "Change password", true);

        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstrains cs = new GridBagConstrains();

        cs.fill = GridBagConstrains.HORIZONTAL;


        lbCurrentPassword = new JLabel("Current password: ");
        cs.gridx = 0;
        cs.gridy = 0;
        cs.gridwidth = 1;
        panel.add(lbCurrentPassword, cs)

        pfCurrentPassword = new JPasswordField(20);
        cs.gridx = 1;
        cs.gridy = 0;
        cs.gridwidth = 1;
        panel.add(pfCurrentPassword, cs);
        panel.setBorder(new LineBorder(Color.GRAY));


        lbNewPassword = new JLabel("New password: ");
        cs.gridx = 0;
        cs.gridy = 1;
        cs.gridwidth = 1;
        panel.add(lbNewPassword, cs);

        pfNewPassword = new JPasswordField(20);
        cs.gridx = 1;
        cs.gridy = 1;
        cs.gridwidth = 1;
        panel.add(pfNewPassword, cs);
        panel.setBorder(new LineBorder(Color.GRAY));
    }
}