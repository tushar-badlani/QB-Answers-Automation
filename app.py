import requests

url = "http://localhost:11434/api/generate"



# data = {
#   "model": "llama3",
#   "prompt":"Why is the sky blue?",
#   "stream": False
# }
#
# response = requests.post(url, json=data)
#
# result = response.json()
# print(result['response'])


with open('qb.txt', 'r') as file:

    for line in file:
        print(line)
        data = {
            "model": "llama3",
            "prompt": f"you are a student appearing for an university level proffesional skills for enginners exam tommorow. This is the question: '{line}' write the best answer to this question. Write exactly like you would in the exam",
            "stream": False
        }

        response = requests.post(url, json=data)

        result = response.json()
        with open('qb_answers.txt', 'a') as file:
            file.write(result['response'] +'\n'+ 'End of a' +'\n')

