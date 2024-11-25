import tkinter as tk
import random

class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong Game")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="black")
        self.canvas.pack()

        self.paddle_a = self.canvas.create_rectangle(10, 170, 25, 230, fill="white")
        self.paddle_b = self.canvas.create_rectangle(575, 170, 590, 230, fill="white")
        self.ball = self.canvas.create_oval(290, 190, 310, 210, fill="white")

        self.score_a = 0
        self.score_b = 0
        self.score_label = tk.Label(root, text=f"Score A: {self.score_a}  Score B: {self.score_b}", fg="white", bg="black")
        self.score_label.pack()

        self.ball_speed_x = 3
        self.ball_speed_y = 3

        self.root.bind("<KeyPress-w>", self.move_paddle_a_up)
        self.root.bind("<KeyPress-s>", self.move_paddle_a_down)
        self.root.bind("<KeyPress-Up>", self.move_paddle_b_up)
        self.root.bind("<KeyPress-Down>", self.move_paddle_b_down)

        self.game_loop()

    def move_paddle_a_up(self, event):
        self.canvas.move(self.paddle_a, 0, -20)
        pos = self.canvas.coords(self.paddle_a)
        if pos[1] < 0:
            self.canvas.move(self.paddle_a, 0, 20)

    def move_paddle_a_down(self, event):
        self.canvas.move(self.paddle_a, 0, 20)
        pos = self.canvas.coords(self.paddle_a)
        if pos[3] > 400:
            self.canvas.move(self.paddle_a, 0, -20)

    def move_paddle_b_up(self, event):
        self.canvas.move(self.paddle_b, 0, -20)
        pos = self.canvas.coords(self.paddle_b)
        if pos[1] < 0:
            self.canvas.move(self.paddle_b, 0, 20)

    def move_paddle_b_down(self, event):
        self.canvas.move(self.paddle_b, 0, 20)
        pos = self.canvas.coords(self.paddle_b)
        if pos[3] > 400:
            self.canvas.move(self.paddle_b, 0, -20)

    def game_loop(self):
        self.move_ball()
        self.check_collision()
        self.root.after(10, self.game_loop)

    def move_ball(self):
        self.canvas.move(self.ball, self.ball_speed_x, self.ball_speed_y)
        pos = self.canvas.coords(self.ball)

        if pos[1] <= 0 or pos[3] >= 400:
            self.ball_speed_y *= -1

        if pos[0] <= 0:
            self.score_b += 1
            self.reset_ball()
            self.update_score()

        if pos[2] >= 600:
            self.score_a += 1
            self.reset_ball()
            self.update_score()

    def check_collision(self):
        ball_pos = self.canvas.coords(self.ball)
        paddle_a_pos = self.canvas.coords(self.paddle_a)
        paddle_b_pos = self.canvas.coords(self.paddle_b)

        if ball_pos[2] >= paddle_b_pos[0] and ball_pos[0] <= paddle_b_pos[2]:
            if ball_pos[3] >= paddle_b_pos[1] and ball_pos[1] <= paddle_b_pos[3]:
                self.ball_speed_x *= -1

        if ball_pos[2] >= paddle_a_pos[0] and ball_pos[0] <= paddle_a_pos[2]:
            if ball_pos[3] >= paddle_a_pos[1] and ball_pos[1] <= paddle_a_pos[3]:
                self.ball_speed_x *= -1

    def reset_ball(self):
        self.canvas.coords(self.ball, 290, 190, 310, 210)
        self.ball_speed_x *= random.choice([-1, 1])
        self.ball_speed_y *= random.choice([-1, 1])

    def update_score(self):
        self.score_label.config(text=f"Score A: {self.score_a}  Score B: {self.score_b}")

if __name__ == "__main__":
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()
