# install [pip install datasets transformers[sentencepiece] sacrebleu -q]
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

def translate_text(input_text, model_checkpoint="Helsinki-NLP/opus-mt-en-hi", max_length=128):
    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    model = TFAutoModelForSeq2SeqLM.from_pretrained('translation_model')

    # Tokenize the input text
    tokenized = tokenizer([input_text], return_tensors='np')

    # Generate translation
    out = model.generate(**tokenized, max_length=max_length)

    # Decode and return the translated text
    with tokenizer.as_target_tokenizer():
        translated_text = tokenizer.decode(out[0], skip_special_tokens=True)

    return translated_text

input_text = input("Enter the text you want to translate: ")
translated_text = translate_text(input_text)
print("\nTranslated Text:", translated_text)