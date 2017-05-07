import datetime
import random
import os
import re


def add_new_album(music):
    """Adds information about album given by a user to the list 'music'."""
    artist = input("Enter artist: ").strip()
    album = input("Enter title of album: ").strip()
    year = input("Enter year of release: ").strip()
    genre = input("Enter genre of album: ").strip()
    length = input("Enter length of album: ").strip()

    # Checks if format of variables 'year' and 'length' are proper.
    if not check_year_format(year):
        year = -1
    if not check_length_format(length):
        length = ""

    name = artist, album
    information = int(year), genre, length
    music.append((name, information))


def find_albums_by_artist(music):
    """Searches for albums in the list 'music' by given artist."""
    artist = input("Enter artist: ").strip()
    for name, information in music:
        if artist.lower() == name[0].lower():
            print("\"{}\" {}".format(name[1], name[0]))


def find_albums_by_year(music):
    """Searches for albums in the list 'music' by given year."""
    year = input("Enter year of release: ").strip()
    if check_year_format(year):
        for name, information in music:
            if int(year) == information[0]:
                print("\"{}\" {}".format(name[1], name[0]))


def find_artist_by_album(music):
    """Searches for artist in the list 'music' by given album."""
    search_album = input("Enter title of album: ").strip()
    for name, information in music:
        if search_album.lower() == name[1].lower():
            print("\"{}\" {}".format(name[1], name[0]))


def find_albums_by_letters(music):
    """Searches for title of albums in the list 'music'
    which includes given letter(s)."""
    letters = input("Enter letter(s): ").strip()
    for name, information in music:
        if letters.lower() in name[1].lower():
            print("\"{}\" {}".format(name[1], name[0]))


def find_albums_by_genre(music):
    """Searches for albums in the list 'music' by given genre."""
    genre = input("Enter genre: ").strip()
    for name, information in music:
        if genre.lower() == information[1].lower():
            print("\"{}\" {}".format(name[1], name[0]))


def calculate_age_of_albums(music):
    """Calculate age of each album in the list 'music'."""
    today = datetime.date.today()
    for name, information in music:
        if information[0] == -1:
            print("\"{}\" {} - wrong year".format(name[1], name[0]))
        else:
            print("\"{}\" {} - {} years old".format(name[1], name[0],
                                                    today.year-information[0]))


def choose_random_album_by_genre(music):
    """Chooses random album from the list 'found_albums'
    which contains albums from the list 'music' by given genre"""
    found_albums = []
    genre = input("Enter genre: ").strip()
    for name, information in music:
        if genre.lower() == information[1].lower():
            found_albums.append((name, information))
    if len(found_albums) > 0:
        name, information = random.choice(found_albums)
        print("\"{}\" {}".format(name[1], name[0]))


def show_amount_of_albums_by_artist(music):
    """Shows amount of albums by an artist."""
    artists_with_amount = {}
    for name, information in music:
        artist = name[0]
        if artist in artists_with_amount:
            artists_with_amount[artist] += 1
        else:
            artists_with_amount[artist] = 1
    for artist in artists_with_amount:
        print("{} - {} album(s)".format(artist, artists_with_amount[artist]))


def find_longest_album(music):
    """Searches for the longest album in the list 'music'."""
    index = 0
    max_index = 0
    max_length = ""
    for name, information in music:
        if max_length < information[2]:
            max_length = information[2]
            max_index = index
        index += 1
    name, information = music[max_index]
    print("\"{}\" {} {}".format(name[1], name[0], information[2]))


def list_all_albums(music):
    """Shows all albums from the list 'music'."""
    for name, information in music:
        if information[0] == -1:
            year = ""
        else:
            year = information[0]
        album = "\"{}\"".format(name[1])
        print("{:20} {:35} {:4} {:20} {:6}".format(name[0], album,
                                                   year,
                                                   information[1],
                                                   information[2]))


