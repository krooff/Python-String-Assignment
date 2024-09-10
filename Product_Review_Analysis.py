#Task 1: Keyword Highlighter

keywords = ["good", "excellent", "bad", "poor", "average"]

# List of product reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def highlight_keywords(review, keywords):
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    return review

for review in reviews:
    highlighted_review = highlight_keywords(review, keywords)
    print(highlighted_review)

highlight_keywords()

#Task 2: Sentiment Tally

# List of positive and negative words
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(review, positive_words, negative_words):
    # Split the review into words
    words = review.lower().split()
   
    positive_count = 0
    negative_count = 0
    
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1
    
    return positive_count, negative_count

# Example usage
for review in reviews:
    pos_count, neg_count = sentiment_tally(review, positive_words, negative_words)
    print(f"Review: {review}\nPositive words: {pos_count}, Negative words: {neg_count}\n")

#Task 3: Review Summary

def review_summary(review, length=30):
    if len(review) <= length:
        return review 
        
    # Find the last space within the allowed length
    end_index = review.rfind(' ', 0, length)
    
    if end_index == -1:
      
      return review[:length] + "…"
    
    return review[:end_index] + "…"

# Example usage
for review in reviews:
    summary = review_summary(review)
    print(f"Summary: {summary}\n")
