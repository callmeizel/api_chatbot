from openai import OpenAI, APIError, AuthenticationError

# using OpenAI SDK

client = OpenAI(
        api_key = "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",
        base_url = "https://openrouter.ai/api/v1"
        )

#prompt = "explain the word <hello>, under the given <max_tokens> variable"
def model(prompt):
    try:
        response = client.chat.completions.create(
                    model = "deepseek/deepseek-r1-0528:free",
                    messages = [
                        {
                            'role' : 'user',
                            'content' : prompt
                        }
                    ],
                    temperature = 0,
                    max_tokens = 500,)
        
        return response.choices[0].message.content
        
    except AuthenticationError:
        return f"Authentication Error/maybe the key is expired"
    except APIError as er:
        return f"API error : {er} "
    except Exception as ep:
        return f"Unexpected Error : {ep} "

   

