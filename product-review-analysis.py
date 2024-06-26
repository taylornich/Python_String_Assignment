
# question 1 task 1

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    print(review)

# question 1 task 2

reviews = [
    "This product is really good. I'm impressed with its quality",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]


def word_count(reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

    positive_count = 0
    negative_count = 0

    for review in reviews:
        words = review.lower().split()

        for word in words:
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1

    return positive_count, negative_count

positive_count, negative_count = word_count(reviews)
 
print(f"Positive word count in reviews: {positive_count}.")
print(f"Negative word count in reviews: {negative_count}.")


# question 1 task 3

reviews = [
    "This product is really good. I'm impressed with its quality",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def review_summary(review):
    first_30 = review[:30]

    if len(review) > 30 and not first_30.endswith(' '):
        space = first_30.rfind(' ')

        if space != -1:
            first_30 = first_30[:space] + "..."
    return first_30

summaries = []
for review in reviews:
    summaries.append(review_summary(review))

for i in range(len(summaries)):
    print(f"Review {i + 1}: {summaries[i]}")
