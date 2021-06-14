from bot import *

# will this work with tests not having an ID?

def test_add_2020():
    pass
    # add valid character
    # add same character (same name, same stats) again (should overwrite)
    # add same character (same name, different stats) again (should overwrite)
    # add character with same stats, different name (should not be considered duplicate)
    # add character with a bad number of parameters
    # add character with negative stat values (shouldn't work)
    # add character with values above 10 (should work)


def test_print_2020():
    pass
    # db should contain two valid characters at this point with this user
    # pull both of them and print them
    # try to print a character that doesn't exist
    # try to print a character that user tried to add, but failed

def test_del_2020():
    pass
    # delete both characters from db
    # delete them again (should fail)
    # delete characters that don't exist (should fail)


def test_add_red():
    pass
    # see test_add_2020 for comments


def test_print_red():
    pass
    # see test_print_2020 for comments


def test_del_red():
    pass
    # see test_del_2020 for comments

