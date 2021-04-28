#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Wed/Apr28/2021
# This program shows how local and global variable work


# global variable:
variable_x = 25


def local_variable():
    # this shows what happen with local variables:

    variable_x = 10
    variable_y = 30
    variable_z = variable_x + variable_y
    print(
        "local variable_x, variable_y, variable_z = {0} + {1} = {2}".format(
            variable_x, variable_y, variable_z
            )
        )


def global_variable():
    # this shows what happen with global variable:

    global variable_x
    variable_x = variable_x + 1
    variable_y = 30
    variable_z = variable_x + variable_y
    print(
        "global variable_x, variable_y, variable_z = {0} + {1} = {2}".format(
            variable_x, variable_y, variable_z
            )
        )


def main():
    # this function shows how local and global variables work

    local_variable()
    global_variable()


if __name__ == "__main__":
    main()
