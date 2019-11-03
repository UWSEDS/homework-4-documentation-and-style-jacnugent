"""
Module to runs tests on a DataFrame for Homework 3.

Author: Jacqueline Nugent
Modified: November 3, 2019

Functions:
test_correct_type: check for the same type in the given dataframe columns
test_nan: check for nan values in the given dataframe
test_rows: check that the given dataframe has at least one row
test_dataframe: run test_correct_type, test_nan, and test_rows at once.
"""

def test_correct_type(dataframe):
    """
    Check that all columns in the DataFrame have the correct type,
    i.e. the values in each column all have the same python type.

    Args:
        dataframe (DataFrame): the DataFrame to test.

    Returns:
        True if all the columns in dataframe have the correct type.
    """
    print "Testing for correct type..."
    correct_type = True

    for col in dataframe.columns:
        # if the type of a column is "object," check if each entry
        # has the same data type as the previous
        if dataframe[col].dtype == 'O':
            for i in range(1, len(dataframe[col])):
                if isinstance(dataframe[col][i], type(dataframe[col][i-1])):
                    correct_type = False
                    break

    if correct_type:
        print "TEST PASSED: All of the DataFrame columns have the correct type.\n"
    else:
        print "TEST FAILED: The DataFrame columns do not have the correct type.\n"

    return correct_type


def test_nan(dataframe):
    """
    Check if the DataFrame has any nan values.

    Args:
        dataframe (DataFrame): the DataFrame to test.

    Returns:
        True if there are any nan values in dataframe.
    """
    print "Testing for nan values..."
    has_nan = dataframe.isnull().values.any()

    if not has_nan:
        print "TEST PASSED: The DataFrame has no nan values.\n"
    else:
        print "TEST FAILED: The DataFrame contains nan values.\n"

    return True


def test_rows(dataframe):
    """
    Verify that the dataframe has at least one row.

    Args:
        dataframe (DataFrame): the DataFrame to test.

    Returns:
        True if dataframe contains at least one row.
    """
    print "Testing for rows..."

    has_rows = dataframe.shape[0] >= 1

    if has_rows:
        print "TEST PASSED: The DataFrame has at least one row.\n"
    else:
        print "TEST FAILED: The DataFrame does not have at least one row.\n"

    return has_rows


def test_dataframe(dataframe):
    """
    Function to run all three tests in the module at once.
    Tests that the DataFrame has columns with the correct type, no nan values, and at least one row.

    Args:
        dataframe (DataFrame): the DataFrame to test.

    Returns:
        True if dataframe passes all three tests.
    """
    correct_type = test_correct_type(dataframe)
    has_nan = test_nan(dataframe)
    has_rows = test_rows(dataframe)

    passed = correct_type and not has_nan and has_rows

    return passed
