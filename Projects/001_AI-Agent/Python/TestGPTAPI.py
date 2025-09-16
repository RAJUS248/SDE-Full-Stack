from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);
