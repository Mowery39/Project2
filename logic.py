from PyQt6.QtWidgets import QMainWindow
from gui import *
import random


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2_stay.clicked.connect(lambda: self.stay())
        self.pushButton_clear.clicked.connect(lambda: self.clear())
        self.pushButton_hit.clicked.connect(lambda: self.hit(self.your_score))

        AI_scores = [17, 18, 19, 20, 21, 22, 23, 24, 25]
        first_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.AI_score = random.choice(AI_scores)
        self.label_2_AI_current_round_score.setText(f'{self.AI_score}')
        self.your_score = random.choice(first_cards)
        self.label_your_current_round_score.setText(f'{self.your_score}')

    def stay(self):
        if self.your_score == self.AI_score:
            self.label_you_win.setText('You TIED!')
        elif (self.your_score > self.AI_score or self.AI_score > 21) and self.your_score <= 21:
            self.label_you_win.setText('YOU WIN!')
        else:
            self.label_AI_wins.setText('AI WINS!')

        # Fix this to display who wins when user clicks stay

    def clear(self):
        self.label_2_AI_current_round_score.clear()
        self.label_your_current_round_score.clear()
        self.label_Error.clear()
        self.label_AI_wins.clear()
        self.label_you_win.clear()
        AI_scores = [17, 18, 19, 20, 21, 22, 23, 24, 25]
        self.AI_score = random.choice(AI_scores)
        self.label_2_AI_current_round_score.setText(f'{self.AI_score}')
        self.your_score = 0

    def hit(self, your_score):
        # Score should add on to previous score
        # Figure out how to keep the AI's score after first hit click
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        card_you_pull = random.choice(cards)
        while True:
            try:
                round_total = card_you_pull + your_score
                self.label_your_current_round_score.setText(f'{round_total}')
                self.your_score = round_total
            except ValueError:
                self.label_Error.setText(f'Pls Put in A NUM')
                break
            else:
                print(card_you_pull)
                print(your_score)
                print(card_you_pull + your_score)
                break
