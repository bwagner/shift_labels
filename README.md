# shift_labels

Shifts [Audacity](https://www.audacityteam.org/) labels by a (possibly negative) offset.
```console
 Usage: shift_labels.py [OPTIONS] INPUT_FILENAME OFFSET

 Command-line interface that reads an Audacity label file, shifts the labels by the
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
Note: To protect a negative offset from being interpreted as an invalid option, you
need to precede it by `--`, e.g.:
```console
shift_labels.py labels.txt -- -.3 > new_labels.txt
```

## See also
[rebuildap](https://github.com/bwagner/rebuildap), [beats2bars](https://github.com/bwagner/beats2bars), [quantize_labels](https://github.com/bwagner/quantize_labels), [pyaudacity](https://github.com/bwagner/pyaudacity)

## To Do
- quantize labels to a given beat track
