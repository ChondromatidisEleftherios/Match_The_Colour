import random as rdm 
import utils as u
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkf

prev_distance = 100.00 # Global μεταβλητη για αρχικοποιηση της απόστασης
attempt = 1 # Μετρητής προσπαθειών
rst = False
auto_va = True # Χρησιμοποιείται για το πρώτο generation το οποίο είναι αυτόματο

def cursorb1(a): # Συνάρτηση για το πρώτο κουμπί, όταν ο κέρσορας είναι πάνω του
   button1.config(background='white', foreground= "darkorchid4")

def no_cursorb1(a): # Συνάρτηση για το πρώτο κουμπί, όταν ο κέρσορας δεν είναι πάνω του
   button1.config(background= 'cyan', foreground= 'darkorchid4')

def cursorb2(a): # Συνάρτηση για το δεύτερο κουμπί, όταν ο κέρσορας είναι πάνω του
   button2.config(background='white', foreground= "darkorchid4")

def no_cursorb2(a): # Συνάρτηση για το δεύτερο κουμπί, όταν ο κέρσορας δεν είναι πάνω του
   button2.config(background= 'cyan', foreground= 'darkorchid4')

def reset_sliders(): # Συνάρτηση για να πάνε όλα τα sliders στο 0
	red.set(0)
	green.set(0)
	blue.set(0)

def upd(c):
	global rst 
	if rst == False:
		col_code = '#%02x%02x%02x' % (red.get(), green.get(), blue.get()) # Μετατρέπει τη τιμή των 3 sliders σε 16δικό αριθμό για το colourcode
		pl_frame.config(bg= col_code)
		pl_col = tk.Label(t_frame, height=1, width=15, fg='white', bg= 'black', text = str(red.get()) + "    " + str(green.get()) + "    " + str(blue.get())) # Εμφάνιση των χρωματων του χρηστη
		pl_col.grid(row = 0, column = 0, sticky = tk.NSEW)
	elif rst == True:
		pl_frame.config(bg= "black")
		pl_col = tk.Label(t_frame, height=1, width=15, fg='white', bg= 'darkorchid4', text = " ")
		pl_col.grid(row = 0, column = 0, sticky = tk.NSEW)

def random_col(): # Συνάρτηση που κάνει generate ένα τυχαίο χρώμα
	global prev_distance
	global rst
	global attempt
	global r # Global ωστε να μπορω να υπολογισω το colour distance
	global g 
	global b 
	attempt = 1
	prev_distance = 100.00
	score = tk.Label(t2_frame, height=1, width= 30, bg='darkorchid4', text= " ")
	score.grid(row=0, column=2, sticky = tk.NSEW)
	r = rdm.randint(1,254) 
	g= rdm.randint(1,254)
	b= rdm.randint(1,254)
	ai_code = '#%02x%02x%02x' % (r, g, b) # Mετατροπή των χρωμάτων σε 16δικο αριθμό
	ai_frame.config (bg= ai_code)
	reset_sliders()
	if rst == False:
		att = tk.Label(at_frame, height=1, width= 10, fg='red', bg='darkorchid4', text= "Attempt " + str(attempt), font= ('Cambria', 24, 'bold'))
		att.grid(row=0, column=2, sticky = tk.NSEW)
	if rst==True: # Σε περίπτωση που η παρτίδα έχει τελειώσει (αποφυγή bug)
		att = tk.Label(at_frame, height=1, width= 10, fg='red', bg='darkorchid4', text= "Attempt " + str(attempt), font= ('Cambria', 24, 'bold'))
		att.grid(row=0, column=2, sticky = tk.NSEW)
		pl_frame.config(bg= "black")
		pl_col = tk.Label(t_frame, height=1, width=15, fg='white', bg= 'darkorchid4', text = " ")
		pl_col.grid(row = 0, column = 0, sticky = tk.NSEW)
		prev_distance = 100.00
		score = tk.Label(t2_frame, height=1, width= 10, bg='darkorchid4', text= " ")
		score.grid(row=0, column=2, sticky = tk.NSEW)
		rst = False


