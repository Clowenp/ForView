"""
getQuestion.py - reads from and writes to JSON file of interview questions for later use
(Alex Chen)
"""

# Import packages
import json
import random as rd

def readFile(filename : str = "questions.json"):
    """
    Function that reads a JSON file and returns its contents (questions.json by default).
    :param filename: name of the custom JSON file being read, if any. Otherwise, defaults to "questions.json".
    """
    # Read JSON file
    try:
        with open(filename, 'r') as fh:
            reader = fh.read()
            database = json.loads(reader)
    except FileNotFoundError:
        # Temporary, for debugging/testing
        print("Error at 117, questions.py: the file boards.json has been moved. Please put the file back in its original location in \
               [the root folder].")
        assert 1 == 0

    return database

def writeFile(contents : dict, filename : str = "questions.json"):
    """
    Function that writes a dictionary to a JSON file (questions.json by default).
    :param contents: dictionary representing data that is being written to the JSON.
    :param filename: name of the custom JSON file being read, if any. Otherwise, defaults to "questions.json".
    """
    with open(filename, "w") as fh2:
        database = json.dumps(contents)
        fh2.write(database) 


def readQuestion(chooseQID : int = None):
    """
    Reads either a random question from a JSON file of questions, or if qID is given, then returns a specific question from 
    the database.
    :param chooseQID: ID assigned to each question in the JSON; increments from 1, and should be an integer.
    """
    question = ""
    content = ""
    qIDValid = True

    database = readFile()
    storedQID = [num for num in database if not database[num]["hasSeen"]] # List of all question IDs in JSON
    
    # Get question content from JSON file
    while True:
        # If list of question IDs to randomly choose from is empty, reset hasSeen status to false for all questions
        if storedQID == []:
            print("Debug: No random question available; resetting hasSeen status for all questions")
            resetReadState()
            database = readFile()
            storedQID = [num for num in database if not database[num]["hasSeen"]]

        # If qID not given or is invalid, then generates a random number to pick out a random question from JSON
        if chooseQID == None or not qIDValid:
            qID = str(rd.choice(storedQID))
        else:
            qID = str(chooseQID)

        try:
            question = database[qID]
            
            # If not requesting a new question:
            if chooseQID != None:
                content = question["content"]
                break
            else:     # Otherwise, if randomly choosing a new question:
                # If question has already been seen before, delete qID entry from storedQID and pick another random Q
                if question["hasSeen"]:
                    del(storedQID[qID])       
                    continue
                else: 
                    content = question["content"]
                    database[qID]["hasSeen"] = True  
                    break                  

        except KeyError:
            print("Question ID not found, choosing random question instead") # temp for testing
            qIDValid = False
            continue
    
    # Modify and write JSON
    writeFile(database)
    print("Read Q Test Success")     
    return {qID : content}

def addQuestion(qStr : str):
    """
    (Optional feature) Adds a question from the user into the database.
    :param qStr: String containing the question itself.
    """
    database = readFile()
    newQID = len(database) + 1
    question = {
        "content": qStr,
        "hasSeen": False
    }
    
    database[newQID] = question
    writeFile(database)


def resetReadState():
    """
    Resets hasSeen setting for every question in questions.json.
    """
    database = readFile()

    for question in database.values():
        question["hasSeen"] = False

    writeFile(database)  


def setVideoPath(qID : int, filePath : str):
    """
    Sets the video path of the question with the given filePath to the specified question ID from the JSON file.
    :param qID: ID assigned to each question in the JSON; increments from 1, and should be an integer.
    :param filePath: String of the filePath to store in the JSON.
    """
    database = readFile()
    qID = str(qID)

    try:
        database[qID]["videoPath"] = filePath
    except KeyError:
        print(f"Debug: Question ID #{qID} does not exist.")
        assert 1 == 0
    
    writeFile(database)
    print("Set Video Path Test Success")   # remove later


def readVideoPath(qID : int):
    """
    Gets the video path of the question with the specified question ID from the JSON file, if it exists.
    """
    database = readFile()
    qID = str(qID)

    try:
        output = database[qID]["videoPath"]
    except KeyError:
        print(f"Debug: Question ID #{qID} does not exist.")
        assert 1 == 0

    return output    


def readSeenQuestions():
    """
    Returns a dictionary of questions that have been viewed before in the format {<questionID>: <question content>}.
    """
    database = readFile()
    output = {qID : database[qID]["content"] for qID in database if database[qID]["hasSeen"]}
    
    return output


def main():
    """
    Just here for debugging.
    """
    setVideoPath(4, "test/path/video.mp4")
    test = readVideoPath(4)
    print(test)
    # resetReadState()

    # test = readSeenQuestions()
    # for i in test:
    #     print(f"#{i}: {test[i]}")

    # addQuestion("What is the meaning of life?")

    test = readQuestion()
    print(test)


if __name__ == "__main__":
    main()

