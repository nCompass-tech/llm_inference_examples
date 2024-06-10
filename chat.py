from ncompass.client import nCompass

client = nCompass(api_key = 'llama3')
'''
Sessions are a performance optimization to maintain a link between you and the server. If you want
to run multiple prompts, call the `complete_chat` command multiple within a started session
rather than restarting multiple sessions.
'''
client.start_session()
client.wait_until_model_running()
params = {'max_tokens':    300 # max output tokens requested
          , 'temperature': 0.5
          , 'top_p':       0.9
          , 'stream':      True}
messages = [
    {
        "role": "assistant",
        "content": "Hello, how can I speed up your ML inference today?",
    },
    {
        "role": "user",
        "content": "What tweaks can I make to my model to make it faster?",
    },
    {
        "role": "assistant",
        "content": "Ah, the age old question.",
    },
]
response = client.complete_chat(messages=messages
                                , add_generation_prompt=True
                                , **params)
# stream = True returns an iterator, but stream = False would return a list
# stream = True case
for res in response: print(res, end='', flush=True)
client.stop_session()

