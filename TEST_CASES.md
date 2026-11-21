# Manual test cases

| Test | Input | Expected result |
|---|---|---|
| Normal input | Name `Asha`; marks `80 90 70` | Average 80.00; grade B |
| Minimum boundary | Marks `0 0` | Average 0.00; grade F |
| Maximum boundary | Marks `100 100` | Average 100.00; grade A |
| Out-of-range mark | Marks `105 80` | Validation error |
| Non-numeric mark | Marks `abc 80` | Input error |
| No marks | Empty marks input | At least one mark is required |
| Empty name | Empty name | Name validation message |

These are test cases to execute; do not report them as executed until you run them.
