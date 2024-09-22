from openai import OpenAI

import config

client = OpenAI(
    api_key=config.OPENAI_API_KEY
)


def generate_image(prompt: str) -> list[str]:
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url"
    )
    data = response.data
    urls = []
    for item in data:
        urls.append(item.url)
    return urls
