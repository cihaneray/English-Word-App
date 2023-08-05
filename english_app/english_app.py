import json

from customtkinter import *
from CTkListbox import *
from random import randint
from CTkMessagebox import CTkMessagebox


class App:
    def __init__(self):
        self.word_class = Word()
        self.crossword = Crossword()

        self.word_list = self.word_class.get_word_list()
        self.sentence_list = {}

        self.font = ("Roboto", 25)

        for i in self.word_list:
            self.sentence_list[i] = self.word_class.get_attr(i)

        self.app = CTk()

        self.app.title("App")
        self.app.minsize(1050, 600)
        self.app.geometry(self.center_window(self.app, 1050, 600))

        self.frame_entry = CTkFrame(self.app, corner_radius=20)
        self.frame_entry.place(relx=0.05, relwidth=0.55,
                               rely=0.05, relheight=0.425)

        self.frame_crossword = CTkFrame(self.app, corner_radius=20)
        self.frame_crossword.place(relx=0.05, relwidth=0.55,
                                   rely=0.525, relheight=0.425)

        self.frame_list = CTkFrame(self.app, corner_radius=20)
        self.frame_list.place(relx=0.65, relwidth=0.30,
                              rely=0.05, relheight=0.9)

        self.crossword_game_frame = CTkFrame(self.frame_crossword)

        self.word_label = CTkLabel(self.frame_entry, text="Word: ", font=self.font, anchor=E)
        self.word_label.place(relx=0.05, relwidth=0.2,
                              rely=0.0875, relheight=0.15)

        self.word_entry = CTkEntry(self.frame_entry, textvariable=StringVar(), font=self.font)
        self.word_entry.place(relx=0.25, relwidth=0.7,
                              rely=0.0875, relheight=0.15)

        self.sentence_label = CTkLabel(self.frame_entry, text="Sentence: ", font=self.font, anchor=E)
        self.sentence_label.place(relx=0.05, relwidth=0.2,
                                  rely=0.325, relheight=0.15)

        self.sentence_entry = CTkEntry(self.frame_entry, font=self.font)
        self.sentence_entry.place(relx=0.25, relwidth=0.7,
                                  rely=0.325, relheight=0.15)

        self.mean_label = CTkLabel(self.frame_entry, text="Mean: ", font=self.font, anchor=E)
        self.mean_label.place(relx=0.05, relwidth=0.2,
                              rely=0.5825, relheight=0.15)

        self.mean_entry = CTkEntry(self.frame_entry, textvariable=StringVar(), font=self.font)
        self.mean_entry.place(relx=0.25, relwidth=0.7,
                              rely=0.5825, relheight=0.15)

        self.entry_button = CTkButton(self.frame_entry, text="Submit", font=self.font,
                                      command=self.__save__)
        self.entry_button.place(relx=0.3, relwidth=0.4,
                                rely=0.82, relheight=0.15)

        self.show_process_frame = CTkFrame(self.frame_entry, width=250, height=150)

        self.show_process_label = CTkLabel(self.show_process_frame)
        self.show_process_label.place(relx=0.02, relwidth=0.96,
                                      rely=0.02, relheight=0.86)

        self.show_process_button = CTkButton(self.show_process_frame, text="OK",
                                             command=self.show_process_frame.place_forget)
        self.show_process_button.place(relx=0.02, relwidth=0.96,
                                       rely=0.88, relheight=0.1)

        self.crossword_label = CTkLabel(self.frame_crossword, text="Crossword Game", font=self.font, anchor=S)
        self.crossword_label.place(relx=0.3, relwidth=0.4,
                                   rely=0.05, relheight=0.15)

        self.crossword_initial_frame = CTkFrame(self.frame_crossword, corner_radius=20)
        self.crossword_initial_frame.place(relx=0.05, relwidth=0.9,
                                           rely=0.25, relheight=0.7)

        self.crossword_button = CTkButton(self.crossword_initial_frame, text="PLAY", font=self.font,
                                          command=self.play_crossword)
        self.crossword_button.place(relx=0.3, relwidth=0.4,
                                    rely=0.07, relheight=0.24)

        self.crossword_word_number = CTkLabel(self.crossword_initial_frame,
                                              text=f"Total word: {self.crossword.get_size()}", font=self.font)
        self.crossword_word_number.place(relx=0.3, relwidth=0.4,
                                         rely=0.38, relheight=0.24)

        self.crossword_best_score = CTkLabel(self.crossword_initial_frame,
                                             text=Crossword.save_get_score(save=False, get=True), font=self.font)
        self.crossword_best_score.place(relx=0.3, relwidth=0.4,
                                        rely=0.69, relheight=0.24)

        self.crossword_dif_frame = CTkFrame(self.frame_crossword, corner_radius=20)

        self.crossword_dif_lev_easy_btn = CTkButton(self.crossword_dif_frame, text="EASY", font=self.font,
                                                    command=lambda: self.init_play(0))
        self.crossword_dif_lev_easy_btn.place(relx=0.3, relwidth=0.4,
                                              rely=0.08, relheight=0.15)

        self.crossword_dif_lev_norm_btn = CTkButton(self.crossword_dif_frame, text="NORMAL", font=self.font,
                                                    command=lambda: self.init_play(1))
        self.crossword_dif_lev_norm_btn.place(relx=0.3, relwidth=0.4,
                                              rely=0.31, relheight=0.15)

        self.crossword_dif_lev_hard_btn = CTkButton(self.crossword_dif_frame, text="HARD", font=self.font,
                                                    command=lambda: self.init_play(2))
        self.crossword_dif_lev_hard_btn.place(relx=0.3, relwidth=0.4,
                                              rely=0.54, relheight=0.15)

        self.crossword_dif_lev_back_btn = CTkButton(self.crossword_dif_frame, text="BACK", font=self.font,
                                                    command=self.back_to_crossword_initial_frame)
        self.crossword_dif_lev_back_btn.place(relx=0.3, relwidth=0.4,
                                              rely=0.77, relheight=0.15)

        self.list_box = CTkListbox(self.frame_list, command=self.show_sentence)
        self.list_box.place(relx=0.07, relwidth=0.86,
                            rely=0.1, relheight=0.86)
        self.list_box.insert(0, "Please type in search!")

        self.search_entry = CTkEntry(self.frame_list, textvariable=StringVar())
        self.search_entry.place(relx=0.07, relwidth=0.49,
                                rely=0.02, relheight=0.06)

        self.search_btn = CTkButton(self.frame_list, text="Search", command=self.search)
        self.search_btn.place(relx=0.63, relwidth=0.3,
                              rely=0.02, relheight=0.06)

        self.crossword_back_button = CTkButton(self.crossword_game_frame,
                                               text="<", font=self.font,
                                               command=lambda: self.init_play(-1))

        self.crossword_main_title = CTkLabel(self.crossword_game_frame, text="CrossWord", font=self.font)

        self.crossword_word_label = CTkLabel(self.crossword_game_frame,
                                             font=self.font, bg_color="#3A4241")

        self.crossword_mean_label = CTkLabel(self.crossword_game_frame,
                                             font=self.font, bg_color="#3A4241")

        self.crossword_word_entry = CTkEntry(self.crossword_game_frame, textvariable=StringVar(), font=self.font)

        self.crossword_reshuffle_button = CTkButton(self.crossword_game_frame, text="Reshuffle",
                                                    font=self.font,
                                                    command=lambda: self.crossword_word_label.configure(
                                                        text=f"Word:   {self.crossword.reshuffle()}"))

        self.crossword_score_label = CTkLabel(self.crossword_game_frame,
                                              text=f"Score is {0}", font=self.font, bg_color="#3A4241")

        self.crossword_answer_frame = CTkFrame(self.app)

        self.crossword_answer_label = CTkLabel(self.crossword_answer_frame, font=self.font, bg_color="black")

        self.crossword_answer_button = CTkButton(self.crossword_answer_frame, text="Okay", font=self.font,
                                                 command=self.okay)

        self.crossword_check_button = CTkButton(
            self.crossword_game_frame, text="Submit", font=self.font,
            command=lambda: self.change_word_mean(self.crossword.is_true(self.crossword_word_entry.get())))

        self.app.mainloop()

    def __save__(self):
        temp_text = self.word_class.save(word=self.word_entry.get(),
                                         mean=self.mean_entry.get(),
                                         sentence=self.sentence_entry.get())

        self.show_process_label.configure(text=temp_text)
        self.word_entry.delete(0, END)
        self.sentence_entry.delete(0, END)
        self.mean_entry.delete(0, END)
        self.show_process_frame.place(relx=0.1, relwidth=0.8,
                                      rely=0.1, relheight=0.8)

    def __insert__(self, searched_list: list | tuple):
        for i in range(len(searched_list)):
            self.list_box.insert(i, searched_list[i])

    def clear(self):
        self.search_entry.delete(0, END)
        for i in range(self.list_box.size()):
            self.list_box.delete(i)

    def search(self):
        search_text = self.search_entry.get().lower()
        word_list = self.word_class.get_word_list()
        searched_word_list = []
        self.clear()
        for i in word_list:
            if search_text in i:
                searched_word_list.append(i)
        self.__insert__(searched_word_list)

    @staticmethod
    def center_window(master, width: int, height: int):
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_coordinate = (screen_width - width) // 2
        y_coordinate = (screen_height - height) // 2
        return f"{width}x{height}+{x_coordinate + 100}+{y_coordinate}"

    def show_sentence(self, word):
        if word != "Please type in search!":
            sentence = self.sentence_list[word][0]
            mean = self.sentence_list[word][1]
            # noinspection PyProtectedMember
            CTkMessagebox(title=f"{word.capitalize()}", message=f"Mean: {mean}\nSentence: {sentence}",
                          icon="none", width=500, border_color="green").info._text_label.configure(wraplength=480)

    def play_crossword(self):
        self.crossword_initial_frame.place_forget()
        self.crossword_dif_frame.place(relx=0.05, relwidth=0.9,
                                       rely=0.25, relheight=0.7)

    def back_to_crossword_initial_frame(self):
        self.crossword_dif_frame.place_forget()
        self.crossword_initial_frame.place(relx=0.05, relwidth=0.9,
                                           rely=0.25, relheight=0.7)

    def set_level(self, level: int):
        if level == 0:
            self.crossword_reshuffle_button.place(relx=0.67, relwidth=0.31,
                                                  rely=0.39, relheight=0.14)
            self.crossword_mean_label.place(relx=0.15, relwidth=0.5,
                                            rely=0.43, relheight=0.13)
        elif level == 1:
            self.crossword_mean_label.place(relx=0.15, relwidth=0.5,
                                            rely=0.43, relheight=0.13)
            self.crossword_reshuffle_button.place_forget()
        elif level == 2:
            self.crossword_mean_label.place_forget()
            self.crossword_reshuffle_button.place(relx=0.15, relwidth=0.5,
                                                  rely=0.43, relheight=0.13)

    def init_play(self, dif_lev):
        if dif_lev == -1:
            return self.back_to_crossword_dif_frame()
        else:
            self.crossword_score_label.configure(text=f"Score is {0}")
            mixed_word, mean = self.crossword.shuffle()
            self.crossword_dif_frame.place_forget()

            self.crossword_game_frame.place(relx=0, relwidth=1,
                                            rely=0, relheight=1)

            self.crossword_main_title.place(relx=0.3, relwidth=0.4,
                                            rely=0.05, relheight=0.15)

            self.crossword_word_label.configure(text=f"Word:   {mixed_word}")
            self.crossword_word_label.place(relx=0.15, relwidth=0.5,
                                            rely=0.25, relheight=0.13)

            self.crossword_mean_label.configure(text=f"Mean:   {mean}")

            self.crossword_word_entry.place(relx=0.15, relwidth=0.5,
                                            rely=0.61, relheight=0.13)

            self.crossword_back_button.place(relx=0.02, relwidth=0.07,
                                             rely=0.04, relheight=0.1)

            self.set_level(level=dif_lev)

            self.crossword_score_label.place(relx=0.67, relwidth=0.31,
                                             rely=0.55, relheight=0.14)

            self.crossword_check_button.place(relx=0.15, relwidth=0.5,
                                              rely=0.79, relheight=0.16)

    def okay(self):
        self.crossword_answer_frame.place_forget()

    def back_to_crossword_dif_frame(self):
        self.crossword_game_frame.place_forget()
        self.crossword_dif_frame.place(relx=0.05, relwidth=0.9,
                                       rely=0.25, relheight=0.7)

    def change_word_mean(self, is_true_word_mean: list):
        """
        is_true_word_mean -> [True, [str, str]] or [False, str, [str, str]]
        :param is_true_word_mean:
        """
        self.crossword_word_entry.delete(0, END)
        if is_true_word_mean[0]:
            word, mean = is_true_word_mean[1]
            new_score = int(self.crossword_score_label.cget("text").split()[-1])
            new_score += 1
        else:
            new_score = int(self.crossword_score_label.cget("text").split()[-1])
            Crossword.save_get_score(new_score)

            answer, word_mean = is_true_word_mean[1:]
            word, mean = word_mean
            self.crossword_answer_label.configure(text=f"Answer: {answer}")
            self.crossword_answer_frame.place(relx=0.2, relwidth=0.3,
                                              rely=0.6, relheight=0.3)
            self.crossword_answer_label.place(relx=0.1, relwidth=0.8,
                                              rely=0.1, relheight=0.3)
            self.crossword_answer_button.place(relx=0.3, relwidth=0.4,
                                               rely=0.5, relheight=0.4)
            new_score = 0
        self.crossword_word_label.configure(text=f"Word:   {word}")
        self.crossword_mean_label.configure(text=f"Mean:   {mean}")
        self.crossword_score_label.configure(text=f"Score is {new_score}")


