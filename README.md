# English to Hinglish Code-Mixed Language Translation Model

In this project, I have developed a model for converting English text to Hinglish, which is a code-mixed language combining English and Hindi. I utilized a custom dataset and a pre-trained transformer model for this task.

## Dataset Creation

To train my English to Hinglish translation model, I employed the "Hinglish TOP Dataset" available on Kaggle. I selectively translated English words into Hindi within certain conditions:

1. **Preservation of English Words:** If the Hindi text contains any nouns, dates, times, or viable English words, I retained the English words as they are.

2. **Translation to Hindi:** If the Hindi text does not contain nouns, dates, times, or recognizable English words, I translated those words to Hindi.

3. **Retention of Unfamiliar Words:** In cases where the translator was uncertain about a word, I kept the original word.

By applying these conditions, I created a dataset containing approximately 10,000 records, each consisting of an English sentence and its corresponding Hinglish code-mixed sentence.

## Model Creation

For building my translation model, I used the custom dataset to fine-tune the "Helsinki-NLP/opus-mt-en-hi" transformer model. This model was originally designed for English to Hindi translation and served as an excellent starting point for my task.

## Outputs

The model's outputs for the required task are saved in the `output.txt` file, and you can find the working code for a dynamic translation process in the `hinglish.py` file.

With this English to Hinglish translation model, I can facilitate communication in code-mixed environments, where both English and Hindi are commonly used. This tool can be valuable for various applications, such as social media content generation, customer support in mixed-language regions, and more. The model provides a bridge for users who prefer Hinglish and enables them to understand and interact with content originally in English.
