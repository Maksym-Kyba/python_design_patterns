from typing import Protocol

class Flyer(Protocol):
    def fly(self) -> None:
        ...

#Будь який обʼєкт який має fly тепер автоматично Flyer
