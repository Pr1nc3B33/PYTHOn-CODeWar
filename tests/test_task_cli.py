import pytest

from task_cli import (
    add_task,
    delete_task,
    display_main_menu,
    get_valid_menu_choice,
    run_task_manager,
    view_tasks,
)


def set_inputs(monkeypatch, values):
    """Mock sequential input() calls."""
    it = iter(values)
    monkeypatch.setattr("builtins.input", lambda _="": next(it))


def test_display_menu(capsys):
    display_main_menu()
    out = capsys.readouterr().out
    assert "1) Add task" in out
    assert "4) Quit" in out


@pytest.mark.parametrize("raw, expected", [("1", 1), ("2", 2), ("3", 3), ("4", 4)])
def test_valid_menu_choice(monkeypatch, raw, expected):
    set_inputs(monkeypatch, [raw])
    assert get_valid_menu_choice() == expected


@pytest.mark.parametrize("raw", ["", "abc", "0", "5", "-1"])
def test_invalid_menu_choice(monkeypatch, capsys, raw):
    set_inputs(monkeypatch, [raw])
    assert get_valid_menu_choice() is None
    assert "Invalid menu option" in capsys.readouterr().out


def test_add_task_success(monkeypatch):
    tasks = []
    set_inputs(monkeypatch, ["Buy milk"])
    add_task(tasks)
    assert tasks == ["Buy milk"]


@pytest.mark.parametrize("raw", ["", "   "])
def test_add_task_empty(monkeypatch, capsys, raw):
    tasks = []
    set_inputs(monkeypatch, [raw])
    add_task(tasks)
    assert tasks == []
    assert "Task cannot be empty" in capsys.readouterr().out


def test_view_tasks_empty(capsys):
    view_tasks([])
    assert "There are no tasks to view" in capsys.readouterr().out


def test_delete_task_empty(capsys):
    tasks = []
    delete_task(tasks)
    assert "There are no tasks to delete" in capsys.readouterr().out


def test_delete_task_invalid_index(monkeypatch, capsys):
    tasks = ["A"]
    set_inputs(monkeypatch, ["2"])
    delete_task(tasks)
    assert tasks == ["A"]
    assert "That task does not exist" in capsys.readouterr().out


def test_delete_task_invalid_number(monkeypatch, capsys):
    tasks = ["A"]
    set_inputs(monkeypatch, ["abc"])
    delete_task(tasks)
    assert tasks == ["A"]
    assert "Please enter a valid number" in capsys.readouterr().out


def test_delete_task_success(monkeypatch):
    tasks = ["A", "B"]
    set_inputs(monkeypatch, ["2"])
    delete_task(tasks)
    assert tasks == ["A"]


def test_full_flow_add_view_delete_quit(monkeypatch, capsys):
    set_inputs(monkeypatch, ["1", "Task X", "2", "3", "1", "4"])
    run_task_manager()
    out = capsys.readouterr().out
    assert 'Added: "Task X"' in out
    assert "1. Task X" in out
    assert 'Deleted: "Task X"' in out
    assert "Goodbye!" in out