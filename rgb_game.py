import tkinter as tk
import random as rdm 

def upd(c):
	col_code = '#%02x%02x%02x' % (red.get(), green.get(), blue.get()) # Μετατρέπει τη τιμή των 3 sliders σε 16δικό αριθμό
	pl_frame.config(bg= col_code)
	A = tk.Label(t_frame, height=1, width=15, fg='white', bg= 'black', text = str(red.get()) + "    " + str(green.get()) + "    " + str(blue.get()))
	A.grid(row = 0, column = 0, sticky = tk.NSEW)

def random_col():
	r = rdm.randint(1,254)
	g = rdm.randint(1,254)
	b = rdm.randint(1,254)
	ai_code = '#%02x%02x%02x' % (r, g, b) 
	ai_frame.config (bg= ai_code)



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
	button1 = tk.Button(root, text='Submit', fg= 'cyan', bg= 'darkorchid4') # Κώδικας για τη δημιουργία κουμπιού
	button1.grid(row=0, column=0, padx=0, pady=0) 
	button2 = tk.Button(root, text='Generate', fg= 'cyan', bg= 'darkorchid4', command= random_col) # Κώδικας για τη δημιουργία κουμπιού
	button2.grid(row=5, column=0, padx=0, pady=0)
	pl_frame = tk.Frame(root, bg="black", width=450, height=270) # Φτιάχνει ένα πλαίσιο που θα έχει default τιμή το μαύρο και θα αλλάζει ανάλογα με τις επιλογές του χρήστη
	pl_frame.grid(row=50, column=0, padx=0, pady=10)
	ai_frame = tk.Frame(root, bg="black", width=450, height=270)
	ai_frame.grid(row=50, column=2, padx=0, pady=0)
	t_frame = tk.Frame(root, bg="darkorchid4", width=420, height=20)
	t_frame.grid(row=40, column=0, padx=0, pady=0)
	root.mainloop() # Τρέχει όλα τα παραπάνω μέχρι να κλείσουμε το παράθυρο
