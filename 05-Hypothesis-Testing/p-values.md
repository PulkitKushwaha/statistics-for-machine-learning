# p-values: What They Are and How to Interpret Them

## One-Sentence Summary

A p-value measures how surprising our data would be if the null hypothesis were true.

---

## What Is It?

The p-value is one of the most important and misunderstood ideas in statistics.

It helps answer the question:

> If the null hypothesis were actually true, how surprising would our observed results be?

The smaller the p-value:

- The more surprising the result
- The harder it is to explain the data using the null hypothesis

The larger the p-value:

- The less surprising the result
- The easier it is to explain the data using the null hypothesis

---

## Why Should I Care?

Suppose:

- A new medicine appears effective.
- A new ML model appears better.
- A new prompt appears superior.
- A new retrieval strategy appears to improve RAG performance.

The key question becomes:

> Is this improvement real?

or

> Could this have happened just by chance?

The p-value helps us assess that question.

---

## Quick Recap

### Null Hypothesis

The default explanation.

```text
Nothing unusual is happening.
```

---

### Alternative Hypothesis

The challenger.

```text
Something unusual is happening.
```

---

### p-value

Measures how surprising the evidence would be if the null hypothesis were true.

---

## The Courtroom Analogy

Imagine a courtroom.

### Null Hypothesis

```text
The defendant is innocent.
```

---

### Alternative Hypothesis

```text
The defendant is guilty.
```

---

### Evidence

DNA
Witnesses
Video Footage

---

### p-value

Measures how surprising the evidence would be if the defendant were actually innocent.

---

Small p-value:

```text
This evidence would be very unusual if the defendant were innocent.
```

Large p-value:

```text
This evidence is not particularly surprising.
```

---

## Intuition

Imagine a fair coin.

Null Hypothesis:

```text
The coin is fair.
```

You flip it:

```text
10 times
```

and get:

```text
5 Heads
5 Tails
```

Not surprising.

Large p-value.

---

Now suppose you get:

```text
10 Heads
0 Tails
```

Very surprising.

Small p-value.

---

The p-value quantifies this surprise.

---

## The Big Idea

A p-value is a measure of surprise.

The more surprising the result:

The smaller the p-value.

---

## What A Small p-value Means

Suppose:

```text
p = 0.001
```

This means:

> If the null hypothesis were true, results at least this extreme would be very uncommon.

Therefore:

The null hypothesis becomes difficult to believe.

---

## What A Large p-value Means

Suppose:

```text
p = 0.60
```

This means:

> The observed result is not unusual under the null hypothesis.

Therefore:

The data does not provide strong evidence against the null hypothesis.

---

## Important Rule

Small p-value:

```text
Evidence against H₀
```

Large p-value:

```text
Little evidence against H₀
```

---

## The Famous 0.05 Threshold

Many studies use:

```text
0.05
```

as the significance threshold.

This means:

### If

```text
p < 0.05
```

Reject the null hypothesis.

---

### If

```text
p ≥ 0.05
```

Do not reject the null hypothesis.

---

This threshold is a convention.

Not a law of nature.

---

## What p-values Do NOT Mean

This is where many people get confused.

---

### Wrong Interpretation

```text
The p-value is the probability that the null hypothesis is true.
```

This is FALSE.

---

### Wrong Interpretation

```text
p = 0.03 means there is a 97% chance my hypothesis is correct.
```

Also FALSE.

---

### Correct Interpretation

```text
Assuming the null hypothesis is true,
how surprising is this result?
```

That is what the p-value measures.

---

## Worked Example

Suppose a company claims:

```text
Average battery life = 10 hours
```

Null Hypothesis:

```text
Battery life = 10 hours
```

After testing:

```text
Average battery life = 13 hours
```

A statistical test produces:

```text
p = 0.002
```

Interpretation:

If the battery truly lasted 10 hours on average,

seeing a result this extreme would be very unusual.

This provides evidence against the null hypothesis.

---

## The StatQuest Takeaway

The p-value does not tell us whether a hypothesis is true.

It tells us how surprised we should be by the observed data if the null hypothesis were true.

Think:

```text
p-value = surprise level
```

The smaller the p-value,

the harder it becomes to explain the data using the null hypothesis.

---

## Machine Learning Connection

### Model Comparison

Suppose:

```text
Model A Accuracy = 91%
Model B Accuracy = 92%
```

Is the difference meaningful?

A p-value helps determine whether the difference is likely due to chance.

---

### Feature Evaluation

Did adding a feature genuinely improve performance?

Or was the improvement random?

p-values help answer this.

---

### Experiment Tracking

Many ML experiments include significance testing using p-values.

---

## AI / LLM / RAG Connection

### Prompt Testing

Prompt A:

```text
Accuracy = 82%
```

Prompt B:

```text
Accuracy = 84%
```

Is the improvement meaningful?

p-values help evaluate the evidence.

---

### RAG Evaluation

Suppose a new retrieval strategy improves answer quality.

The p-value helps determine whether the improvement is statistically meaningful.

---

### LLM Benchmarking

Researchers often compare models using significance testing rather than raw scores alone.

---

## Common Misconceptions

### Small p-value Proves My Hypothesis

False.

It only provides evidence against the null hypothesis.

---

### Large p-value Proves The Null Hypothesis

False.

It simply means the evidence is not strong enough.

---

### p-value Measures Effect Size

False.

A tiny improvement can have a tiny p-value.

The p-value measures evidence, not importance.

---

### 0.049 and 0.051 Are Completely Different

False.

They are nearly identical.

The 0.05 threshold is a convention.

---

## Pulkit's Mental Model

A p-value is a surprise meter.

The smaller it is, the harder it becomes to explain the data using the null hypothesis.

---

## Interview Questions

### What is a p-value?

A measure of how surprising the observed data would be if the null hypothesis were true.

---

### What does a small p-value indicate?

Strong evidence against the null hypothesis.

---

### What does a large p-value indicate?

Weak evidence against the null hypothesis.

---

### Does a p-value tell us whether a hypothesis is true?

No.

It only evaluates evidence against the null hypothesis.

---

### What is the common significance threshold?

0.05

---

## Related Topics

- Hypothesis Testing
- Null Hypothesis
- Alternative Hypothesis
- Statistical Power
- Confidence Intervals
- A/B Testing

---

## References

- StatQuest: p-values: What they are and how to interpret them
- Statistics Fundamentals Playlist (StatQuest)
