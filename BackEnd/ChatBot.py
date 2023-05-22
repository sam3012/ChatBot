import openai

openai.api_key = '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'

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def GenerateResponse(prompt):
    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=['Human:', 'AI:']
    )

    text = response['choices'][0]['text'].strip()
    return text

if __name__ == '__main__':
    conversation = list()
    while True:
        user_input = input('USER: ')
        conversation.append(f'USER: {user_input}')
        text_block = '\n'.join(conversation)
        prompt = open_file('prompt_chat.txt').replace('<<BLOCK>>', text_block)
        prompt = prompt + '\nAI:'
        response = GenerateResponse(prompt)
        print('AI:', response)
        conversation.append(f'AI: {response}')