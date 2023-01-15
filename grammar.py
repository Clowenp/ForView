import requests

def grammar_check(sentence):
    url = "https://grammarbot.p.rapidapi.com/check"

    phrase = "%20".join(sentence.split())
    payload = f"text={phrase}&language=en-US"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "dee425aed6msh6be5851497cf95fp1f44c0jsn1957c38f92c5",
        "X-RapidAPI-Host": "grammarbot.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    final_text_checked = response.text

    print(final_text_checked)