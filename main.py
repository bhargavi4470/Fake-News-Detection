from src.utils import load_and_merge
from src.preprocess import clean_text
from src.models import train_model
import joblib

# Load data
data = load_and_merge('data/Fake.csv', 'data/True.csv')

# Clean text
data['clean_text'] = data['text'].apply(clean_text)

# Train model
model, vectorizer = train_model(data['clean_text'], data['label'])

# Save model and vectorizer
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
print("✅ Model and vectorizer saved!")