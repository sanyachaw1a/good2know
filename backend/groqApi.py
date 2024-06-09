from groq import Groq

API_KEY = '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'

client = Groq(api_key=API_KEY)


def generate_title(topic_words):
    topic_line = ', '.join(topic_words.keys())
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"generate a catchy short title that accurately describes these topic words: {topic_line}. Maximum three words. Only return the title, no need for anything else. Wrap the title in quotation marks",
        }
    ],
    model="llama3-8b-8192",
    )

    title = chat_completion.choices[0].message.content
    return title