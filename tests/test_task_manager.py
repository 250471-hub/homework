import subprocess
import sys
import unittest
from pathlib import Path

from task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_valid_description_is_trimmed_and_added(self):
        self.manager.add_task("  Study Python  ")
        self.assertEqual(self.manager.tasks, ["Study Python"])

    def test_blank_descriptions_are_rejected_without_adding(self):
        for description in ("", "   ", "\t\n"):
            with self.subTest(description=description):
                with self.assertRaisesRegex(ValueError, "cannot be empty"):
                    self.manager.add_task(description)
        self.assertEqual(self.manager.tasks, [])

    def test_invalid_input_does_not_stop_cli(self):
        script = Path(__file__).resolve().parents[1] / "task_manager.py"
        result = subprocess.run(
            [sys.executable, str(script)],
            input="1\n   \n1\n  Study Python  \n2\n3\n",
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("Task description cannot be empty.", result.stdout)
        self.assertIn("1. Study Python", result.stdout)
        self.assertIn("Goodbye!", result.stdout)

    def test_cli_exits_cleanly_on_end_of_input(self):
        script = Path(__file__).resolve().parents[1] / "task_manager.py"
        result = subprocess.run(
            [sys.executable, str(script)], input="", text=True, capture_output=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("Goodbye!", result.stdout)


if __name__ == "__main__":
    unittest.main()
