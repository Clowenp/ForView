"""
videos.py - reads from and writes to JSON file of information on user's videos for later use
(Alex Chen)
"""
# Import modules
import json
import os
from questions import readFile, writeFile

# Custom exception for the case where reading a QID from videos.json yields no info
class QIDNotFoundError(Exception):
    pass

def binVideoSearch(database, firstIndex, lastIndex, qID):
    """
    Binary search algorithm used for searching through userHistory.json for 
    """
    qID = int(qID)

    if firstIndex <= lastIndex:
        midIndex = (lastIndex + firstIndex) // 2
        check = int(database[midIndex]["ID"])

        if check == qID:
            return midIndex
            # return database[midIndex]          # An alternative; see how JSON dicts are parsed in Javascript
        elif check > qID:
            return binVideoSearch(database, firstIndex, midIndex - 1, qID)
        else:
            return binVideoSearch(database, midIndex + 1, lastIndex, qID)
    else:
        print("Debug: question ID not found in videos.json; try again with another question ID.")
        raise QIDNotFoundError


def readVideo(qID: int):
    """
    Reads either a random question from a JSON file of questions, or if qID is given, then returns a specific question from 
    the database.
    :param qID: ID assigned to each video entry in the JSON; increments from 1, and should be an integer.
    """
    database = readFile(f"userHistory.json")

    if database == []:
        print("Debug: Nothing in file.")
        output = [None, None, None, None]
        return output

    try:
        index = binVideoSearch(database, 0, len(database) - 1, qID)
        output = [info for info in database[index].values()]
    except QIDNotFoundError:
        output = [None, None, None, None]
        assert 1 == 0

    return output

def writeVideo(filename: str, qID: str, score: str, transcript: str):
    """
    Placeholder description
    """
    database = readFile(f"userHistory.json")

    # Increment number of videos, then add info as a dict into "Entries" key
    info = {
        "FILENAME": filename,
        "ID": qID,
        "SCORE": score,
        "TRANSCRIPT": transcript
    }

    # Test to see if QID already exists within JSON; if so, replace with new video info, and otherwise, overwrite video entry
    try:
        index = binVideoSearch(database, 0, len(database) - 1, qID)
        database[index] = info
    except QIDNotFoundError:
        database.append(info)
        print(database)
        database.sort(key=(lambda video : video["ID"])) 

    writeFile(database, f"userHistory.json")
    print("Write Video Test Success")

# Unused, due to change in plans
def createVidDir(firstName : str, lastName : str): 
    """
    (Unused) Creates directory to store the video files and video.json in the data folder in root.
    """
    firstName = firstName.title()
    lastName = lastName.title()
    directory = f"data/{firstName}{lastName}"
    
    try:
        absPath = os.path.dirname(__file__)
        JSONPath = os.path.join(absPath, directory)
        os.mkdir(JSONPath)
    except FileExistsError:
        print("Debug: Directory already exists")
        return

    writeFile([], f"{directory}/videos.json")
    print("Create dir test successful")


def deleteVideo(qID : int):
    """
    Placeholder
    """  
    database = readFile(f"userHistory.json")

    try:
        index = binVideoSearch(database, 0, len(database) - 1, qID)
        del(database[index])
    except QIDNotFoundError:   # QID doesn't exist, so therefore there's nothing to delete
        print("Debug: no video to delete")
        pass

    writeFile(database, f"userHistory.json")
    print("Delete video success")    


def main():
    writeVideo("video.wav", "90", "100", "California potato powers")
    test = readVideo("90")
    print(test)


if __name__ == "__main__":
    main()
