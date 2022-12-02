win = "WIN"
draw = "DRAW"
lose = "LOSE"

rock = "ROCK"
paper = "PAPER"
scissors = "SCISSORS"

outcome_scores = {win: 6, draw: 3, lose: 0}
play_shape_scores = {rock: 1, paper: 2, scissors: 3}

play_shape_dictionary = {
    "A": rock,
    "B": paper,
    "C": scissors,
    "X": rock,
    "Y": paper,
    "Z": scissors
}

expected_outcomes = {
    "Y": draw,
    "X": lose,
    "Z": win
}


class Rule:
    def __init__(self, play: str, beats: str, looses_to:str):
        self.play = play
        self.beats = beats
        self.looses_to = looses_to

    def outcome_with_opponent_play(self, opponent_play):
        if self.play == opponent_play:
            return draw
        elif self.beats == opponent_play:
            return win
        else:
            return lose

    def outcome_shape(self, play_expected_outcome):
        if draw == play_expected_outcome:
            return self.play
        elif lose == play_expected_outcome:
            return self.beats
        else:
            return self.looses_to


rules = {rock: Rule(rock, scissors, paper),
         scissors: Rule(scissors, paper, rock),
         paper: Rule(paper, rock, scissors)}


def calculate_based_on_play_shape(plays_line: str):
    plays = plays_line.split(" ")
    opponent_play = play_shape_dictionary.get(plays[0])
    your_play = play_shape_dictionary.get(plays[1])
    outcome = rules.get(your_play).outcome_with_opponent_play(opponent_play)
    return play_shape_scores.get(your_play) + outcome_scores.get(outcome)


def calculate_based_on_outcome(plays_line: str):
    plays = plays_line.split(" ")
    opponent_play = play_shape_dictionary.get(plays[0])
    expected_outcome = expected_outcomes.get(plays[1])
    your_play = rules.get(opponent_play).outcome_shape(expected_outcome)
    return play_shape_scores.get(your_play) + outcome_scores.get(expected_outcome)


def calculate_total(plays_strategy: str):
    return sum(map(lambda play_round: calculate_based_on_play_shape(play_round), list(plays_strategy.splitlines())))


def calculate_total_2(plays_strategy: str):
    return sum(map(lambda play_round: calculate_based_on_outcome(play_round), list(plays_strategy.splitlines())))


def use_input():
    with open("test_input_data.txt", "r") as input_file:
        input_data = input_file.read()
        total_score = calculate_total(input_data)
        print("Answer 1.", total_score)
        print("Answer 2.", calculate_total_2(input_data))


use_input()