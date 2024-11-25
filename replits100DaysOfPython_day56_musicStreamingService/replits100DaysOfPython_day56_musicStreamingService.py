import os # open()
import csv #DictReader() 

os.system("cls")

print("Building...\n")

with open("replits100DaysOfPython_day56_musicStreamingService/100MostStreamedSongs.csv") as file: 
    reader = csv.DictReader(file)

    for row in reader: 
        # declare an array for the list of artists processed 
        artists_folders = os.listdir() 

        artist_name = row["Artist(s)"].strip().lower().title()

        dir_name = os.path.join("replits100DaysOfPython_day56_musicStreamingService", artist_name)
        
        if artist_name not in artists_folders: 
            print(f"Adding... {artist_name},", end=" ")

            # make a folder for the artist 
            os.mkdir(dir_name)

            song_name = row["Song"].strip().lower().title()

            # make a file for each song 
            print(f"{song_name}")

            file_name = os.path.join(dir_name, song_name)

            f = open(file_name, "w")
            f.close() 

print()