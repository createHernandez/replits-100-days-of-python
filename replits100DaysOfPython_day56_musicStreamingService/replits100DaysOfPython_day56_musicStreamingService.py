import os # open()
import csv #DictReader() 

os.system("cls")

print("Building...\n")

with open("replits100DaysOfPython_day56_musicStreamingService/100MostStreamedSongs.csv") as file: 
    reader = csv.DictReader(file)

    # declare an array for the list of artists processed 
    artists_folders = []
    song_files = []

    for row in reader: 
        dir_name = os.path.join("replits100DaysOfPython_day56_musicStreamingService", str(row["Artist(s)"]))
        
        if row["Artist(s)"] not in artists_folders: 
            print(f"Adding... {row['Artist(s)']},", end=" ")

            # make a folder for the artist 
            os.mkdir(dir_name)

            if row["Song"] not in song_files: 
                # make a file for each song 
                print(f"{row['Song']}")

                file_name = os.path.join(dir_name, str(row["Song"]))

                f = open(file_name, "w")
                f.close() 

print()