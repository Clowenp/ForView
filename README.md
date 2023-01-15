# ForView - An Interviewing Practice Web Application

ForView is an AI-based web app aimed at non-native speakers to help improve their interview-taking skills. The user will be assigned a 
random question from a database of common interview questions, and then will record themselves making a short response with their device's camera. Once 
finished, the app runs the program through a grammar checker API (GrammarBot) and gives the user advice on how to improve the wording of their responses.

Submission for Deltahacks 9 (2022).

Created by [Aaron Jumarang](https://github.com/aaronjuma), [Owen Pan](https://github.com/Clowenp), [Jessica](https://github.com/ojaura), and [Alex Chen](https://github.com/alexchen2)

## List of Features:
- Randomly reads and loads a question from a database of interview questions
- Records and saves the user's response to the interview question (using javascript)
- Uses *speech_recognition* Python library to convert speech in recorded .wav file to text

## Planned Features:
- [ ] Login authentication system
  - [ ] Different files tracking the progress of each individual user
  - [ ] Videos stored and associated with each user
- [ ] Machine learning implemented to detect facial mannerisms during video recordings
- [ ] Detection of fluctuations in voice within newly-converted .wav file
- [ ] Implementation of more languages to translate text

## Required Dependancies/Packages:
For Python:
  1. ```speech_recognition```
  2. ```translate```
  3. ```flask```
  4. ```pydub```
  5. ```ffmpeg```
<!--  Add on more if necessary  -->

