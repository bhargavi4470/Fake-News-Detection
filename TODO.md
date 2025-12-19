# TODO List for Fixing Fake News Detector Misclassification

## Step 1: Add Debug Output in Detector.py
- [x] Add debug output to show cleaned input text
- [x] Add debug output to show prediction probabilities for both classes
- [x] Add debug output to show the raw prediction value

## Step 2: Verify Model and Vectorizer Files
- [x] Check timestamps of model.pkl and vectorizer.pkl
- [x] Retrain model if files are outdated or if needed
- [x] Run main.py to retrain and save new model/vectorizer

## Step 3: Improve Prediction Logic (Optional)
- [x] Consider adding a confidence threshold (e.g., if confidence < 60%, show uncertain)
- [ ] Add explainability features if possible
- [ ] Test with various real and fake news inputs

## Followup Steps
- [ ] Test the app with real news inputs
- [ ] Test the app with fake news inputs
- [ ] Gather user feedback on predictions
