"""Test pytest_unittest_id_runner"""

from pytest_unittest_id_runner import convert_unittest_id_to_pytest


def test_convert_unittest_id_to_pytest():
    """Test id conversion"""
    assert (
        convert_unittest_id_to_pytest("path.to.TestClass.test_method")
        == "path/to.py::TestClass::test_method"
    )
    assert convert_unittest_id_to_pytest("path.to") == "path.to"


def test_unittest_id(pytester):
    """Simple end-to-end test"""
    # Create a temporary test file
    pytester.makepyfile("""
        import unittest
        class TestExample(unittest.TestCase):
            def test_one(self):
                assert True
            def test_two(self):
                assert True
    """)

    # Run pytest with the plugin option
    result = pytester.runpytest("test_unittest_id.TestExample.test_one")

    # Check that only one test ran
    result.assert_outcomes(passed=1)


def test_pytest_id(pytester):
    """Simple end-to-end test"""
    # Create a temporary test file
    pytester.makepyfile("""
        import unittest
        class TestExample(unittest.TestCase):
            def test_one(self):
                assert True
            def test_two(self):
                assert True
    """)

    # Run pytest with the plugin option
    result = pytester.runpytest("test_pytest_id.py::TestExample::test_one")

    # Check that only one test ran
    result.assert_outcomes(passed=1)


def test_multiple_unittest_ids(pytester):
    """End-to-end test with two selections"""
    pytester.makepyfile("""
        import unittest
        class TestExample(unittest.TestCase):
            def test_one(self):
                assert True
            def test_two(self):
                assert True
            def test_three(self):
                assert True
    """)

    result = pytester.runpytest(
        "test_multiple_unittest_ids.TestExample.test_one",
        "test_multiple_unittest_ids.TestExample.test_two",
    )

    result.assert_outcomes(passed=2)


def test_nonexistent_unittest_id(pytester):
    """Test that missing ID's are just ignored"""
    pytester.makepyfile("""
        import unittest
        class TestExample(unittest.TestCase):
            def test_one(self):
                assert True
    """)

    result = pytester.runpytest(
        "test_nonexistent_unittest_id.TestExample.nonexistent_test"
    )

    result.assert_outcomes(passed=0, failed=0, errors=0)
