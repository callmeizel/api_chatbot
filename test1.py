from openai import OpenAI, APIError, AuthenticationError

# using OpenAI SDK
# api key - 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

client = OpenAI(
        api_key = "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",
        base_url = "https://openrouter.ai/api/v1"
        )

prompt = "explain the word <hello>, under the given <max_tokens> variable"

try:
    response = client.chat.completions.create(
                model = "deepseek/deepseek-r1-0528",
                messages = [
                    {
                        'role': 'user',
                        'content' : prompt
                    }
                ],
                temperature = 0,
                max_tokens = 500)
    
except AuthenticationError:
    print(f"Authentication Error --check your API key")
except APIError as er:
    print(f"API error : {er} ")
except Exception as ep:
    print(f"Unexpected Error : {ep} ")

print(response.choices[0].message.content)
