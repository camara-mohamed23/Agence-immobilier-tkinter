import tkinter as tk
from tkinter import ttk

# Couleurs principales
PRIMARY_BG = "#e6f5f6"
HEADER_TOP = "#0c546e"
CARD_BG = "#ffffff"
ACCENT = "#ff5a5f"
TEXT_DARK = "#18212f"

root = tk.Tk()
root.title("Real Estate UI")
root.geometry("1100x780")
root.configure(bg=PRIMARY_BG)

# --------- HEADER ---------
header = tk.Frame(root, bg=HEADER_TOP, height=260)
header.pack(fill="x", side="top")
header.grid_columnconfigure(0, weight=1)
header.grid_columnconfigure(1, weight=1)

title_frame = tk.Frame(header, bg=HEADER_TOP)
title_frame.grid(row=0, column=0, sticky="w", padx=50, pady=40)

title_label = tk.Label(
    title_frame,
    text="Find Your\nDream Home",
    bg=HEADER_TOP,
    fg="white",
    font=("Segoe UI", 28, "bold")
)
title_label.pack(anchor="w")

subtitle = tk.Label(
    title_frame,
    text="Browse thousands of listings and find the perfect place.",
    bg=HEADER_TOP,
    fg="#cde6ed",
    font=("Segoe UI", 11)
)
subtitle.pack(anchor="w", pady=(10, 20))

cta_btn = tk.Button(
    title_frame,
    text="Search Now",
    bg=ACCENT,
    fg="white",
    bd=0,
    padx=20,
    pady=10,
    font=("Segoe UI", 11, "bold")
)
cta_btn.pack(anchor="w")

# Bloc image à droite (placeholder)
image_placeholder = tk.Frame(header, bg="#264b63", width=380, height=220)
image_placeholder.grid(row=0, column=1, sticky="e", padx=50, pady=20)
image_placeholder.grid_propagate(False)

img_label = tk.Label(
    image_placeholder,
    text="IMAGE\n(immeuble)",
    fg="white",
    bg="#264b63",
    font=("Segoe UI", 14, "bold")
)
img_label.place(relx=0.5, rely=0.5, anchor="center")

# --------- BARRE DE RECHERCHE ---------
search_bar = tk.Frame(root, bg=PRIMARY_BG)
search_bar.pack(fill="x", padx=40, pady=(40, 10))  # chevauche un peu le header


search_box = tk.Frame(search_bar, bg=CARD_BG, bd=0, relief="flat")
search_box.pack(fill="x", padx=40)
search_box.grid_columnconfigure((0, 1, 2, 3), weight=1)

def make_field(parent, label, row, col):
    f = tk.Frame(parent, bg=CARD_BG)
    f.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
    tk.Label(
        f, text=label, bg=CARD_BG, fg="#7b8ca5",
        font=("Segoe UI", 9)
    ).pack(anchor="w")
    e = ttk.Entry(f)
    e.pack(fill="x", pady=(3, 0))
    return e

location_entry = make_field(search_box, "Location", 0, 0)
type_entry = make_field(search_box, "Property Type", 0, 1)
price_entry = make_field(search_box, "Max Price", 0, 2)

search_btn = tk.Button(
    search_box,
    text="Search",
    bg=ACCENT,
    fg="white",
    bd=0,
    padx=20,
    pady=10,
    font=("Segoe UI", 10, "bold")
)
search_btn.grid(row=0, column=3, padx=10, pady=10, sticky="e")

# --------- CONTENU PRINCIPAL ---------
content = tk.Frame(root, bg=PRIMARY_BG)
content.pack(fill="both", expand=True, padx=40, pady=10)

section_title = tk.Label(
    content,
    text="Featured listings",
    bg=PRIMARY_BG,
    fg=TEXT_DARK,
    font=("Segoe UI", 18, "bold")
)
section_title.pack(anchor="w", pady=(10, 15))

cards_frame = tk.Frame(content, bg=PRIMARY_BG)
cards_frame.pack(fill="x")

