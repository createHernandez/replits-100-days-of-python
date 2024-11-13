import os # system() 

os.system("cls") 

print("HIGH SCORE TABLE\n")

f = open("replits100DaysOfPython_day49_readingAfile/high.score", "r")

top_score = 0 
top_scorer = ""

while True: 
    content = f.readline().strip()
    if content == "": 
        break
    
    content_list = content.split() 
    
    initials = content_list[0]
    score = int(content_list[1])

    if score > top_score: 
        top_score = score 
        top_scorer = initials

print(f"{top_scorer} has the highest score with {top_score}\n")

f.close() 