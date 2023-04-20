from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """
        Documentation content.
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """
        Documentation content again.
        """
        yield from iter(self.answer)