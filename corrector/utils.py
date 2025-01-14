from openai import OpenAI
from decouple import config

client = OpenAI(
    api_key=config("OPENAI_API_KEY"),
)

def correct_text_with_ai(text):
    content = f"""
    Вот текст: {text}
    Исправь его грамматические ошибки и объясни свои изменения. Ответь в таком формате:
    
    {{Исправленный текст}}
    
    {{Объяснение изменений}}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
    )

    try:
        message_content = response.choices[0].message.content
        ai_response = message_content.split("\n\n")
    except Exception as e:
        print(f"AI response error: {e}")
        return None, "Ошибка взаимодействия с AI"

    return ai_response[0], ai_response[1]