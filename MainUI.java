package hackprinceton;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

/**
 * Main class that loads the JFrame for the UI.
 * @author Alok Tripathy
 * @since  November 8, 2013
 * @version 1.0.0
 *
 */
public class MainUI {

	public MainUI() {
		
		JFrame frame = new JFrame("Swarm");
	
		frame.setSize(400, 400);
		frame.setVisible(true);
		
		frame.addWindowListener(
				new WindowAdapter() {
					@Override
					public void windowClosing(WindowEvent e) {
						System.exit(0);
					}
				});
	}
	
	public static void main(String[] args) {
		new MainUI();
	}
}