def create_card(parent, title, price, beds, baths):
    card = tk.Frame(parent, bg=CARD_BG, bd=0, relief="flat")
    card.pack(side="left", padx=10, pady=5, expand=True, fill="both")

    top_img = tk.Frame(card, bg="#203951", height=120)
    top_img.pack(fill="x")
    top_img.pack_propagate(False)
    tk.Label(
        top_img,
        text="IMAGE",
        bg="#203951",
        fg="white",
        font=("Segoe UI", 10, "bold")
    ).place(relx=0.5, rely=0.5, anchor="center")

    body = tk.Frame(card, bg=CARD_BG)
    body.pack(fill="both", padx=10, pady=10)

    tk.Label(
        body,
        text=title,
        bg=CARD_BG,
        fg=TEXT_DARK,
        font=("Segoe UI", 12, "bold")
    ).pack(anchor="w")

    tk.Label(
        body,
        text=price,
        bg=CARD_BG,
        fg=ACCENT,
        font=("Segoe UI", 11, "bold")
    ).pack(anchor="w", pady=(5, 8))

    info = tk.Frame(body, bg=CARD_BG)
    info.pack(anchor="w")
    tk.Label(
        info,
        text=f"{beds} beds",
        bg=CARD_BG,
        fg="#7b8ca5",
        font=("Segoe UI", 9)
    ).pack(side="left")
    tk.Label(
        info,
        text=" • ",
        bg=CARD_BG,
        fg="#7b8ca5",
        font=("Segoe UI", 9)
    ).pack(side="left")
    tk.Label(
        info,
        text=f"{baths} baths",
        bg=CARD_BG,
        fg="#7b8ca5",
        font=("Segoe UI", 9)
    ).pack(side="left")

# Trois cartes de biens
create_card(cards_frame, "Modern Apartment", "$1,200 / month", 2, 1)
create_card(cards_frame, "Family House", "$2,400 / month", 4, 2)
create_card(cards_frame, "Luxury Condo", "$3,100 / month", 3, 2)

# --------- SECTION DU BAS (style grid) ---------
bottom = tk.Frame(content, bg=PRIMARY_BG)
bottom.pack(fill="both", expand=True, pady=(30, 0))

# Texte de gauche
left_text = tk.Frame(bottom, bg=PRIMARY_BG)
left_text.pack(side="left", fill="both", expand=True)

tk.Label(
    left_text,
    text="Ours is your\nbest evening rest",
    bg=PRIMARY_BG,
    fg=TEXT_DARK,
    font=("Segoe UI", 20, "bold")
).pack(anchor="w")

tk.Label(
    left_text,
    text="Short marketing sentence explaining why this agency is great.",
    bg=PRIMARY_BG,
    fg="#607086",
    font=("Segoe UI", 11),
    wraplength=350,
    justify="left"
).pack(anchor="w", pady=(10, 20))

# Grille de petites cartes à droite
right_grid = tk.Frame(bottom, bg=PRIMARY_BG)
right_grid.pack(side="right", fill="both", expand=True)

