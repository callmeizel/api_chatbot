from openai import OpenAI, APIError, AuthenticationError

# using OpenAI SDK
# # api-key - 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

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
    print(f"Authentication Error --check your API key")
except APIError as er:
    print(f"API error : {er} ")
except Exception as ep:
    print(f"Unexpected Error : {ep} ")

print(response.choices[0].message.content)
