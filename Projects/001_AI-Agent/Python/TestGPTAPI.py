from openai import OpenAI

client = OpenAI(
  api_key="please add your api key here"
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);
