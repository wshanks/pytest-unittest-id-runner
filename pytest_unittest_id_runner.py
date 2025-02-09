"""pytest plugin to convert unittest-style test id's to pytest style"""

from pathlib import Path

from pytest import hookimpl


def convert_unittest_id_to_pytest(test_id: str) -> str:
    """Convert unittest id to pytest node identifier

    Args:
        test_id: A test specification from the pytest commandline

    Returns:
        If ``test_id`` was a unittest-style test identifier, the pytest
        identifier is returned. Otherwise, the input ``test_id`` is returned.
    """

    # unittest format will not include :: or be a valid path in the first part
    path, _, _ = test_id.partition("::")
    if Path(path).exists():
        return test_id

    # A unittest identifier needs at least 3 parts (path, class, method)
    parts = test_id.split(".")
    if len(parts) < 3:
        return test_id

    file_path = "/".join(parts[:-2]) + ".py"
    class_name = parts[-2]
    method_name = parts[-1]
    pytest_id = f"{file_path}::{class_name}::{method_name}"
    return pytest_id


@hookimpl
def pytest_collection(session):
    """Override pytest collection to replace unittest-style test identifiers"""
    for idx, arg in enumerate(session.config.args):
        session.config.args[idx] = convert_unittest_id_to_pytest(arg)
