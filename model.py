from transformers import BertTokenizer, BertForQuestionAnswering
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration



def load_model():
    """
    Load the BERT model and tokenizer specifically fine-tuned for Q&A tasks.
    """
    tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    return model, tokenizer

def answer_question(question, context, model, tokenizer):
    """
    Takes a `question` string and an answer `context` string (text of the privacy policy),
    and finds the answer within the context using the BERT model.
    """
    # Encode the question-context pair to input_ids and segment_ids (tokens)
    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]

    # Model prediction
    answers = model(**inputs)

    # Find the position of the start and end of answer
    answer_start_scores, answer_end_scores = answers.start_logits, answers.end_logits
    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1

    # Convert tokens to the answer string
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

    return answer

# Example usage of the functions
if __name__ == "__main__":
    model, tokenizer = load_model()
    privacy_policy_text = "Your privacy policy text goes here"
    question = "What types of personal information does this privacy policy collect?"

    # Get the answer from the privacy policy
    answer = answer_question(question, privacy_policy_text, model, tokenizer)
    print("Answer:", answer)


def load_model():
    """
    Load the T5 model and tokenizer.
    """
    model_name = 't5-small'  # You can choose other versions, like 't5-base' or 't5-large'
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    return model, tokenizer

def answer_question(question, context, model, tokenizer):
    """
    Takes a `question` string and a `context` string (text of the privacy policy),
    and generates the answer using the T5 model.
    """
    input_text = "question: " + question + " context: " + context
    input_ids = tokenizer.encode(input_text, return_tensors="pt")  # Convert text to token ids
    outputs = model.generate(input_ids)  # Generate answer tokens

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)  # Decode tokens to string
    return answer

# Example usage of the functions
if __name__ == "__main__":
    model, tokenizer = load_model()
    privacy_policy_text = "Your privacy policy text goes here."
    question = "What types of personal information does this privacy policy collect?"

    # Get the answer from the privacy policy
    answer = answer_question(question, privacy_policy_text, model, tokenizer)
    print("Answer:", answer)
