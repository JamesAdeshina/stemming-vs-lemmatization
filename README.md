# NLP Stemming vs Lemmatization on Healthcare Text Data

## Project Overview

This project compares the effects of **stemming** and **lemmatization** techniques on healthcare text data. The goal is to evaluate how each technique processes text and how they affect the accuracy and performance of text analysis, particularly for medical-related content.

## Objective
The main objective of this project is to analyze the speed and effectiveness of stemming and lemmatization when applied to healthcare-related text data. The focus is on the processing time and how each method handles words, especially in the context of healthcare terminologies.

## Techniques Compared

1. **Stemming**: 
   - Stemming uses heuristic rules to chop off prefixes or suffixes from words, resulting in a "stem" of the word. While this method is fast, it can sometimes lead to words that are not linguistically valid.

2. **Lemmatization**: 
   - Lemmatization, in contrast, reduces words to their base form (lemma) using a vocabulary and morphological analysis. This process is slower but ensures that the words are linguistically correct.

## Methodology

1. **Preprocessing**: Tokenization, stopword removal, stemming and lemmatization are applied to healthcare-related text data.
2. **Comparison**: We compare the outputs of both techniques and assess their impact on the clarity of key medical terms.
3. **Performance**: Time performance of both techniques is measured to see how they scale with larger datasets.
4. **Results**: We analyze the effects of each technique using various metrics and discuss their applicability in natural language processing for healthcare data.

## Files

- `preprocessing.py`: Contains the functions for text preprocessing (tokenization, stopwords removal, etc.).
- `healthcare_text_data.txt`: A sample healthcare text dataset used for the analysis.


## Test Results

The following are the results from multiple tests comparing the time it takes for each technique to process the text data:

### Test Results:

1. **Test 1**: 
   - Word Count: 9653 words
   - Stemming Time: 0.057559 seconds
   - Lemmatization Time: 2.858664 seconds

2. **Test 2**: 
   - Word Count: 9653 words
   - Stemming Time: 0.075721 seconds
   - Lemmatization Time: 2.939014 seconds

3. **Test 3**: 
   - Word Count: 9653 words
   - Stemming Time: 0.054525 seconds
   - Lemmatization Time: 2.939997 seconds

4. **Test 4**: 
   - Word Count: 9653 words
   - Stemming Time: 0.044131 seconds
   - Lemmatization Time: 2.686534 seconds

5. **Test 5**: 
   - Word Count: 9653 words
   - Stemming Time: 0.043380 seconds
   - Lemmatization Time: 2.683788 seconds

6. **Test 6**: 
   - Word Count: 9653 words
   - Stemming Time: 0.051086 seconds
   - Lemmatization Time: 2.812119 seconds

7. **Test 7**: 
   - Word Count: 9653 words
   - Stemming Time: 0.045296 seconds
   - Lemmatization Time: 2.775453 seconds

8. **Test 8**: 
   - Word Count: 9653 words
   - Stemming Time: 0.043793 seconds
   - Lemmatization Time: 2.655179 seconds

9. **Test 9**: 
   - Word Count: 9653 words
   - Stemming Time: 0.043671 seconds
   - Lemmatization Time: 2.818865 seconds

10. **Test 10**: 
   - Word Count: 9653 words
   - Stemming Time: 0.059875 seconds
   - Lemmatization Time: 2.798689 seconds

## Bar chart showng the comparison of Processing Time between Stemming and Lemmatization
![Plot showing the Bar chart showng the comparison of Processing Time between Stemming and Lemmatization](https://res.cloudinary.com/dezlc4u1i/image/upload/v1731886402/e7ukacyhp3h5xnsmkccp.png)

### Conclusion

From the test results, it is evident that **stemming** consistently performs faster than **lemmatization** across multiple runs. On average, stemming times range from approximately **0.04 to 0.07 seconds**, whereas lemmatization times are significantly higher, ranging from **2.65 to 2.94 seconds**.

This difference in processing time can be attributed to the nature of both techniques:
- **Stemming** applies a simple heuristic-based rule to reduce words to their root form, making it computationally faster.
- **Lemmatization**, on the other hand, requires more complex linguistic analysis, including part-of-speech tagging and dictionary lookups, making it slower but more precise.

In practical terms, if speed is a priority and slight loss in accuracy is acceptable (e.g., in large-scale real-time applications), stemming may be the better choice. However, if accuracy and meaningful interpretation of words are more important (e.g., for detailed healthcare text analysis), lemmatization is preferable despite the higher processing time.

These insights I believe can guide the choice of technique depending on the specific use case and resource constraints in healthcare text processing tasks.

