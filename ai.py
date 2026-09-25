from google import genai
import time

client = genai.Client()

def ask_ai(question, note):

    with open(note, 'r') as file:
        notes = file.read()

    for attempt in range(3):
        try:
            reponse = client.models.generate_content(
                model='gemini-3.8-flash',
                contents=f"""
                You are a study assistant.

                Answer the student's question using their notes.

                NOTES:
                {notes}

                QUESTION:
                {question}
                """
            )

            print('\nAnswer: ')
            print(reponse.text)
            break
        except Exception as e:
            print(f'Attempt {attempt + 1} failed.')
            
            if attempt < 2:
                print('Retrying in 5 seconds...')
                time.sleep(5)
            else:
                print('Could not connect Gemini. Try again later.')
                print(e)

def summarise(note):
    with open(note, 'r') as file:
        notes = file.read()
    
    for attempt in range(3):
        try:
            reponse = client.models.generate_content(
                model='gemini-3.8-flash',
                contents=f"""
                You are a study assistant.

                Summarise the student's notes.

                NOTES:
                {notes}
                """
            )

            print("\nSummary:")
            print(reponse)
            break
        except Exception as e:
            print(f'Attempt {attempt + 1} failed.')

            if attempt < 2:
                print('Retrying in 5 seconds...')
                time.sleep(5)
            else:
                print('Could not connect Gemini. Try again later.')
                print(e)
        