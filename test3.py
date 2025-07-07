from openai import OpenAI,AuthenticationError,APIError

client = OpenAI(
        api_key = "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",
        base_url = "https://openrouter.ai/api/v1"
)

try:  
    response = client.chat.completions.create(
                model = "deepseek/deepseek-r1-0528:free",
                messages = [
                    {
                        'role':'user',
                        'content':'who are omnivorus? under 500 words'
                    }
                ],
                temperature = 0,
                max_tokens = 1000,
                stream = True
    )
    for chunk in response:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end='', flush=True)

except AuthenticationError:
    print(f"Authentication Error/maybe the key is expired")
except APIError as apier:
    print(f"API Error : {apier}")
except Exception as exp:
    print(f"Error : {exp}")