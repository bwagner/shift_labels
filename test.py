# test_shift_labels.py


import pytest

from shift_labels import shift_labels


@pytest.mark.parametrize(
    "input_lines, offset, expected_output",
    [
        # single column input (start time + label)
        (
            ["1.000000\tLabel A\n", "2.500000\tLabel B\n"],
            0.5,
            ["1.500000\tLabel A\n", "3.000000\tLabel B\n"],
        ),
        # two columns (start time, end time + label)
        (
            ["1.000000\t2.000000\tLabel A\n", "3.500000\t5.000000\tLabel B\n"],
            0.5,
            ["1.500000\t2.500000\tLabel A\n", "4.000000\t5.500000\tLabel B\n"],
        ),
        # empty labels (just time values, no actual label)
        (
            ["1.000000\t2.000000\t\n", "3.500000\t4.500000\t\n"],
            0.5,
            ["1.500000\t2.500000\t\n", "4.000000\t5.000000\t\n"],
        ),
        # negative offset
        (
            ["1.000000\t3.000000\tLabel A\n", "4.500000\tLabel B\n"],
            -0.5,
            ["0.500000\t2.500000\tLabel A\n", "4.000000\tLabel B\n"],
        ),
        # one column (single time value)
        (
            ["1.000000\n", "2.500000\n"],
            0.5,
            ["1.500000\t\n", "3.000000\t\n"],
        ),
        # zero offset
        (
            ["1.000000\t3.000000\tLabel A\n", "4.500000\tLabel B\n"],
            0.0,
            ["1.000000\t3.000000\tLabel A\n", "4.500000\tLabel B\n"],
        ),
    ],
)
def test_shift_labels(input_lines, offset, expected_output):
    # Simulate input as a generator
    input_gen = (line for line in input_lines)

    # Call shift_labels and collect output
    output_gen = shift_labels(input_gen, offset)
    output_lines = list(output_gen)

    # Check if the output matches the expected output
    assert output_lines == expected_output


@pytest.mark.parametrize(
    "input_lines, offset, expected_errors",
    [
        # invalid time format (non-numeric)
        (
            ["InvalidTime\t2.000000\tLabel A\n", "3.500000\tInvalidEnd\tLabel B\n"],
            0.5,
            [
                "Error processing line: InvalidTime\t2.000000\tLabel A - could not convert string to float: 'InvalidTime'\n",
                "Error processing line: 3.500000\tInvalidEnd\tLabel B - could not convert string to float: 'InvalidEnd'\n",
            ],
        ),
        # missing time column (too few columns)
        (
            ["\tLabel A\n", "3.500000\t\tLabel B\n"],
            0.5,
            [
                "Error processing line: Label A - could not convert string to float: ''\n",
                "Error processing line: 3.500000\t\tLabel B - could not convert string to float: ''\n",
            ],
        ),
    ],
)
def test_shift_labels_invalid_input(input_lines, offset, expected_errors):
    # Simulate input as a generator
    input_gen = (line for line in input_lines)

    # Call shift_labels and collect output
    output_gen = shift_labels(input_gen, offset)
    output_lines = list(output_gen)

    # Check if the output contains expected error messages
    assert output_lines == expected_errors
