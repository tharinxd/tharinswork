import tkinter as tk

def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index[0])
        result_label.config(text=f"Selected Item: {selected_item}")
    else:
        result_label.config(text="No item selected")

# Create the main application window
root = tk.Tk()
root.title("Listbox Example")

# Create a Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Populate the Listbox with items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

# Bind the selection event to the on_select function
listbox.bind('<<ListboxSelect>>', on_select)

# Label to display the selected item
result_label = tk.Label(root, text="No item selected")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

