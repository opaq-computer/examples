import { createOpenAI } from '@ai-sdk/openai';
import { generateText } from 'ai';

const opaq = createOpenAI({ baseURL: 'https://opaq.computer/v1', apiKey: process.env.OPAQ_API_KEY });

const { text } = await generateText({
  model: opaq.chat('anthropic/claude-sonnet-5.5'),
  prompt: 'Name three things that should never be logged.',
});
console.log(text);
