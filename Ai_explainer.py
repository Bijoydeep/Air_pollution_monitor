import openai

openai.api_key = "your-openai-key"  # 🔐 Replace with your actual key

def explain_trend(df):
    df = df.tail(30).dropna()
    text_data = df.to_csv()

    prompt = f"""You're an environmental data analyst.
Analyze the following 30-day air pollution dataset and summarize trends or anomalies.

{str(text_data)}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message["content"]
