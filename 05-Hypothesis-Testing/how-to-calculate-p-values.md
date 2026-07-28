# How to Calculate p-values

## One-Sentence Summary

A p-value is calculated by measuring how likely it would be to observe results as extreme as ours if the null hypothesis were true.

---

## What Is It?

In the previous topic, we learned:

> A p-value measures how surprising our data would be if the null hypothesis were true.

Now we want to answer:

> Where does that p-value actually come from?

Calculating a p-value is essentially the process of measuring surprise.

The more unusual the observed result is under the null hypothesis, the smaller the p-value becomes.

---

## Why Should I Care?

Understanding what a p-value means is helpful.

Understanding where it comes from is even better.

Many people can repeat:

```text
p < 0.05
```

but cannot explain:

- Why the p-value exists
- How it is calculated
- What it actually measures

This topic solves that problem.

---

## The Big Idea

Every p-value calculation starts with:

```text
Null Hypothesis
```

We assume:

```text
Nothing unusual is happening.
```

Then we compare:

```text
What actually happened
```

with

```text
What we would expect if the null hypothesis were true.
```

The bigger the difference, the more surprising the result becomes.

---

## Courtroom Analogy

Remember:

### Null Hypothesis

```text
The defendant is innocent.
```

Now imagine collecting evidence.

Evidence can range from:

```text
Not suspicious
```

to

```text
Extremely suspicious
```

The p-value measures:

> How likely would evidence this strong be if the defendant were actually innocent?

Small probability:

```text
Hard to believe innocence.
```

Large probability:

```text
Evidence not strong enough.
```

---

## Coin Flip Example

Suppose:

```text
Null Hypothesis:
The coin is fair
```

This means:

```text
50% Heads
50% Tails
```

---

Now flip the coin:

```text
10 times
```

Result:

```text
10 Heads
0 Tails
```

Question:

> How likely is this outcome if the coin is truly fair?

Probability:

```text
(1/2)^10

≈ 0.00098
```

This probability becomes the basis for the p-value.

---

## Intuition

A p-value calculation asks:

```text
If the null hypothesis is true,

how often would we see results
at least this extreme?
```

The key phrase is:

```text
At least this extreme
```

Not:

```text
Exactly this result
```

but:

```text
This result or something even more unusual.
```

---

## What Does "More Extreme" Mean?

This depends on the problem.

Suppose:

```text
10 coin flips
```

Observed:

```text
10 Heads
```

More extreme outcomes:

There are none.

This is already the most extreme.

---

Suppose:

```text
9 Heads
1 Tail
```

Now:

```text
10 Heads
```

would be even more extreme.

When calculating the p-value, we include both.

---

## Step-by-Step Process

### Step 1

Define the null hypothesis.

Example:

```text
The coin is fair.
```

---

### Step 2

Collect data.

Example:

```text
10 flips
9 Heads
1 Tail
```

---

### Step 3

Calculate how likely the result would be under the null hypothesis.

---

### Step 4

Include outcomes that are equally or more extreme.

---

### Step 5

Add those probabilities together.

The result is the p-value.

---

## Visual Explanation

Imagine a bell curve.

Most observations gather near the center.

The tails contain unusual outcomes.

```text
Center = Common
Tails  = Rare
```

A p-value measures the amount of probability sitting in the relevant tail(s).

The farther away our result is from the center:

- The smaller the p-value
- The more surprising the result

---

## Why This Matters

Suppose:

```text
p = 0.40
```

Interpretation:

The observed result is not unusual.

Null hypothesis remains reasonable.

---

Suppose:

```text
p = 0.0001
```

Interpretation:

The observed result would be extremely unusual if the null hypothesis were true.

The null hypothesis becomes difficult to defend.

---

## Worked Example

A company claims:

```text
Average battery life = 10 hours
```

Null Hypothesis:

```text
Average battery life = 10 hours
```

After testing:

```text
Average battery life = 13 hours
```

Question:

> If the true average is really 10 hours,

how likely would it be to observe a sample average this extreme?

The answer becomes:

```text
p-value
```

Small p-value:

Evidence against the null hypothesis.

Large p-value:

Not enough evidence.

---

## The StatQuest Takeaway

A p-value is not magical.

It is simply a probability calculation.

We:

1. Assume the null hypothesis.
2. Measure how unusual the data is.
3. Calculate how often such unusual outcomes should occur.

That probability becomes the p-value.

---

## Machine Learning Connection

### Model Comparison

Suppose:

```text
Model A = 91%
Model B = 93%
```

A p-value helps determine:

```text
Is this improvement real?
```

or

```text
Random variation?
```

---

### Feature Selection

New features often produce small improvements.

Statistical testing helps determine whether those improvements are meaningful.

---

### Experiment Tracking

Model evaluations often rely on p-values when comparing approaches.

---

## AI / LLM / RAG Connection

### Prompt Testing

Prompt B appears better than Prompt A.

The p-value helps determine whether the improvement is statistically meaningful.

---

### RAG Evaluation

A new retrieval strategy produces better results.

The p-value helps measure whether that observed improvement is likely genuine.

---

### Benchmark Analysis

Many AI papers use p-values when comparing models.

Without statistical testing, performance differences may simply reflect randomness.

---

## Common Misconceptions

### The p-value Is The Probability The Null Hypothesis Is True

False.

This is one of the most common mistakes.

---

### Small p-value Means Huge Effect

False.

It measures evidence.

Not importance.

---

### p-value Tells Us What To Believe

False.

It is evidence, not proof.

---

### p-values Eliminate Uncertainty

False.

They help quantify uncertainty.

---

## Pulkit's Mental Model

A p-value measures how surprised we should be if the null hypothesis were telling the truth.

---

## Interview Questions

### What is a p-value?

A probability measuring how surprising the observed data would be if the null hypothesis were true.

---

### What is the first step in calculating a p-value?

Define the null hypothesis.

---

### Why do we include outcomes that are more extreme?

Because p-values measure the probability of observing results at least as extreme as the data.

---

### What does a very small p-value indicate?

The observed result is difficult to explain under the null hypothesis.

---

### Does a p-value prove a hypothesis?

No.

It only measures evidence.

---

## Related Topics

- Null Hypothesis
- Alternative Hypothesis
- p-values
- Fisher's Exact Test
- Statistical Power
- Confidence Intervals

---

## References

- StatQuest: How to calculate p-values
- Statistics Fundamentals Playlist (StatQuest)
