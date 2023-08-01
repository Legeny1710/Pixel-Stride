import pygame


class Score:
    current_score = 0
    delay_time = 0

    def __init__(self):
        pygame.font.init()
        self.game_font = pygame.font.Font("Pixeltype.ttf", 50)
        self.score_text = self.game_font.render(f"Score:{self.current_score}", False, (64, 64, 64))
        self.score_text_rect = self.score_text.get_rect(center=(400, 100))
        self.best_score_text = self.game_font.render(f"Best Score: 0", False, (64, 64, 64))
        self.best_score_text_rect = self.best_score_text.get_rect(center=(400, 100))
        with open("score_storage.txt", "r+") as score_file:
            if score_file.readline() == "":
                score_file.write("best_score: 0")

    def update_score(self):
        self.current_score += 0.2
        self.score_text = self.game_font.render(f"Score: {int(self.current_score)}", False, (64, 64, 64))
        self.score_text_rect = self.score_text.get_rect(center=(400, 100))

    def save_score(self):
        if self.current_score >= self.show_best_score():
            with open("score_storage.txt", "w") as score_file:
                score_file.write(f"best_score: {int(self.current_score)}")

    def show_best_score(self):
        with open("score_storage.txt", "r") as score_file:
            best_score_list = score_file.readline().split(" ")
            best_score = int(best_score_list[1])
            return best_score

    def compare_current_score(self):
        with open("score_storage.txt", "r") as score_file:
            best_score_list = score_file.readline().split(" ")
            best_score = int(best_score_list[1])
            return self.current_score - best_score
