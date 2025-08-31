| Run           | 500MBfile.txt (Unique Words) | 500MBfile.txt (Time, s) | 1GBfile.txt (Unique Words) | 1GBfile.txt (Time, s) | 2GBfile.txt (Unique Words) | 2GBfile.txt (Time, s) |
|---------------|------------------------------|-------------------------|---------------------------|-----------------------|---------------------------|-----------------------|
| Single Thread  | 234451                    | 6.13                    | 234451                 | 15.30                 | 234451                 | 46.64                 |
| Spark Compute | 234451                    | 5.49                    | 234451                 | 8.10                  | 234451                 | 16.30                 |

*All word counts are for unique words. Times are in seconds. Averages are calculated over 6 runs.*


