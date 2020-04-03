#!/usr/bin/env python
#

import sys


def minimumHours(rows, column, grid):
    minHrs = 0
    for ridx, row in enumerate(grid):
        for cidx,col in enumerate(row):
            if col == 1:
                continue
            if col == 0:
                # check nextdoor
                neighbor_flag = False
                if cidx > 0 and cidx < column:
                    if row[cidx-1] == 1 or row[cidx+1] == 1:
                        neighbor_flag == True
                if cidx == 0:
                    if row[cidx+1] == 1:
                        neighbor_flag = True
                if cidx == column:
                    if row[cidx-1] == 1:
                        neighbor_flag = True
                # check below
                above_below_flag = False
                if ridx > 0 and ridx < rows:
                    if grid[ridx+1][cidx] == 1 or grid[ridx-1][cidx] == 1:
                        above_below_flag == True
                if ridx == 0:
                    if grid[ridx+1][cidx+1] == 1:
                        above_below_flag = True
                if ridx == rows:
                    if grid[ridx-1][cidx] == 1:
                        above_below_flag = True
        if neighbor_flag == True or above_below_flag == True:
            minHrs += 1
    return minHrs

def main():

    x = [[0,1,1,0,1],[0,1,0,1,0],[0,0,0,0,1],[0,1,0,0,0]]
    print(minimumHours(4,4,x))


# ---------- run main -------------
if __name__ == "__main__":
    main()

