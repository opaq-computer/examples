import OpenAI from 'openai';

const client = new OpenAI({ baseURL: 'https://opaq.computer/v1', apiKey: process.env.OPAQ_API_KEY });

const stream = await client.chat.completions.create({
  model: 'deepseek/deepseek-v4.1-flash',
  stream: true,
  messages: [{ role: 'user', content: 'Write a haiku about privacy.' }],
});
for await (const chunk of stream) process.stdout.write(chunk.choices[0]?.delta?.content ?? '');
process.stdout.write('\n');
