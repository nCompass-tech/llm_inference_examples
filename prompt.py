from ncompass.client import nCompass

client = nCompass(api_key = 'llama2')
'''
Sessions are a performance optimization to maintain a link between you and the server. If you want
to run multiple prompts, call the `complete_prompt` command multiple within a started session
rather than restarting multiple sessions.
'''
client.start_session()
client.wait_until_model_running()
params = {'max_tokens':    300 # max output tokens requested
          , 'temperature': 0.5
          , 'top_p':       0.9
          , 'stream':      True}
prompt = 'Give me 5 tools I can use to accelerate inference of my ML model?'
response = client.complete_prompt(prompt, **params)
# stream = True returns an iterator, but stream = False would return a list
# stream = True case
for res in response: print(res, end='', flush=True)
client.stop_session()
