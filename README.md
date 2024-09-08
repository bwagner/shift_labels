# shift_labels

Shifts [Audacity](https://www.audacityteam.org/) labels by a (possibly negative) offset.
```
 Usage: shift_labels.py [OPTIONS] INPUT_FILENAME OFFSET

 Command-line interface that reads an input file, shifts the labels by the
 given offset, and prints the result to standard output.

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    input_filename      TEXT   File containing audacity labels or a column  │
│                                 of numbers                                   │
│                                 [default: None]                              │
│                                 [required]                                   │
│ *    offset              FLOAT  Offset by which to shift the labels          │
│                                 [default: None]                              │
│                                 [required]                                   │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯
```
Example invocation (I want to shift labels by .3 seconds)
```console
shift_labels.py labels.txt .3 > new_labels.txt
```
Note: to protect a negative offset to be interpreted as an invalid option, you
need to protect that argument by a preceding `--`:
```console
shift_labels.py labels.txt -- -.3 > new_labels.txt
```
