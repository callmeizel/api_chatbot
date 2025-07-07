from openai import OpenAI, APIError, AuthenticationError

# using OpenAI SDK

client = OpenAI(
        api_key = "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",
        base_url = "https://openrouter.ai/api/v1"
        )

prompt = "explain the word <hello>, under the given <max_tokens> variable"

try:
    response = client.chat.completions.create(
                model = "deepseek/deepseek-r1-0528:free",
                messages = [
                    {
                        'role': 'user',
                        'content' : prompt
                    }
                ],
                temperature = 0,
                max_tokens = 500)
    
except AuthenticationError:
    print(f"Authentication Error/maybe the key is expired")
except APIError as er:
    print(f"API error : {er} ")
except Exception as ep:
    print(f"Unexpected Error : {ep} ")

print(response.choices[0].message.content)
