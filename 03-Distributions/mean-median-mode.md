# The Mean, the Median, and the Mode

## One-Sentence Summary

The mean, median, and mode are three different ways of describing the center of a dataset.

---

## What Is It?

When we look at a dataset, one of the first questions we ask is:

> What is a typical value?

The mean, median, and mode help answer this question.

They are called measures of central tendency because they help identify the center of a dataset.

However, they do not always tell the same story.

Each measure looks at the data differently and has its own strengths and weaknesses.

---

## Why Should I Care?

Imagine analyzing:

- Customer ages
- Product prices
- Monthly sales
- Exam scores
- Retrieval scores in a RAG system

Looking at hundreds or thousands of values individually is difficult.

We need a way to summarize the dataset with a single representative value.

The mean, median, and mode provide different ways of doing exactly that.

---

## Intuition

Imagine a group of friends discussing the average length of songs on a playlist.

One person asks:

> "What is the average song length?"

Another asks:

> "What is the middle song length?"

A third asks:

> "What song length occurs most often?"

These are three different questions.

The answers correspond to:

- Mean
- Median
- Mode

---

# Mean

## What Is the Mean?

The mean is what most people call the average.

To calculate it:

1. Add all values together.
2. Divide by the total number of values.

---

## Formula

Mean = Sum of all values ÷ Number of values

---

## Example

Dataset:

10, 20, 30, 40, 50

Step 1:

Sum the values:

150

Step 2:

Divide by the number of values:

150 ÷ 5 = 30

Mean = 30

---

## Intuition

Imagine every value is a weight placed on a seesaw.

The mean is the balancing point.

If all values could slide toward a single location, they would meet at the mean.

---

## Rock & Metal Corner

Suppose five songs have lengths:

3, 4, 5, 6, 7 minutes

Total length:

25 minutes

Average length:

5 minutes

The mean tells us the typical song length if the total playtime were evenly distributed.

---

# Median

## What Is the Median?

The median is the middle value after sorting the data.

It separates the dataset into two equal halves.

---

## Example

Dataset:

10, 20, 30, 40, 50

The middle value is:

30

Median = 30

---

## Example with Even Numbers

Dataset:

10, 20, 30, 40

Two middle values:

20 and 30

Median:

(20 + 30) ÷ 2

Median = 25

---

## Intuition

The median does not care about extreme values.

It only cares about who stands in the middle.

Imagine lining up 1,000 people by height.

The median is the person standing exactly in the middle of the line.

---

# Mode

## What Is the Mode?

The mode is the value that appears most frequently.

---

## Example

Dataset:

1, 2, 2, 2, 3, 4, 5

Mode = 2

Because 2 appears more often than any other value.

---

## Multiple Modes

Dataset:

1, 1, 2, 2, 3

Both 1 and 2 appear twice.

This dataset has two modes.

---

## Intuition

The mode is the crowd favorite.

It tells us what shows up most often.

---

## Worked Example

Let's compare all three using the same dataset.

Dataset:

10, 20, 20, 30, 40

Mean:

(10 + 20 + 20 + 30 + 40) ÷ 5

120 ÷ 5

24

Median:

Middle value = 20

Mode:

Most frequent value = 20

Results:

| Measure | Value |
|----------|--------|
| Mean | 24 |
| Median | 20 |
| Mode | 20 |

Notice that the three measures are not always identical.

---

## The Outlier Problem

This is where things become interesting.

Consider:

10, 20, 30, 40, 1000

---

### Mean

(10 + 20 + 30 + 40 + 1000) ÷ 5

1100 ÷ 5

220

---

### Median

30

---

### Mode

No mode

---

Which value better represents the dataset?

Probably:

30

The value 1000 is an outlier.

The mean was heavily influenced by it.

The median remained stable.

This is why statisticians often prefer the median when extreme values exist.

---

## The StatQuest Takeaway

The mean, median, and mode each describe the center of a dataset from a different perspective.

The important lesson is:

> There is no universally best measure of center.

The correct choice depends on the data and the problem being solved.

---

## When Should We Use Each One?

### Use the Mean When

- Data is reasonably symmetrical
- Outliers are rare
- Mathematical calculations are required

Examples:

- Test scores
- Measurement data
- Experimental results

---

### Use the Median When

- Outliers exist
- Data is skewed

Examples:

- House prices
- Salaries
- Wealth distributions

---

### Use the Mode When

- Most common value matters

Examples:

- Most common product size
- Most common shoe size
- Most common customer choice

---

## Machine Learning Connection

Measures of central tendency appear frequently in machine learning.

### Missing Value Imputation

Missing values are often replaced using:

- Mean
- Median
- Mode

depending on the feature.

---

### Feature Understanding

They help summarize variables during exploratory data analysis.

---

### Data Quality Checks

Unexpected averages may indicate issues in the data.

---

### Outlier Analysis

Comparing mean and median often reveals skewness and unusual observations.

---

## AI / LLM / RAG Connection

These concepts appear in AI systems more often than many people realize.

### Evaluation Scores

The average score across thousands of responses is simply a mean.

---

### User Feedback

Median feedback scores may be more useful than means when extreme ratings exist.

---

### RAG Evaluation

Average retrieval scores help measure overall performance.

Median scores help identify typical retrieval quality.

---

### Benchmark Analysis

Researchers frequently compare:

- Mean accuracy
- Median latency
- Most common error types

when analyzing AI models.

---

## Common Misconceptions

### Mean, Median, and Mode Are Always Similar

False.

Outliers can make them very different.

---

### The Mean Is Always Best

False.

The median is often more representative when extreme values are present.

---

### Every Dataset Has a Mode

False.

Some datasets have:

- One mode
- Multiple modes
- No mode

---

### Median Means Average

Not exactly.

The median is the middle value, not the arithmetic average.

---

## Pulkit's Mental Models

### Mean

The mean is where the dataset would balance if every value were placed on a seesaw.

---

### Median

The median does not care how extreme the outliers are.

It only cares who stands in the middle.

---

### Mode

The mode is the crowd favorite.

It tells us what appears most often.

---

## Interview Questions

### What is the difference between mean and median?

The mean is the arithmetic average.

The median is the middle value after sorting the data.

---

### Why might the median be preferred over the mean?

Because it is less sensitive to outliers.

---

### What is the mode?

The value that occurs most frequently.

---

### Can a dataset have multiple modes?

Yes.

Such datasets are called multimodal.

---

### Which measure is most affected by outliers?

The mean.

---

## Related Topics

- Variance
- Standard Deviation
- Normal Distribution
- Histograms
- Population vs Sample
- Statistical Inference

---

## References

- StatQuest: The Mean, the Median, and the Mode
- Statistics Fundamentals Playlist (StatQuest)
