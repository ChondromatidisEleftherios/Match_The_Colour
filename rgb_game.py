import tkinter as tk
def upd(c):
	col_code = '#%02x%02x%02x' % (red.get(), green.get(), blue.get()) # Μετατρέπει τη τιμή των 3 sliders σε 16δικό αριθμό
	pl_frame.config(bg= col_code)
	


if __name__ == '__main__':
	root = tk.Tk() 
	root.resizable(False,False) # Για να μη μπορει να παει fullscreen
	root.geometry("900x600") # Mέγεθος παραθύρου
	root.configure(bg="darkorchid4") # Χρώμα παραθύρου

	red = tk.Scale(root,from_=0,to=255,fg='white',bg='red', sliderlength= 15, orient='horizontal', command= upd) # Slider παίρνει τιμές από 0-255, λευκά γράμματα, κόκκινο bg
	red.grid(row=10, column=0, padx=10, pady=20) 
	green = tk.Scale(root,from_=0,to=255,fg='white', bg='SpringGreen4',sliderlength= 15, orient='horizontal', command= upd)
	green.grid(row=20, column=0, padx=10, pady=20)
	blue = tk.Scale(root,from_=0,to=255,fg='white', bg='dark blue', sliderlength= 15, orient='horizontal', command= upd)
	blue.grid(row=30, column=0,padx=10,pady=20)
	button = tk.Button(root, text='Υποβολή', fg= 'cyan', bg= 'darkorchid4') # Κώδικας για τη δημιουργία κουμπιού
	button.grid(row=0, column=0, padx=12, pady=22) 
	pl_frame = tk.Frame(root, bg="black", width=420, height=240) # Φτιάχνει ένα πλαίσιο που θα έχει default τιμή το μαύρο και θα αλλάζει ανάλογα με τις επιλογές του χρήστη
	pl_frame.grid(row=50, column=0, padx=0, pady=50)
	root.mainloop() # Τρέχει όλα τα παραπάνω μέχρι να κλείσουμε το παράθυρο