def di(): # Συνάρτηση για υπολογισμό απόστασης, εμφάνισης καλύτερου σκορ παρτίδας και αποτελέσματος παρτίδας
	global attempt 
	global prev_distance
	global rst
	attempt= attempt + 1
	distance = u.diff(red.get(), green.get(), blue.get(), r,g,b) # Yπολογισμός colour distance
	if rst == False:
		if distance <= prev_distance and attempt < 7: # Υπολογισμός της καλύτερης απόστασης της παρτίδας
			prev_distance = distance
			score = tk.Label(t2_frame, height=1, width= 44, fg='white', bg='darkorchid4', text= "Best Score= " + str(distance) + "% away from the colour", font= ('Verdana', '12'))
			score.grid(row=0, column=2, sticky = tk.NSEW)
			att = tk.Label(at_frame, height=1, width= 10, fg='red', bg='darkorchid4', text= "Attempt " + str(attempt), font= ('Cambria', 24, 'bold'))
			att.grid(row=0, column=2, sticky = tk.NSEW)
		elif distance > prev_distance and attempt < 7 : # Υπολογισμός της καλύτερης απόστασης της παρτίδας
			score = tk.Label(t2_frame, height=1, width= 44, fg='white', bg='darkorchid4', text= "Best Score= " + str(prev_distance) + "% away from the colour", font= ('Verdana', '12'))
			score.grid(row=0, column=2, sticky = tk.NSEW)
			att = tk.Label(at_frame, height=1, width= 10, fg='red', bg='darkorchid4', text= "Attempt " + str(attempt), font= ('Cambria', 24, 'bold'))
			att.grid(row=0, column=2, sticky = tk.NSEW)
		if distance >=10.0 and attempt == 6: # Αν δε τα καταφερει
			att = tk.Label(at_frame, height=1, width= 10, fg='red', bg='darkorchid4', text= "Attempt 5", font= ('Cambria', 24, 'bold'))
			att.grid(row=0, column=2, sticky = tk.NSEW)
			tk.messagebox.showinfo(" ", "YOU LOSE !")
			rst = True
		if distance <= 10.0 and attempt == 2: # Αν τα καταφέρει με τη πρώτη προσπάθεια
			att = tk.Label(at_frame, height=1, width= 10, fg='red', bg='darkorchid4', text= "Attempt " + str(attempt-1), font= ('Cambria', 24, 'bold'))
			att.grid(row=0, column=2, sticky = tk.NSEW)
			tk.messagebox.showinfo(" ", "YOU'RE SKILLED ;D")
			rst = True
		elif distance <= 10.0 and (attempt <= 5 and attempt >= 3):
			att = tk.Label(at_frame, height=1, width= 10, fg='red', bg='darkorchid4', text= "Attempt " + str(attempt-1), font= ('Cambria', 24, 'bold'))
			att.grid(row=0, column=2, sticky = tk.NSEW)
			tk.messagebox.showinfo(" ", "NOT BAD !")
			rst = True
		elif distance <= 10.0 and attempt == 6: # Αν τα καταφέρει με τη τελευταία προσπάθεια
			att = tk.Label(at_frame, height=1, width= 10, fg='red', bg='darkorchid4', text= "Attempt 5", font= ('Cambria', 24, 'bold'))
			att.grid(row=0, column=2, sticky = tk.NSEW)
			tk.messagebox.showinfo(" ", "YOU WIN!")
			rst = True
	elif rst == True:
		distance = 100.00
		prev_distance = 100.00
		att = tk.Label(at_frame, height=1, width= 15, fg='red', bg='darkorchid4', text= " No more Attempts ", font= ('Cambria', 24, 'bold'))
		att.grid(row=0, column=2, sticky = tk.NSEW)
		score = tk.Label(t2_frame, height=1, width= 30, fg='white', bg='darkorchid4', text= " ")
		score.grid(row=0, column=2, sticky = tk.NSEW)
		tk.messagebox.showwarning(" ", "PRESS 'GENERATE' TO PLAY AGAIN!")


if __name__ == '__main__':
	root = tk.Tk() 
	root.title('Match The Colour - Chondromatidis Eleftherios')
	root.resizable(False,False) # Για να μη μπορει να παει fullscreen
	root.geometry("900x600") # Mέγεθος παραθύρου
	root.configure(bg="darkorchid4") # Χρώμα παραθύρου

	red = tk.Scale(root,from_=0,to=255,fg='white',bg='red', sliderlength= 15, orient='horizontal', command= upd) # Slider παίρνει τιμές από 0-255, λευκά γράμματα, κόκκινο bg
	red.grid(row=10, column=0, padx=10, pady=20) 
	green = tk.Scale(root,from_=0,to=255,fg='white', bg='SpringGreen4',sliderlength= 15, orient='horizontal', command= upd)
	green.grid(row=20, column=0, padx=10, pady=20)
	blue = tk.Scale(root,from_=0,to=255,fg='white', bg='dark blue', sliderlength= 15, orient='horizontal', command= upd)
	blue.grid(row=30, column=0,padx=10,pady=20)
	button1 = tk.Button(root, background= 'cyan', foreground= 'darkorchid4',  relief='flat', text= '  Submit  ', cursor= 'hand2', activebackground= 'white', activeforeground= 'cyan', font=('Verdana', 9), command = di) # Κώδικας για τη δημιουργία κουμπιού το οποιο θα κάνει submit το χρώμα του παίκτη
	button1.grid(row=0, column=0, padx=0, pady=0) 
	button1.bind('<Enter>', cursorb1)
	button1.bind('<Leave>', no_cursorb1)
	button2 = tk.Button(root, background= 'cyan', foreground= 'darkorchid4', relief= 'flat', text='Generate', cursor= 'hand2', activebackground= 'white', activeforeground= 'cyan', font=('Verdana', 9), command= random_col) # Κώδικας για τη δημιουργία κουμπιού που θα κάνει generate νέο χρώμα
	button2.grid(row=8, column=0, padx=0, pady=0)
	button2.bind('<Enter>', cursorb2)
	button2.bind('<Leave>', no_cursorb2)
	pl_frame = tk.Frame(root, bg="black", width=450, height=270) # Φτιάχνει ένα πλαίσιο που θα έχει default τιμή το μαύρο και θα αλλάζει ανάλογα με τις επιλογές του χρήστη
	pl_frame.grid(row=50, column=0, padx=0, pady=10)
	ai_frame = tk.Frame(root, bg="black", width=450, height=270)
	ai_frame.grid(row=50, column=2, padx=0, pady=0)
	t_frame = tk.Frame(root, bg="darkorchid4", width=420, height=20)
	t_frame.grid(row=40, column=0, padx=0, pady=0)
	t2_frame = tk.Frame(root, bg="darkorchid4", width=420, height=20)
	t2_frame.grid(row=20, column=2, padx=0, pady=0)
	at_frame = tk.Frame(root, bg="darkorchid4", width=420, height=20)
	at_frame.grid(row=10, column=2, padx=0, pady=0)
	if auto_va == True: # Κλήση της συνάρτησης ώστε να γίνει αυτόματα generated το πρώτο χρώμα
		random_col()
		auto_va = False
	root.mainloop() # Τρέχει όλα τα παραπάνω μέχρι να κλείσουμε το παράθυρο
