import tkinter as tk
from tkinter import messagebox

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Perjalanan Hidup")
        self.stage = 0
        self.score = 0

        self.story_text = tk.Label(root, text="", wraplength=400, font=("Arial", 12))
        self.story_text.pack(pady=20)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.option1 = tk.Button(self.button_frame, text="", width=20, command=lambda: self.choose(1))
        self.option2 = tk.Button(self.button_frame, text="", width=20, command=lambda: self.choose(0))

        self.option1.grid(row=0, column=0, padx=10)
        self.option2.grid(row=0, column=1, padx=10)

        self.next_stage()

    def next_stage(self):
        self.stage += 1
        if self.stage == 1:
            self.story_text.config(text="Stage 1: Masa Kecil\nKamu melihat dua anak bertengkar di taman. Apa yang kamu lakukan?")
            self.option1.config(text="Bantu", command=lambda: self.choose(1))
            self.option2.config(text="Abaikan", command=lambda: self.choose(0))
        elif self.stage == 2:
            self.story_text.config(text="Stage 2: Remaja\nKamu diajak mencontek saat ujian. Apa yang kamu lakukan?")
            self.option1.config(text="Tolak", command=lambda: self.choose(1))
            self.option2.config(text="Ikut", command=lambda: self.choose(0))
        elif self.stage == 3:
            self.story_text.config(text="Stage 3: Dewasa\nKamu mendapat tawaran kerja yang merugikan orang lain. Apa yang kamu pilih?")
            self.option1.config(text="Tolak", command=lambda: self.choose(1))
            self.option2.config(text="Ambil", command=lambda: self.choose(0))
        else:
            self.ending()

    def choose(self, point):
        self.score += point
        self.next_stage()

    def ending(self):
        self.option1.pack_forget()
        self.option2.pack_forget()
        if self.score >= 2:
            ending_text = "Kamu menjalani hidup dengan hati nurani.\nEnding: BAIK."
        else:
            ending_text = "Pilihanmu membuatmu kehilangan arah.\nEnding: BURUK."
        self.story_text.config(text=ending_text)
        messagebox.showinfo("Akhir", ending_text)
        self.root.after(3000, self.root.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
