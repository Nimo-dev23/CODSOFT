import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors Game")

        self.user_choice = None
        self.computer_choice = None
        self.result_text = tk.StringVar()
        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Choose Rock, Paper, or Scissors:").pack()

        choices = ["Rock", "Paper", "Scissors"]
        for choice in choices:
            tk.Button(self.window, text=choice, command=lambda c=choice: self.play_round(c)).pack()

        self.result_label = tk.Label(self.window, textvariable=self.result_text)
        self.result_label.pack()

        self.score_label = tk.Label(self.window, text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")
        self.score_label.pack()

        self.play_again_button = tk.Button(self.window, text="Play Again", command=self.reset)
        self.play_again_button.pack()

    def play_round(self, user_choice):
        self.user_choice = user_choice
        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner()
        self.update_result_text(result)
        self.update_score(result)

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            return "It's a tie!"
        elif (self.user_choice == "Rock" and self.computer_choice == "Scissors") or \
             (self.user_choice == "Scissors" and self.computer_choice == "Paper") or \
             (self.user_choice == "Paper" and self.computer_choice == "Rock"):
            return "You win!"
        else:
            return "You lose!"

    def update_result_text(self, result):
        self.result_text.set(f"User chose {self.user_choice}, Computer chose {self.computer_choice}. {result}")

    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1
        self.score_label.config(text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")

    def reset(self):
        self.user_choice = None
        self.computer_choice = None
        self.result_text.set("")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()
