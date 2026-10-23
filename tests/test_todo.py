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

    def test_remove_from_empty_list(self):
        todos = TodoList()
        self.assertIs(todos.remove("x"), False)
        self.assertEqual(todos.count(), 0)
        self.assertEqual(todos.list_all(), [])

    def test_remove_matching_item(self):
        todos = TodoList()
        todos.add("a")
        remaining = todos.add("b")
        self.assertIs(todos.remove("a"), True)
        self.assertEqual(todos.count(), 1)
        self.assertEqual(todos.list_all(), [remaining])

    def test_remove_missing_item_leaves_list_unchanged(self):
        todos = TodoList()
        todos.add("a")
        todos.add("b")
        before = todos.list_all()
        self.assertIs(todos.remove("x"), False)
        self.assertEqual(todos.list_all(), before)
        self.assertEqual(todos.count(), 2)

    def test_remove_ignores_surrounding_whitespace(self):
        todos = TodoList()
        todos.add("  Hello  ")
        self.assertIs(todos.remove(" \tHello\n"), True)
        self.assertEqual(todos.list_all(), [])
        self.assertEqual(todos.count(), 0)

    def test_remove_deletes_only_first_match(self):
        todos = TodoList()
        todos.add("a")
        middle = todos.add("b")
        second_match = todos.add("a")
        self.assertIs(todos.remove("a"), True)
        remaining = todos.list_all()
        self.assertEqual(remaining, [middle, second_match])
        self.assertIs(remaining[1], second_match)
        self.assertEqual(todos.count(), 2)


if __name__ == "__main__":
    unittest.main()
