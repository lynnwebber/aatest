#!/usr/bin/env python
#

import sys

def numberAmazonTreasureTrucks(rows, column, grid):
    ttpopup_count = 0
    for row in grid:
        for idx,col in enumerate(row):
            if idx > 0 and idx < column-1:
                if row[idx+1] == 1:
                    ttpopup_count -= 1
            if col == 1:
                ttpopup_count += 1
                if idx > 0 and idx < column:
                    if row[idx-1] == 1:
                        ttpopup_count -= 1
            if idx == 0:
                continue
            if idx == column:
                continue
    return ttpopup_count


def main():

    x = [[1,1,0,0],[0,0,0,0],[0,0,1,1],[0,0,0,0]]
    print(numberAmazonTreasureTrucks(4,4,x))


# ---------- run main -------------
if __name__ == "__main__":
    main()

