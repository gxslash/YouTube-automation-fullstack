import json
from openai import OpenAI

MODEL = "gpt-3.5-turbo-0125"

class GPTClient:
    
    def __init__(self, api_key: str):
        self._client = self._connect_client(api_key)

    def _connect_client(self, api_key):
        client = OpenAI(api_key)
        return client
    
    def answer_question(self, q, system_prompt, max_tokens=4000):
        response = None
        try:
            response = self._client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": f"Question: {q}\nAnswer:"
                    }
                ],
                temperature=0,
                max_tokens=max_tokens,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                model=MODEL,
                response_format={ "type": "json_object" }
            )
        except Exception as e:
            print(e)
        finally:
            self._validate_response(response)
            response = json.loads(response.choices[0].message.content)
            return response
        
    def _validate_response(response):
        if response is None or response.choices[0].finish_reason == 'length':
            raise ValueError('Response value is found to be either None or too long')   