from openai import OpenAI

client = OpenAI(
    api_key="sk-or-vv-25dc501d046524024b08d4d7b288e0803b2695bf795a751ef233770dd542b69c",  # ваш ключ в VseGPT после регистрации
    base_url="https://api.vsegpt.ru/v1",
)

prompt = "Напиши последовательно числа от 1 до 10"

messages = []
# messages.append({"role": "system", "content": system_text})
messages.append({"role": "user", "content": prompt})

response_big = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=messages,
    temperature=0.7,
    n=1,
    max_tokens=3000,
    extra_headers={"X-Title": "My App"},
)

response = response_big.choices[0].message.content
print("Response:", response)