class Crossword:
    def __init__(self):
        with open("crossword.json", "r", encoding="utf-8") as self.file:
            self.crossword_dict = json.loads(self.file.read())
        self.random_word: str = ""
        self.mean: str = ""

    def get_size(self):
        return len(list(self.crossword_dict.keys()))

    def shuffle(self, new: bool = True):
        """
        [new = False] to shuffle existing word.\n
        [new = True] to generate new word.\n
        :returns: [mixed_word, mean] -> list(str)
        :param new:
        """
        mixed_word = ""
        if new:
            self.random_word = list(self.crossword_dict.keys())[randint(0, len(self.crossword_dict.keys()))]
            self.mean = self.crossword_dict[self.random_word]["mean"].lower()
            temp_word = [x for x in self.random_word.lower()]
        else:
            temp_word = [i for i in self.random_word.lower()]
        for _ in range(0, len(temp_word)):
            var = randint(0, len(temp_word) - 1)
            mixed_word += temp_word[var]
            temp_word.pop(var)
        try:
            self.crossword_dict.pop(self.random_word)
        except KeyError:
            pass
        return [mixed_word, self.mean]

    @staticmethod
    def save_get_score(score: int = 0, save: bool = True, get: bool = False):
        """
        "save" and "get" must be opposites to run without error.
        :param score:
        :param save:
        :param get:
        :return:
        """
        with open("crossword_score.json", "r", encoding="utf-8") as crossword_score:
            crossword_score_dict = json.loads(crossword_score.read())
        if save and not get:
            if score != 0:
                crossword_score_dict["scores"].append(score)
                with open("crossword_score.json", "w", encoding="utf-8") as writing_file:
                    json.dump(crossword_score_dict, writing_file)
        elif not save and get:
            if score == 0:
                best_score = max(crossword_score_dict["scores"])
                return f"Best score: {best_score}"

    def is_true(self, user_answer: str):
        if user_answer.lower() == self.random_word.lower():
            return [True, self.shuffle()]
        else:
            return [False, self.random_word, self.shuffle()]

    def reshuffle(self):
        return self.shuffle(new=False)[0]