for r in range(2):
    for c in range(2):
        small = tk.Frame(right_grid, bg=CARD_BG)
        small.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
        right_grid.grid_columnconfigure(c, weight=1)
        right_grid.grid_rowconfigure(r, weight=1)

        img = tk.Frame(small, bg="#203951", height=80)
        img.pack(fill="x")
        img.pack_propagate(False)
        tk.Label(
            img,
            text="IMG",
            bg="#203951",
            fg="white",
            font=("Segoe UI", 9, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            small,
            text="Building Title",
            bg=CARD_BG,
            fg=TEXT_DARK,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=8, pady=(5, 2))

        tk.Label(
            small,
            text="Small description...",
            bg=CARD_BG,
            fg="#7b8ca5",
            font=("Segoe UI", 9),
            wraplength=160,
            justify="left"
        ).pack(anchor="w", padx=8, pady=(0, 8))

root.mainloop()
import tkinter as tk
from tkinter import ttk

# Couleurs principales
PRIMARY_BG = "#e6f5f6"
HEADER_TOP = "#0c546e"
CARD_BG = "#ffffff"
ACCENT = "#ff5a5f"
TEXT_DARK = "#18212f"

root = tk.Tk()
root.title("Real Estate UI")
root.geometry("1100x780")
root.configure(bg=PRIMARY_BG)

# --------- HEADER ---------
header = tk.Frame(root, bg=HEADER_TOP, height=260)
header.pack(fill="x", side="top")
header.grid_columnconfigure(0, weight=1)
header.grid_columnconfigure(1, weight=1)

title_frame = tk.Frame(header, bg=HEADER_TOP)
title_frame.grid(row=0, column=0, sticky="w", padx=50, pady=40)

title_label = tk.Label(
    title_frame,
    text="Find Your\nDream Home",
    bg=HEADER_TOP,
    fg="white",
    font=("Segoe UI", 28, "bold")
)
title_label.pack(anchor="w")

subtitle = tk.Label(
    title_frame,
    text="Browse thousands of listings and find the perfect place.",
    bg=HEADER_TOP,
    fg="#cde6ed",
    font=("Segoe UI", 11)
)
subtitle.pack(anchor="w", pady=(10, 20))

cta_btn = tk.Button(
    title_frame,
    text="Search Now",
    bg=ACCENT,
    fg="white",
    bd=0,
    padx=20,
    pady=10,
    font=("Segoe UI", 11, "bold")
)
cta_btn.pack(anchor="w")

# Bloc image à droite (placeholder)
image_placeholder = tk.Frame(header, bg="#264b63", width=380, height=220)
image_placeholder.grid(row=0, column=1, sticky="e", padx=50, pady=20)
image_placeholder.grid_propagate(False)

img_label = tk.Label(
    image_placeholder,
    text="IMAGE\n(immeuble)",
    fg="white",
    bg="#264b63",
    font=("Segoe UI", 14, "bold")
)
img_label.place(relx=0.5, rely=0.5, anchor="center")

# --------- BARRE DE RECHERCHE ---------
search_bar = tk.Frame(root, bg=PRIMARY_BG)
search_bar.pack(fill="x", padx=40, pady=(-40, 10))

search_box = tk.Frame(search_bar, bg=CARD_BG, bd=0, relief="flat")
search_box.pack(fill="x", padx=40)
search_box.grid_columnconfigure((0, 1, 2, 3), weight=1)

def make_field(parent, label, row, col):
    f = tk.Frame(parent, bg=CARD_BG)
    f.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
    tk.Label(
        f, text=label, bg=CARD_BG, fg="#7b8ca5",
        font=("Segoe UI", 9)
    ).pack(anchor="w")
    e = ttk.Entry(f)
    e.pack(fill="x", pady=(3, 0))
    return e

location_entry = make_field(search_box, "Location", 0, 0)
type_entry = make_field(search_box, "Property Type", 0, 1)
price_entry = make_field(search_box, "Max Price", 0, 2)

search_btn = tk.Button(
    search_box,
    text="Search",
    bg=ACCENT,
    fg="white",
    bd=0,
    padx=20,
    pady=10,
    font=("Segoe UI", 10, "bold")
)
search_btn.grid(row=0, column=3, padx=10, pady=10, sticky="e")

# --------- CONTENU PRINCIPAL ---------
content = tk.Frame(root, bg=PRIMARY_BG)
content.pack(fill="both", expand=True, padx=40, pady=10)

section_title = tk.Label(
    content,
    text="Featured listings",
    bg=PRIMARY_BG,
    fg=TEXT_DARK,
    font=("Segoe UI", 18, "bold")
)
section_title.pack(anchor="w", pady=(10, 15))

cards_frame = tk.Frame(content, bg=PRIMARY_BG)
cards_frame.pack(fill="x")

def create_card(parent, title, price, beds, baths):
    card = tk.Frame(parent, bg=CARD_BG, bd=0, relief="flat")
    card.pack(side="left", padx=10, pady=5, expand=True, fill="both")

    top_img = tk.Frame(card, bg="#203951", height=120)
    top_img.pack(fill="x")
    top_img.pack_propagate(False)
    tk.Label(
        top_img,
        text="IMAGE",
        bg="#203951",
        fg="white",
        font=("Segoe UI", 10, "bold")
    ).place(relx=0.5, rely=0.5, anchor="center")

    body = tk.Frame(card, bg=CARD_BG)
    body.pack(fill="both", padx=10, pady=10)

    tk.Label(
        body,
        text=title,
        bg=CARD_BG,
        fg=TEXT_DARK,
        font=("Segoe UI", 12, "bold")
    ).pack(anchor="w")

    tk.Label(
        body,
        text=price,
        bg=CARD_BG,
        fg=ACCENT,
        font=("Segoe UI", 11, "bold")
    ).pack(anchor="w", pady=(5, 8))

    info = tk.Frame(body, bg=CARD_BG)
    info.pack(anchor="w")
    tk.Label(
        info,
        text=f"{beds} beds",
        bg=CARD_BG,
        fg="#7b8ca5",
        font=("Segoe UI", 9)
    ).pack(side="left")
    tk.Label(
        info,
        text=" • ",
        bg=CARD_BG,
        fg="#7b8ca5",
        font=("Segoe UI", 9)
    ).pack(side="left")
    tk.Label(
        info,
        text=f"{baths} baths",
        bg=CARD_BG,
        fg="#7b8ca5",
        font=("Segoe UI", 9)
    ).pack(side="left")

# Trois cartes de biens
create_card(cards_frame, "Modern Apartment", "$1,200 / month", 2, 1)
create_card(cards_frame, "Family House", "$2,400 / month", 4, 2)
create_card(cards_frame, "Luxury Condo", "$3,100 / month", 3, 2)

# --------- SECTION DU BAS (style grid) ---------
bottom = tk.Frame(content, bg=PRIMARY_BG)
bottom.pack(fill="both", expand=True, pady=(30, 0))

# Texte de gauche
left_text = tk.Frame(bottom, bg=PRIMARY_BG)
left_text.pack(side="left", fill="both", expand=True)

tk.Label(
    left_text,
    text="Ours is your\nbest evening rest",
    bg=PRIMARY_BG,
    fg=TEXT_DARK,
    font=("Segoe UI", 20, "bold")
).pack(anchor="w")

tk.Label(
    left_text,
    text="Short marketing sentence explaining why this agency is great.",
    bg=PRIMARY_BG,
    fg="#607086",
    font=("Segoe UI", 11),
    wraplength=350,
    justify="left"
).pack(anchor="w", pady=(10, 20))

# Grille de petites cartes à droite
right_grid = tk.Frame(bottom, bg=PRIMARY_BG)
right_grid.pack(side="right", fill="both", expand=True)

for r in range(2):
    for c in range(2):
        small = tk.Frame(right_grid, bg=CARD_BG)
        small.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
        right_grid.grid_columnconfigure(c, weight=1)
        right_grid.grid_rowconfigure(r, weight=1)

        img = tk.Frame(small, bg="#203951", height=80)
        img.pack(fill="x")
        img.pack_propagate(False)
        tk.Label(
            img,
            text="IMG",
            bg="#203951",
            fg="white",
            font=("Segoe UI", 9, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            small,
            text="Building Title",
            bg=CARD_BG,
            fg=TEXT_DARK,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", padx=8, pady=(5, 2))

        tk.Label(
            small,
            text="Small description...",
            bg=CARD_BG,
            fg="#7b8ca5",
            font=("Segoe UI", 9),
            wraplength=160,
            justify="left"
        ).pack(anchor="w", padx=8, pady=(0, 8))

root.mainloop()
