# p-hacking: What It Is and How to Avoid It

## One-Sentence Summary

p-hacking occurs when people manipulate experiments or analyses until they obtain statistically significant results, even when no real effect exists.

---

## What Is It?

p-hacking refers to a collection of practices that increase the likelihood of obtaining a statistically significant result by chance.

In simple terms:

Instead of following a predefined experiment,

someone keeps trying different analyses until a desirable p-value appears.

The result may look statistically significant,

but the conclusion may not be trustworthy.

---

## Why Should I Care?

This topic is incredibly important because:

- Researchers use significance testing.
- Data scientists run experiments.
- Machine learning teams compare models.
- AI teams evaluate prompts and retrieval strategies.

If we misuse statistical testing, we can easily convince ourselves that something works when it actually doesn't.

Understanding p-hacking helps us avoid fooling ourselves.

---

## The Big Idea

Hypothesis testing assumes:

- The experiment was planned correctly.
- The analysis was chosen beforehand.
- The researcher is not repeatedly searching for significance.

When these assumptions break down,

the p-value becomes much less reliable.

---

## Intuition

Imagine you're trying to get:

```text
p < 0.05
```

You run an experiment.

Result:

```text
p = 0.12
```

Not significant.

Instead of accepting the result, you:

- Remove some observations
- Add more observations
- Try different metrics
- Try different subsets of data
- Repeat multiple tests

Eventually:

```text
p = 0.04
```

Success?

Not necessarily.

You may simply have increased the chances of finding a random pattern.

This is p-hacking.

---

## Treasure Hunt Analogy

Imagine hiding a coin in a football field.

A friend makes one guess.

Finding it immediately would be impressive.

Now imagine they get:

```text
10,000 guesses
```

Finding the coin becomes much less surprising.

The same idea applies to p-values.

The more tests you perform,

the easier it becomes to discover apparently significant results by chance.

---

## Rock & Metal Corner

Imagine a music reviewer testing whether:

> Progressive metal fans prefer Album A over Album B.

The initial analysis shows:

```text
No significant difference.
```

The reviewer then:

- Removes some listeners
- Splits listeners into age groups
- Separates countries
- Separates streaming platforms

After enough tests:

```text
p = 0.03
```

appears somewhere.

The result looks impressive.

But it may simply be randomness disguised as discovery.

---

## Common Forms of p-hacking

### Multiple Testing

Running many tests and reporting only the significant ones.

---

### Selective Reporting

Only publishing successful results.

Ignoring failures.

---

### Data Peeking

Repeatedly checking results while collecting data.

Stopping when significance appears.

---

### Removing Outliers Selectively

Removing inconvenient observations only because they hurt significance.

---

### Trying Many Metrics

Testing:

- Accuracy
- Recall
- Precision
- F1 Score
- ROC AUC

and only reporting the metric that looks best.

---

## Why p-hacking Is Dangerous

p-hacking can create:

- False discoveries
- Misleading conclusions
- Unreliable research
- Poor business decisions

Most importantly:

It increases the chance of detecting patterns that do not actually exist.

---

## The Coin Flip Example

Suppose:

```text
20 people
```

each test a fair coin.

The null hypothesis is true.

Nothing unusual is happening.

However:

Because randomness exists,

some people may still obtain:

```text
p < 0.05
```

purely by chance.

The more tests we run,

the more likely this becomes.

---

## The StatQuest Takeaway

A statistically significant result is not automatically a trustworthy result.

The quality of the experimental process matters.

Good science requires:

- Planning experiments in advance
- Reporting all results
- Avoiding selective analysis

The goal is to discover truth,

not significance.

---

## How To Avoid p-hacking

### Pre-register Your Plan

Decide:

- Hypotheses
- Metrics
- Sample size
- Analysis method

before collecting data.

---

### Report All Results

Do not hide unsuccessful experiments.

---

### Use Appropriate Corrections

When multiple tests are performed,

use methods designed to control false discoveries.

---

### Replicate Results

If the result is real,

it should appear again.

---

### Focus on Practical Importance

A tiny p-value does not automatically mean the result matters.

Always ask:

> Is the effect actually useful?

---

## Machine Learning Connection

p-hacking can occur in ML workflows.

Examples:

### Model Selection

Trying dozens of model configurations and only reporting the best result.

---

### Hyperparameter Tuning

Repeatedly experimenting until one configuration gets lucky.

---

### Benchmark Reporting

Only publishing favorable benchmarks.

---

### Feature Selection

Testing many features and only discussing successful ones.

---

## AI / LLM / RAG Connection

This topic is extremely relevant in modern AI.

### Prompt Engineering

Trying hundreds of prompts and reporting only the best result can create misleading conclusions.

---

### RAG Evaluation

Testing many retrieval strategies increases the risk of false discoveries.

---

### Benchmark Shopping

Evaluating models on many benchmarks and only highlighting successful results.

---

### Agent Evaluation

Testing numerous workflows and presenting only the strongest outcomes.

---

In all cases:

Better methodology leads to more trustworthy conclusions.

---

## Common Misconceptions

### p-hacking Requires Fraud

False.

Most p-hacking is accidental.

Researchers genuinely believe they are improving their analysis.

---

### Significant Results Are Always Valid

False.

The process that produced the result matters.

---

### More Testing Is Always Better

False.

More testing without proper controls increases false discoveries.

---

### Small p-values Guarantee Truth

False.

A poor experiment can still produce small p-values.

---

## Pulkit's Mental Model

A p-value is a surprise meter.

p-hacking is repeatedly rolling the dice until you finally get the surprise you wanted.

---

## Interview Questions

### What is p-hacking?

Manipulating analyses or repeatedly testing data until statistical significance appears.

---

### Why is p-hacking dangerous?

It increases false discoveries and reduces trustworthiness.

---

### What are common examples of p-hacking?

- Multiple testing
- Selective reporting
- Data peeking
- Trying many metrics

---

### How can p-hacking be avoided?

Pre-registration, transparent reporting, replication, and proper statistical corrections.

---

### Can p-hacking happen in machine learning?

Yes. Feature selection, hyperparameter tuning, benchmark comparisons, and model evaluations can all be affected.

---

## Related Topics

- Hypothesis Testing
- Null Hypothesis
- Alternative Hypothesis
- p-values
- Statistical Power
- False Discovery Rate
- A/B Testing

---

## References

- StatQuest: p-hacking: What it is and how to avoid it!
- Statistics Fundamentals Playlist (StatQuest)
