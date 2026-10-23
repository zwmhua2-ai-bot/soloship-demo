"""Tiny todo module used by the SoloShip P03 test repository."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Todo:
    title: str


class TodoList:
    def __init__(self) -> None:
        self._items: list[Todo] = []

    def add(self, title: str) -> Todo:
        if not title.strip():
            raise ValueError("title cannot be empty")
        todo = Todo(title=title.strip())
        self._items.append(todo)
        return todo

    def remove(self, title: str) -> bool:
        title = title.strip()
        for index, todo in enumerate(self._items):
            if todo.title.strip() == title:
                del self._items[index]
                return True
        return False

    def list_all(self) -> list[Todo]:
        return list(self._items)

    def count(self) -> int:
        return len(self._items)
