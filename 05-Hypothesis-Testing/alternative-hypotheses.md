# Alternative Hypotheses

## One-Sentence Summary

The alternative hypothesis represents the claim that something interesting, meaningful, or different is actually happening.

---

## What Is It?

In hypothesis testing, we always start with a null hypothesis.

The null hypothesis assumes:

> Nothing unusual is happening.

However, we usually conduct experiments because we suspect that something *is* happening.

That suspicion is captured by the Alternative Hypothesis.

The alternative hypothesis is represented by:

```text
H₁
```

or sometimes:

```text
Hₐ
```

and it represents the explanation we would accept if the null hypothesis becomes difficult to believe.

---

## Why Should I Care?

Imagine:

- A new medicine appears effective.
- A marketing campaign seems successful.
- A new machine learning model performs better.
- A new RAG strategy improves retrieval quality.

These claims are not the null hypothesis.

They are alternative hypotheses.

Without an alternative hypothesis, there is no reason to perform a hypothesis test in the first place.

---

## Relationship with the Null Hypothesis

The simplest way to think about these concepts is:

### Null Hypothesis

```text
Nothing changed.
```

### Alternative Hypothesis

```text
Something changed.
```

The goal of hypothesis testing is to determine whether the evidence is strong enough to move from the first statement to the second.

---

## Intuition

Imagine a smoke detector.

The default assumption is:

```text
There is no fire.
```

That is similar to the null hypothesis.

When enough evidence appears:

```text
Smoke
Heat
Alarm activation
```

the hypothesis changes to:

```text
There is a fire.
```

That is similar to accepting the alternative hypothesis.

---

## Courtroom Analogy

Continuing our courtroom mental model:

### Null Hypothesis

```text
The defendant is innocent.
```

### Alternative Hypothesis

```text
The defendant is guilty.
```

The prosecution must provide strong evidence.

Without sufficient evidence:

```text
The defendant remains innocent.
```

Similarly, without sufficient statistical evidence:

```text
The null hypothesis remains.
```

---

## Rock & Metal Corner

Suppose a band claims:

> "Our new album is significantly better than the previous album."

The hypotheses become:

### Null Hypothesis

```text
There is no real difference in ratings.
```

### Alternative Hypothesis

```text
The new album has genuinely higher ratings.
```

The data (listener reviews) become the evidence.

---

## The Three Main Types of Alternative Hypotheses

This is the most important part of the topic.

---

# Type 1: Two-Tailed Alternative Hypothesis

We care about differences in either direction.

Example:

### Null Hypothesis

```text
Average score = 80
```

### Alternative Hypothesis

```text
Average score ≠ 80
```

Notice:

```text
Not equal
```

This means we care about both:

- Higher values
- Lower values

---

## Intuition

We simply want to know whether something changed.

We do not care about the direction.

---

## Example

Suppose a manufacturer claims:

```text
Average package weight = 100g
```

You test samples.

You are concerned if the weight is:

- Too high
- Too low

This is a two-tailed test.

---

# Type 2: Right-Tailed Alternative Hypothesis

We care only about increases.

### Null Hypothesis

```text
Average score = 80
```

### Alternative Hypothesis

```text
Average score > 80
```

---

## Intuition

We are looking only for improvement.

Smaller values are not interesting.

---

## Example

A new medicine claims to improve recovery rates.

You only care whether recovery improves.

This becomes a right-tailed test.

---

# Type 3: Left-Tailed Alternative Hypothesis

We care only about decreases.

### Null Hypothesis

```text
Average score = 80
```

### Alternative Hypothesis

```text
Average score < 80
```

---

## Intuition

We are looking only for decline.

Higher values are not relevant.

---

## Example

Quality control teams often monitor whether performance has dropped below an acceptable level.

This naturally leads to a left-tailed test.

---

## Visual Explanation

Think of a normal distribution.

### Two-Tailed

We care about both tails.

```text
← unusual     center     unusual →
```

---

### Right-Tailed

We care only about unusually large values.

```text
center ------------→ unusual
```

---

### Left-Tailed

We care only about unusually small values.

```text
unusual ←------------ center
```

---

## The StatQuest Takeaway

The null hypothesis and alternative hypothesis always work together.

The null hypothesis provides the default explanation.

The alternative hypothesis provides the competing explanation.

The evidence determines whether the alternative becomes convincing enough.

---

## Why Alternative Hypotheses Matter

Without defining the alternative hypothesis first, we can accidentally:

- Change our conclusions after seeing the data
- Fool ourselves with randomness
- Introduce bias into experiments

Good statistical practice defines the hypotheses before collecting data.

---

## Machine Learning Connection

Alternative hypotheses appear in many ML workflows.

### Model Comparison

Null Hypothesis:

```text
Model A and Model B perform equally well.
```

Alternative Hypothesis:

```text
Model B performs better.
```

---

### Feature Engineering

Null Hypothesis:

```text
The new feature does not help.
```

Alternative Hypothesis:

```text
The new feature improves performance.
```

---

### Experiment Tracking

Many ML teams use statistical testing when comparing models.

---

## AI / LLM / RAG Connection

### Prompt Testing

Null Hypothesis:

```text
Prompt A and Prompt B are equally effective.
```

Alternative Hypothesis:

```text
Prompt B improves results.
```

---

### RAG Evaluation

Null Hypothesis:

```text
The retrieval change has no impact.
```

Alternative Hypothesis:

```text
The retrieval change improves answer quality.
```

---

### LLM Benchmarking

Alternative hypotheses are often used when comparing:

- Models
- Prompts
- Retrieval strategies
- Fine-tuned versions

---

## Common Misconceptions

### The Alternative Hypothesis Must Be True

False.

It is simply a competing explanation.

---

### Rejecting The Null Proves The Alternative

False.

Statistics supports evidence.

It does not provide absolute proof.

---

### Two-Tailed Tests Are Always Better

False.

The correct test depends on the question being asked.

---

### We Choose The Alternative After Seeing Results

False.

Hypotheses should be defined before analyzing the data.

---

## Pulkit's Mental Model

The null hypothesis is the default story.

The alternative hypothesis is the challenger trying to replace it.

---

## Interview Questions

### What is the alternative hypothesis?

A statement suggesting that an effect, difference, or relationship exists.

---

### What is the relationship between the null and alternative hypotheses?

They are competing explanations for observed data.

---

### What is a two-tailed alternative hypothesis?

A hypothesis that looks for differences in either direction.

---

### What is a one-tailed hypothesis?

A hypothesis that looks for change in only one direction.

---

### Why define hypotheses before collecting data?

To avoid bias and maintain statistical validity.

---

## Related Topics

- Hypothesis Testing
- Null Hypothesis
- p-values
- Statistical Power
- Confidence Intervals
- A/B Testing

---

## References

- StatQuest: Alternative Hypotheses: Main Ideas!!!
- Statistics Fundamentals Playlist (StatQuest)
