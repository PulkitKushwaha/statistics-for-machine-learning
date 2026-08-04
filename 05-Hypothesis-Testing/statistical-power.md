# Statistical Power

## One-Sentence Summary

Statistical power is the probability that an experiment will successfully detect a real effect when that effect actually exists.

---

## What Is It?

Imagine a new medicine genuinely works.

A new machine learning model is genuinely better.

A new prompt genuinely improves results.

A new retrieval strategy genuinely helps.

Yet your experiment concludes:

```text
"No significant difference."
```

What happened?

The experiment failed to detect a real effect.

Statistical power measures how likely we are to avoid this mistake.

---

## Why Should I Care?

Most people spend a lot of time worrying about:

```text
False Positives
```

Finding effects that do not exist.

However, another problem exists:

```text
False Negatives
```

Missing effects that actually exist.

Low statistical power increases the probability of false negatives.

---

## The Big Idea

Suppose:

```text
A real effect exists.
```

Statistical power asks:

> What is the probability that my experiment will successfully discover it?

Higher power means:

```text
Greater chance of finding real effects.
```

Lower power means:

```text
Higher chance of missing real effects.
```

---

## Intuition

Imagine searching for a flashlight in a dark room.

A weak flashlight:

- Misses many objects.
- Creates uncertainty.

A powerful flashlight:

- Reveals what's actually there.

Statistical power works the same way.

A powerful experiment is better at detecting reality.

---

## Courtroom Analogy

The null hypothesis is:

```text
The defendant is innocent.
```

Now imagine:

The defendant is actually guilty.

Statistical power asks:

> How likely is the court to correctly identify guilt?

Low power:

```text
The guilty defendant often goes free.
```

High power:

```text
The court is more likely to reach the correct conclusion.
```

---

## Rock & Metal Corner

Imagine trying to determine whether fans prefer:

```text
Album A
```

or

```text
Album B
```

You only survey:

```text
5 people
```

Your experiment may miss a genuine preference.

Now survey:

```text
5,000 people
```

The real preference becomes much easier to detect.

More information creates more power.

---

## The Four Possible Outcomes

Hypothesis testing has four possible outcomes.

### Reality

Null Hypothesis True

or

Null Hypothesis False

---

### Decision

Reject H₀

or

Do Not Reject H₀

---

This creates four possibilities:

| Reality | Decision | Outcome |
|----------|----------|----------|
| H₀ True | Do Not Reject | Correct |
| H₀ True | Reject | False Positive |
| H₀ False | Reject | Correct Detection |
| H₀ False | Do Not Reject | False Negative |

---

## Where Power Fits

Power is:

```text
Probability of Correct Detection
```

Specifically:

```text
Power = Probability of Rejecting H₀
         When H₀ Is False
```

---

## Mental Model

If p-values measure:

```text
How surprised we are
```

Power measures:

```text
How likely we are to notice
```

a real effect.

---

## What Influences Statistical Power?

Several factors affect power.

---

### 1. Sample Size

The biggest factor.

Larger samples:

```text
Higher Power
```

Smaller samples:

```text
Lower Power
```

More data generally makes real effects easier to detect.

---

### 2. Effect Size

Large effects are easier to detect.

Small effects are harder to detect.

---

Example:

A medicine that improves recovery by:

```text
50%
```

is easier to detect than one improving recovery by:

```text
2%
```

---

### 3. Variability

Highly noisy data reduces power.

Stable data increases power.

---

### 4. Significance Threshold

Very strict thresholds reduce power.

More relaxed thresholds increase power.

---

## A Simple Example

Suppose:

```text
Model A Accuracy = 90%
Model B Accuracy = 90.5%
```

The improvement is tiny.

Detecting it reliably requires:

```text
Large sample size
```

Now suppose:

```text
Model B Accuracy = 98%
```

The difference becomes obvious.

Power increases dramatically.

---

## The StatQuest Takeaway

Failing to find significance does not automatically mean:

```text
No effect exists.
```

Sometimes:

```text
The experiment simply lacked power.
```

This is one of the most important lessons in statistics.

---

## Why Many Experiments Fail

Researchers often assume:

```text
No significant result
=
No effect
```

This is incorrect.

A real effect may exist.

The study simply may not have been powerful enough to detect it.

---

## Machine Learning Connection

Statistical power matters everywhere in ML.

### Model Comparisons

Tiny performance differences require:

```text
Large evaluation datasets
```

to confidently detect.

---

### Feature Engineering

Small feature improvements may be missed when experiments lack power.

---

### Hyperparameter Tuning

Weak experiments often create misleading conclusions.

---

### Benchmarking

Large benchmark datasets increase statistical power.

---

## AI / LLM / RAG Connection

### Prompt Evaluation

Prompt improvements can be subtle.

Small evaluation sets may miss them entirely.

---

### RAG Evaluation

Small test sets often create unreliable conclusions.

More evaluation questions generally improve power.

---

### LLM Benchmarking

Reliable model comparisons require enough examples to detect meaningful differences.

---

### Agent Evaluation

Many agent improvements are small.

Low-power evaluations often fail to discover genuine improvements.

---

## Common Misconceptions

### No Significant Difference Means No Effect Exists

False.

There may simply be insufficient power.

---

### Larger Samples Are Always Unnecessary

False.

Many real effects require large samples to detect.

---

### p-values And Power Are The Same Thing

False.

p-values measure evidence.

Power measures detection ability.

---

### More Power Means Better Research

Usually, but only when experiments are well-designed.

Bad experiments can still have high power.

---

## Pulkit's Mental Model

Statistical power is the brightness of your flashlight.

The brighter the flashlight, the more likely you are to see what is really there.

---

## Interview Questions

### What is statistical power?

The probability of detecting a real effect when that effect actually exists.

---

### Why is statistical power important?

It reduces the chance of missing real effects.

---

### What increases statistical power?

- Larger sample sizes
- Larger effect sizes
- Lower variability

---

### What happens when power is low?

False negatives become more likely.

---

### What is the difference between p-values and power?

p-values measure evidence.

Power measures detection capability.

---

## Related Topics

- Hypothesis Testing
- Null Hypothesis
- Alternative Hypothesis
- p-values
- p-hacking
- Power Analysis
- Confidence Intervals

---

## References

- StatQuest: Statistical Power, Clearly Explained!!!
- Statistics Fundamentals Playlist (StatQuest)
