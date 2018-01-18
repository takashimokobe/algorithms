# Takahiro Shimokobe

# Implement a musical catalog with functionality similar to various media players
# Program takes in a single command line argument 
# File loads the contents of the catalog (song's title, artist, album.)

import sys
from arraylist import *

class Song:
	def __init__(self, number, title, artist, album):
		self.number = number
		self.title = title
		self.artist = artist
		self.album = album

	def __eq__(self, other):
		return ((type(other) == Song)
			and self.number = other.number
			and self.title = other.title
			self.artists = other.artist
			self.album = other.album
			)

	def __repr__(self):
		return ("Song({!r}, {!r}, {!r}, {!r})".format(self.number, self.title, self.artist, self.album))

# file -> list
# this function reads in a file and turns it into a list. 
def readFile(file):
	songlist = empty_list()
	line_num = 1
	song_num = 0
	for line in file:
		s = parse_line(line, song_num)
		if s is not None:
			songlist = add(songlist, song_num, s)
			song_num += 1
		else:
			print("line {}: malformed song information".format(line_num))
		line_num += 1

	return songlist

# line int -> format
# should pull apart the song information. Would return the song info into a format you can store into a list.
def parse_line(line, song_num):
	l = line.split("--")
	if len(l) != 3:
		s = None
	else:
		s = Song(song_number, l[0], l[1], l[2])
	return s

# no arguments -> prompt
# this function prints out the Menu, and returns an prompt of type int
def Menu():
    prompt = input("Song Catalog\n    1) Print Catalog\n    2) Song Information\n    3) Sort\n    4) Add Songs\n    0) Quit\nEnter Selection: ")
    while (int(prompt) < 0 or int(prompt) > 4):
        print ("Invalid option.\n")
        prompt = input("Song Catalog\n    1) Print Catalog\n    2) Song Information\n    3) Sort\n    4) Add Songs\n    0) Quit\nEnter Selection: ")
    return int(prompt)

# song -> void
# prints out the information of a song
def printSong(song):
    print(str(song.number) + '--' + song.title + '--' + song.artist + '--' + song.album)

# Each song is assigned a number as it is added to the list. Adds to the beginning of the file.
# all songs are printed out with numbers assigned
def printCatalog(songlist):
    foreach(songlist, printSong)

# prompts the user for a song number. Then prints the attributes of said song. Invalid song number prints out 'Invalid song number'
def songInformation(songlist):
    songnum = int(input("Enter song number: "))
    while (songnum < 0 or songnum > length(songlist)):
        print ("Invalid song number\n")
        songnum = int(input("Enter song number: "))
    song = get(songlist, songnum)
    print("Song information...\n    Number: " + (str(
        song.number)) + "\n    " + "Song Title: " + song.title + "\n    " + "Artist: " + song.artist + "\n    " + "Album: " + song.album)

# songlist -> List
# this function prompts the user for a sort method. Based on the sort method, will then sort the list. 
def sortPrompt(songlist):
    prompt = input("Sort songs\n    0) By Number\n    1) By Title\n    2) By Artist\n    3) By Album\nSort by: ")
    while int(prompt) < 0 or int(prompt) > 3:
        print ("...Invalid sort option\n")
        prompt = input("Sort songs\n    0) By Number\n    1) By Title\n    2) By Artist\n    3) By Album\nSort by: ")
    if prompt == 0:
        return sort(songlist, lessthan_Num())
    elif prompt == 1:
        return sort(songlist, lessthan_Title())
    elif prompt == 2:
        return sort(songlist, lessthan_Art())
    elif prompt == 3:
        return sort(songlist, lessthan_Album())

# song song -> boolean
# comparator for song number
def lessthan_Num(song1, song2):
    return (song1.number < song2.number)

# song song -> boolean
# comparator for song title
def lessthan_Title(song1, song2):
    return (song1.title < song2.title)

# song song -> boolean
# comparator for song artist
def lessthan_Art(song1, song2):
    return (song1.artist < song2.artist)

#song song -> boolean
# comparator for song album
def lessthan_Album(song1, song2):
    return (song2.album < song2.album)

# add songs adds songs from a file to your Catalog
def addSongs():
    prompt = input("Enter name of file to load: ")

# start of my main code.
if (__name__ == '__main__'):
    if (len(sys.argv) > 1):
        file = open(str(sys.argv[1]), "r")
        songlist = readFile(file)
    quit = False
    while not quit:
        prompt = Menu()
        if prompt == 0:
            quit = True
        elif prompt == 1:
            printCatalog(songlist)
        elif prompt == 2:
            songInformation(songlist)
        elif prompt == 3:
            sortPrompt(songlist)
        elif prompt == 4:
            addSongs()