class Word:
    def __init__(self):
        with open("words.json", "r", encoding="utf-8") as words:
            self.words_dict = json.loads(words.read())

    def get_word_list(self):
        return list(map(lambda x: x.lower(), self.words_dict.keys()))

    def save(self, word: str, sentence: str = "", mean: str = ""):
        word, sentence, mean = word.lower(), sentence.lower(), mean.lower()
        if word in self.words_dict.keys():
            if self.words_dict[word]["sentence"] != sentence and self.words_dict[word]["mean"] != mean:
                self.words_dict[word]["sentence"] = sentence
                self.words_dict[word]["mean"] = mean
                self.write_changes()
                return (f"The sentence and mean of {word} has been saved."
                        f" The sentence is {sentence}. The mean is {mean}")
            elif self.words_dict[word]["mean"] != mean:
                self.words_dict[word]["mean"] = mean
                self.write_changes()
                return f"The mean of {word} has been saved. The mean is {mean}"
            elif self.words_dict[word]["sentence"] != sentence:
                self.words_dict[word]["sentence"] = sentence
                self.write_changes()
                return f"The sentence of {word} has been saved. The sentence is {sentence}"
            else:
                return (f"{word} is already saved with all components."
                        f" {word}'s sentence is {sentence}, and the mean is {mean}.")
        else:
            self.words_dict[word] = {"mean": mean, "sentence": sentence}
            self.write_changes()
            return f"Has been saved."

    def write_changes(self):
        with open("words.json", "w", encoding="utf-8") as file:
            json.dump(self.words_dict, file)

    def get_attr(self, word: str | int, sentence: bool = True, mean: bool = True):
        if type(word) is str:
            word = word.lower()
            word = self.words_dict[word]
            word_sentence, word_mean = word["sentence"], word["mean"]
            if sentence and mean:
                return [word_sentence, word_mean]
            elif sentence and not mean:
                return word_sentence
            else:
                return word_mean
        else:
            _word_ = list(self.words_dict.keys())[word]
            _word_ = self.words_dict[_word_]
            word_sentence, word_mean = _word_["sentence"], _word_["mean"]
            if sentence and mean:
                return [word_sentence, word_mean]
            elif sentence and not mean:
                return word_sentence
            elif not sentence and mean:
                return word_mean
            else:
                return _word_

    def get_size(self):
        return len(list(self.words_dict.keys()))


if __name__ == "__main__":
    App()