def sort_list(given_list):
    """Sort 'given list' in bubble way."""
    sort = False
    while not sort:
        sort = True
        index = 0
        while index < len(given_list) - 1:
            if given_list[index] > given_list[index+1]:
                item = given_list[index]
                given_list[index] = given_list[index+1]
                given_list[index+1] = item
                sort = False
            index += 1


def check_file(file_name):
    """Checks if the 'file_name' file exists and is non empty."""
    if not os.path.isfile(file_name):
        print("Where is '{}' file?".format(file_name))
        exit()

    if os.stat(file_name).st_size == 0:
        print("'{}' file is empty.".format(file_name))
        exit()


def action_service():
    """Checks if 'action' given by a user is valid."""
    while True:
        action = input("")
        if re.match("[0-9]$|1[0-2]$", action):
            break
        print("Enter a valid number!")
    return action


def check_year_format(year):
    "Checks if given year is in proper format."
    if re.match("19[0-9]{2}$|20[0-9]{2}$", year):
        return True
    else:
        return False


def check_length_format(length):
    "Checks if given length is in proper format."
    if re.match("[1-9][0-9]*:[0-5][0-9]$", length):
        return True
    else:
        return False


def read_file_to_music_list(file_name, music):
    """Reads a 'file_name' file and fill the list 'music' with data."""
    music_file = open(file_name, "r")

    for line in music_file.readlines():
        split_line = line[:-1].split("|")

        if len(split_line) == 5:
            for index in range(5):
                split_line[index] = split_line[index].strip()
            if not check_year_format(split_line[2]):
                split_line[2] = -1
            if not check_length_format(split_line[4]):
                split_line[4] = ""
            name = split_line[0], split_line[1]
            information = int(split_line[2]), split_line[3], split_line[4]
            music.append((name, information))
    music_file.close()


def write_music_list_to_file(file_name, music):
    """Write data from the list 'music' to the 'file_name' file."""
    music_file = open(file_name, "w")
    for name, information in music:
        year = ""
        if information[0] != -1:
            year = information[0]
        music_file.write("{} | {} | {} | {} | {}\n".format(name[0],
                                                           name[1],
                                                           year,
                                                           information[1],
                                                           information[2]))
    music_file.close()


def show_menu():
    MENU = """Choose the action:
    1) Add new album
    2) Find albums by artist
    3) Find albums by year
    4) Find musician by album
    5) Find albums by letter(s)
    6) Find albums by genre
    7) Calculate the age of all albums
    8) Choose a random album by genre
    9) Show the amount of albums by an artist
   10) Find the longest-time album
    0) Exit\n"""
    print(MENU)


def main():
    """Checks which action user choose and runs proper function."""
    FILE_NAME = "music.csv"
    music = []

    check_file(FILE_NAME)
    read_file_to_music_list(FILE_NAME, music)

    os.system("clear")
    print("\nWelcome in the CoolMusic!\n")

    while True:
        show_menu()

        action = action_service()

        os.system("clear")

        if action == "0":
            write_music_list_to_file(FILE_NAME, music)
            os.system("clear")
            exit()

        elif action == "1":
            add_new_album(music)

        elif action == "2":
            find_albums_by_artist(music)

        elif action == "3":
            find_albums_by_year(music)

        elif action == "4":
            find_artist_by_album(music)

        elif action == "5":
            find_albums_by_letters(music)

        elif action == "6":
            find_albums_by_genre(music)

        elif action == "7":
            calculate_age_of_albums(music)

        elif action == "8":
            choose_random_album_by_genre(music)

        elif action == "9":
            show_amount_of_albums_by_artist(music)

        elif action == "10":
            find_longest_album(music)

        elif action == "11":
            list_all_albums(music)

        elif action == "12":
            sort_list(music)

        input("\nPress return to enter menu.\n")
        os.system("clear")


if __name__ == "__main__":
    main()
