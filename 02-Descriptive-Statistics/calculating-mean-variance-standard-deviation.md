# Calculating the Mean, Variance and Standard Deviation

## One-Sentence Summary

The mean tells us where the center of the data is, while variance and standard deviation tell us how spread out the data is around that center.

---

## What Is It?

When we first learn statistics, the mean seems like the most important number.

However, the mean alone does not tell the whole story.

Consider these two datasets:

Dataset A:

10, 20, 30, 40, 50

Dataset B:

0, 0, 30, 60, 60

Both have the same mean:

30

But they clearly behave very differently.

Why?

Because the values in Dataset B are much more spread out.

This is exactly why we need:

- Mean
- Variance
- Standard Deviation

Together, these three measurements help us understand both:

- The center of the data
- The spread of the data

---

## Why Should I Care?

Imagine two AI models.

Both achieve:

90% Accuracy

At first glance they appear identical.

However:

Model A consistently scores around 90%.

Model B sometimes scores 99% and sometimes 80%.

Which model would you trust more?

Most people would trust Model A because it is more consistent.

Variance and standard deviation measure that consistency.

---

## The Big Picture

Think of statistics as answering two questions:

### Question 1

Where is the center?

Answer:

Mean

---

### Question 2

How spread out is the data?

Answer:

Variance and Standard Deviation

---

If the mean gives the location of the crowd:

Variance tells us how scattered the crowd is.

---

## Step 1: Calculating the Mean

### Definition

The mean is the arithmetic average.

### Formula

Mean = Sum of Values ÷ Number of Values

---

### Example

Dataset:

10, 20, 30, 40, 50

Add all values:

10 + 20 + 30 + 40 + 50 = 150

Divide by 5:

150 ÷ 5 = 30

Mean = 30

---

## Mean Mental Model

Imagine balancing weights on a seesaw.

The mean is the point where everything balances perfectly.

---

## Step 2: Understanding Variance

### Why Variance Exists

Now that we know the center, we want to know:

> How far away are the values from that center?

Variance measures the average squared distance from the mean.

---

### Intuition

Variance answers:

> How weird is the data around the average?

Small Variance:

Values are tightly clustered.

Large Variance:

Values are spread out.

---

### Example Dataset

10, 20, 30, 40, 50

Mean:

30

---

### Calculate Distances from Mean

| Value | Distance from Mean |
|---------|---------|
| 10 | -20 |
| 20 | -10 |
| 30 | 0 |
| 40 | 10 |
| 50 | 20 |

---

### Problem

If we average these distances:

-20 + (-10) + 0 + 10 + 20

Result:

0

Everything cancels out.

This does not help.

---

### Solution

Square the distances.

| Value | Distance | Squared Distance |
|---------|----------|---------|
| 10 | -20 | 400 |
| 20 | -10 | 100 |
| 30 | 0 | 0 |
| 40 | 10 | 100 |
| 50 | 20 | 400 |

Total:

1000

---

### Variance

Divide by number of observations:

1000 ÷ 5

Variance = 200

---

## Variance Mental Model

The average tells me where the crowd is.

Variance tells me how tightly packed the crowd is.

---

## Rock & Metal Corner

Imagine two bands.

Band A:

All songs are around 5 minutes.

Band B:

Some songs are 2 minutes.

Some songs are 18 minutes.

Both bands may have the same average song length.

Band B has much higher variance.

Variance measures this unpredictability.

---

## Step 3: Understanding Standard Deviation

### Why We Need It

Variance has a problem.

The units become squared.

Example:

If song lengths are measured in minutes:

Variance is measured in:

minutes²

which is not very intuitive.

---

### Solution

Take the square root of variance.

This gives us:

Standard Deviation

---

### Formula

Standard Deviation = √Variance

---

### Example

Variance:

200

Standard Deviation:

√200

≈ 14.14

---

Now the value is back in the original units.

This makes interpretation much easier.

---

## Standard Deviation Mental Model

If variance tells us how spread out the crowd is,

standard deviation tells us the typical distance people stand from the center.

---

## Why Standard Deviation Is More Popular

In practice:

- Analysts talk about standard deviation.
- Data scientists talk about standard deviation.
- Machine learning papers often discuss standard deviation.

Rarely do people discuss variance directly.

Variance is important mathematically.

Standard deviation is easier for humans to understand.

---

## Worked Example

Dataset A:

29, 30, 31, 30, 30

Mean:

30

Very small variance.

Very small standard deviation.

Values are tightly clustered.

---

Dataset B:

0, 10, 30, 50, 60

Mean:

30

Large variance.

Large standard deviation.

Values are widely spread.

---

Both datasets share the same mean.

But they tell very different stories.

This is why mean alone is not enough.

---

## The StatQuest Takeaway

The mean tells us where the data is centered.

Variance tells us how spread out the data is.

Standard deviation converts that spread into units that are easier to understand.

Together, they provide one of the most important summaries in all of statistics.

---

## Machine Learning Connection

Variance appears everywhere in machine learning.

### Feature Scaling

Algorithms often use standard deviation during standardization.

Example:

Z-score normalization.

---

### Model Stability

Variance helps measure consistency.

Less variance often means more predictable behavior.

---

### Bias-Variance Tradeoff

One of the most important concepts in machine learning.

Models with very high variance often overfit.

You will encounter this topic later.

---

### Outlier Detection

Data points far from the mean measured in standard deviations are often considered potential outliers.

---

## AI / LLM / RAG Connection

### Model Evaluation

Average benchmark scores are useful.

Standard deviation tells us how stable those scores are.

---

### Prompt Evaluation

Average responses can look good.

Large variance may reveal inconsistency.

---

### RAG Evaluation

Retrieval scores with low variance indicate reliable retrieval.

High variance suggests unstable behavior.

---

### User Ratings

Mean ratings tell us overall satisfaction.

Standard deviation tells us how much users disagree.

---

## Common Misconceptions

### Variance and Standard Deviation Are The Same

False.

Standard deviation is the square root of variance.

---

### Mean Alone Is Enough

False.

Mean describes the center.

Variance describes the spread.

---

### High Variance Is Always Bad

False.

High variance simply means more variability.

Whether that's good or bad depends on the situation.

---

### Standard Deviation Must Be Small

False.

Some naturally occurring datasets are highly variable.

---

## Pulkit's Mental Models

### Mean

The mean is where the dataset would balance if every value were placed on a seesaw.

---

### Variance

The average tells me where the crowd is.

Variance tells me how tightly packed the crowd is.

---

### Standard Deviation

Standard deviation is the typical distance people stand from the center of the crowd.

---

## Interview Questions

### Why do we square the distances when calculating variance?

To prevent positive and negative distances from canceling each other out.

---

### What does variance measure?

The average squared distance from the mean.

---

### What does standard deviation measure?

The typical distance observations lie from the mean.

---

### Why is standard deviation often preferred over variance?

Because it uses the original units and is easier to interpret.

---

### Can two datasets have the same mean but different variances?

Yes.

And this happens frequently in real-world data.

---

## Related Topics

- Mean, Median, and Mode
- Normal Distribution
- Population and Estimated Parameters
- Variance
- Standard Deviation
- Z-Scores
- Central Limit Theorem
- Bias-Variance Tradeoff

---

## References

- StatQuest: Calculating the Mean, Variance and Standard Deviation, Clearly Explained!!!
- Statistics Fundamentals Playlist (StatQuest)
