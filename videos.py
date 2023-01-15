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

def binVideoSearch(videos, firstIndex, lastIndex, qID):
    """
    Binary search algorithm used for searching through videos.json for 
    """
    if firstIndex <= lastIndex:

        midIndex = (lastIndex + firstIndex) // 2
        check = videos[midIndex]["QID"]

        if check == qID:
            return midIndex
            # return videos[midIndex]          # An alternative; see how JSON dicts are parsed in Javascript
        elif check > qID:
            return binVideoSearch(videos, firstIndex, midIndex - 1, qID)
        else:
            return binVideoSearch(videos, midIndex + 1, lastIndex, qID)
    else:
        print("Debug: question ID not found in videos.json; try again with another question ID.")
        raise QIDNotFoundError


def readVideo(qID: int, firstName : str, lastName : str):
    """
    Reads either a random question from a JSON file of questions, or if qID is given, then returns a specific question from 
    the database.
    :param qID: ID assigned to each video entry in the JSON; increments from 1, and should be an integer.
    """
    firstName = firstName.title()
    lastName = lastName.title()
    database = readFile(f"data/{firstName}{lastName}/videos.json")

    if database == {}:
        print("Debug: Nothing in file.")
        output = [None, None, None, None]
        return output

    videos = database["Entries"]

    try:
        index = binVideoSearch(videos, 0, len(videos) - 1, qID)
        output = [info for info in videos[index].values()]
    except QIDNotFoundError:
        output = [None, None, None, None]
        assert 1 == 0

    return output

def writeVideo(filename: str, qID: int, score: int, transcript: str, firstName : str, lastName : str):
    """
    Placeholder description
    """
    firstName = firstName.title()
    lastName = lastName.title()
    database = readFile(f"data/{firstName}{lastName}/videos.json")

    # Increment number of videos, then add info as a dict into "Entries" key
    videos = database["Entries"]
    info = {
        "Filepath": filename,
        "QID": qID,
        "Score": score,
        "Transcript": transcript
    }

    # Test to see if QID already exists within JSON; if so, replace with new video info, and otherwise, overwrite video entry
    try:
        index = binVideoSearch(videos, 0, len(videos) - 1, qID)
        videos[index] = info
    except QIDNotFoundError:
        videos.append(info)
        print(videos)
        videos.sort(key=(lambda video : video["QID"])) 

    writeFile(database, f"data/{firstName}{lastName}/videos.json")
    print("Write Video Test Success")


def createVidDir(firstName : str, lastName : str): 
    """
    Creates directory to store the video files and video.json in the data folder in root.
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

    writeFile({"Entries": []}, f"{directory}/videos.json")
    print("Create dir test successful")


def deleteVideo(qID : int, firstName : str, lastName : str):
    """
    Placeholder
    """
    firstName = firstName.title()
    lastName = lastName.title()    
    database = readFile(f"data/{firstName}{lastName}")
    videos = database["Entries"]

    try:
        index = binVideoSearch(videos, 0, len(videos) - 1, qID)
        del(videos[index])
    except QIDNotFoundError:   # QID doesn't exist, so therefore there's nothing to delete
        print("Debug: no video to delete")
        pass

    print("Delete video success")
    return    


def main():
    createVidDir("Hello", "wOrld")
    writeVideo("video.wav", 1, 100, "California potato powers", "Hello", "World")
    test = readVideo(1, "Hello", "World")
    print(test)


if __name__ == "__main__":
    main()
