from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained model tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Load pre-trained model
model = BertModel.from_pretrained('bert-base-uncased')

def encode_titles(title1, title2):
    # Tokenize the titles
    inputs = tokenizer([title1, title2], return_tensors='pt', padding=True, truncation=True)
    
    # Get the embeddings
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Use the mean of the token embeddings as the sentence embedding
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings

from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(embeddings):
    similarity = cosine_similarity(embeddings[0].unsqueeze(0), embeddings[1].unsqueeze(0))
    return similarity[0][0]
