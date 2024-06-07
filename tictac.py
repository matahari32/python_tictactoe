import numpy as np


class Game:
    def __init__(self):
        self.__tic = ""
        self.__array = np.array([["", "", ""], ["", "", ""], ["", "", ""]])
        self.__is_game = True

    def __place_tic(self, x, y):
        if self.__array[int(x), int(y)] == "":
            self.__array[int(x), int(y)] = self.__tic
            print(self.__array)
            if self.__check_user_win():
                print(f"Gracz {self.__tic} wygrał!")
                return True
            else:
                self.__tic = "O" if self.__tic == "X" else "X"
        else:
            print("To pole jest już zajęte. Wybierz inne.")
        return False

    def __check_user_win(self):
        if self.__check_x_is_filled() or self.__check_y_is_filled() or self.__check_diagonals():
            return True
        return False

    def __check_x_is_filled(self):
        for row in self.__array:
            if "" not in row and self.__check_values_in_row(row):
                return True
        return False

    def __check_y_is_filled(self):
        for col in range(self.__array.shape[1]):
            column = self.__array[:, col]
            if "" not in column and self.__check_values_in_row(column):
                return True
        return False

    def __check_values_in_row(self, row):
        return all(val == row[0] and val != "" for val in row)

    def __check_diagonals(self):
        main_diagonal = [self.__array[i, i] for i in range(self.__array.shape[0])]
        anti_diagonal = [self.__array[i, self.__array.shape[0] - i - 1] for i in range(self.__array.shape[0])]
        if self.__check_values_in_row(main_diagonal) or self.__check_values_in_row(anti_diagonal):
            return True
        return False

    def play_game(self):
        while True:
            user_input_cell = input(f"Podaj gdzie umieścić {self.__tic} na planszy, "
                                    f"w formacie x:y np. 0:1: ").split(":")
            x, y = user_input_cell[0], user_input_cell[1]
            if self.__place_tic(x, y):
                break
