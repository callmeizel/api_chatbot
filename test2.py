from openai import OpenAI, AuthenticationError,APIError

client = OpenAI(
        api_key = "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",
        base_url = "https://openrouter.ai/api/v1"
)


prompt = 'explain why <Oxygen> is important? under 500 words'

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