from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Summarize a construction project status report in 3 bullet points"
)

print(response.output[0].content[0].text)
