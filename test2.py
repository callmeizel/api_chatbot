from openai import OpenAI, AuthenticationError,APIError

# api-key - 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

client = OpenAI(
        api_key = "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",
        base_url = "https://openrouter.ai/api/v1"
)

prompt = 'explain why <Oxygen> is important? <limit the response under the <<max_tokens>> variable value >'

stream = client.chat.completions.create(
            model = "deepseek/deepseek-r1-0528",
            messages = [
                {
                    'role' : 'user',
                    'content' : prompt
                }
            ],
            temperature = 0.1,
            max_tokens = 500,
            stream = True
)

for chunks in stream:
    if chunks.choices[0].delta.content:
        print(chunks.choices[0].delta.content, end='', flush=True)

#print(response.choices[0].message.content)