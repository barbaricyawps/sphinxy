from sphinxy.riddle import Riddle


class IncorrectAnswer(Exception):
    ...


class Sphinx:
    def __init__(self, name: str):
        """
        Args:
           This is for the initial class.
        
        Raises:
           This is what the initial class raises.
        
        Returns:
            I don't really know what the init returns,
        """
        self._name = name
        self._riddle = Riddle(
            question=(
                "What goes on four legs in the morning, two legs at noon, "
                "and three legs in the evening?"
            ),
            answer="man",
        )

    def introduce(self) -> str:
        """
        Args:
           Yes.

        Raises:
           Eventually I should put real data here,
        
        Returns:
           And so forth.
        """
        return (
            f"Greetings, mortals. I am {self._name}. I have guarded the city of Thebes"
            "for centuries and posed riddles to those who dared to approach me."
        )

    def update_riddle(self, riddle: Riddle) -> str:
        """
        Args:
            I really need to learn more about documeting APIs.

        Raises:
            No really I should.

        Returns:
            Something, I guess.
        """
        self._riddle = riddle
        return "I have updated my riddle. Are you ready to solve it?"

    def pose_riddle(self, include_hint: bool = False) -> tuple[str, str | None]:
        """
        Args:
            answer (str): The given answer to the riddle.

        Raises:
            I'm just making this up.

        Returns:
            I'm also making this up too!
        """
        hint = (
            f"Hint: The answer starts with the letter '{self._riddle.get_hint()}'."
            if include_hint
            else None
        )
        return (self._riddle.question, hint)

    def check_riddle_answer(self, answer: str, return_hint: bool = False) -> str:
        """
        Args:
            answer (str): The given answer to the riddle.
            return_hint (bool, optional): Controls whether a hint for the riddle should
                be returned. Defaults to False.

        Raises:
            IncorrectAnswer: Exception for incorrect answer.

        Returns:
            str: The result of the evaluation of the answer.
        """
        if self._riddle.check_answer(answer):
            return "Your answer was correct. You may pass."
        elif return_hint:
            return (
                "Your answer was wrong. Hint: The answer starts with the letter "
                f"'{self._riddle.get_hint()}'."
            )
        else:
            raise IncorrectAnswer("Your answer was wrong. You shall not pass.")