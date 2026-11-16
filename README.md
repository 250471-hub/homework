# Task Manager

A small Python command-line program for adding and listing tasks. Tasks are stored
in memory and disappear when the program exits. This is an **example project**
created for the Unit 3 exercise because the previous-course project was not in
the repository; it is not a copy of that project.

## Requirements and running

Python 3 is required; there are no external dependencies.

```sh
python task_manager.py
```

Choose `1` to add a task, `2` to list tasks, or `3` to quit. Empty or
whitespace-only descriptions are rejected, and surrounding whitespace is
removed from valid descriptions. You can try again after an invalid entry.

## Tests

```sh
python -m unittest discover -s tests -v
```

## Unit 3 exercise

- Improvement and acceptance checks: [Issue #1](../../issues/1).
- Baseline on `main`: `934c24d87e540fb3e305e26f84e97bcca89dbeae`.
- The issue documents the reason for the validation approach. The feature
  branch contains separate commits for the example, the improvement, and tests.
- The student still needs to arrange a partner review, complete the conflict
  practice, merge after approval, and create the `v0.1.0` release on the merged
  `main` commit. Do not claim these steps are done without completing them.

## Unit 4: Booking bug activity

Run `python booking.py` to see the corrected booking boundary, and run
`python test_booking.py` for the supplied checks. The reproduction, bug report,
hypotheses, fix, and reflection are documented in `unit4_activity_answers.md`.
