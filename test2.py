from openai import OpenAI, AuthenticationError,APIError

# api-key - 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

client = OpenAI(
        api_key = "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",
        base_url = "https://openrouter.ai/api/v1"
)


prompt = 'explain why <Oxygen> is important?'

try:
    response = client.chat.completions.create(
                model = "deepseek/deepseek-r1-0528:free",
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

    for chunks in response:
        if chunks.choices[0].delta.content:
            print(chunks.choices[0].delta.content, end='', flush=True)
            
except AuthenticationError:
    print('Authentication error --check your api key')
except APIError as apier:
    print(f"API error : {apier}")
except Exception as exp:
    print(f"Error : {exp}")