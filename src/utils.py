import pandas as pd

def load_and_merge(fake_path, true_path):
    fake = pd.read_csv("C:\Users\BHARGAVI\OneDrive\Documents\fake news\data\Fake.csv")
    true = pd.read_csv("C:\Users\BHARGAVI\OneDrive\Documents\fake news\data\True.csv")
    fake['label'] = 0
    true['label'] = 1
    data = pd.concat([fake, true], ignore_index=True)
    data = data.sample(frac=1, random_state=42).reset_index(drop=True)
    return data
