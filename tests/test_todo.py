import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from todo import TodoList


class TodoListTests(unittest.TestCase):
    def test_add_and_list(self):
        todos = TodoList()
        todo = todos.add("  Hello  ")
        self.assertEqual(todo.title, "Hello")
        self.assertEqual([item.title for item in todos.list_all()], ["Hello"])

    def test_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            TodoList().add("   ")

    def test_count(self):
        todos = TodoList()
        self.assertEqual(todos.count(), 0)
        todos.add("a")
        todos.add("b")
        self.assertEqual(todos.count(), 2)


if __name__ == "__main__":
    unittest.main()
