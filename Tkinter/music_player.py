import tkinter as tk

root = tk.Tk()
root.title("Music Player")
root.config(bg = "lightblue")

root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)
root.grid_rowconfigure(3, weight = 1)

def add_to_list():
    value = songEntry.get()
    if value:
        musicList.insert(tk.END, value)
        songEntry.delete(0, tk.END )
    else:
        print("Missing Input")

def remove_from_list():
    value = musicList.curselection()
    if value:
        musicList.delete(value)
    else:
        print("Missing Selection")

def play(event = None):
    selected = musicList.curselection()
    if selected:
        newSong = musicList.get(selected)
        song.set(f"{newSong} is playing")

# TITLE
my_title = tk.Label(root, text = "Music Player", bg = "lightgray")
my_title.grid(row = 0, column = 0, columnspan = 4)

# MUSIC LIST
musicList = tk.Listbox(root)
musicList.grid(row = 1, column = 1, rowspan = 5)

songs = [
    "Bohemian Rhapsody - Queen",
    "Shape of You - Ed Sheeran",
    "Blinding Lights - The Weeknd",
    "Smells Like Teen Spirit - Nirvana",
    "Rolling in the Deep - Adele",
    "Uptown Funk - Mark Ronson ft. Bruno Mars",
    "Hotel California - Eagles",
    "Billie Jean - Michael Jackson",
    "Imagine - John Lennon",
    "Someone You Loved - Lewis Capaldi"
]

for song in songs:
    musicList.insert(tk.END, song)

# SCROLLBAR CONFIG
scrollbar = tk.Scrollbar(root, orient = tk.VERTICAL, command = musicList.yview)
scrollbar.grid(row = 1, column = 0, sticky = "nse", rowspan = 5)
musicList.config(yscrollcommand = scrollbar.set)

# ADD BUTTON
addButton = tk.Button(root, text = "ADD", bg = "lightgray", command = add_to_list)
addButton.grid(row = 2, column = 2, sticky = "nsew")

# REMOVE BUTTON
removeButton = tk.Button(root, text = "REMOVE", bg = "lightgray", command = remove_from_list)
removeButton.grid(row = 3, column = 2, sticky= "nsew")

# PLAY BUTTON
playButton = tk.Button(root, text= "PLAY", bg= "lightgray", command = play)
playButton.grid(row = 4, column = 2, sticky = "nsew")

# SHOW SONGS WIDGET
song = tk.StringVar()
musicList.bind("<<ListboxSelect>>", play)

showSongs = tk.Entry(root, state = "readonly", bg = "lightgray", textvariable = song)
showSongs.grid(row = 1, column = 2, sticky = "nsew")

# ENTRY TAKER
songEntry = tk.Entry(root, bg = "lightgray")
songEntry.grid(row = 5, column = 1, columnspan = 2, sticky = "nsew")

root.mainloop()