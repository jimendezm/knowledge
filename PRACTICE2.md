# Logical Propositions

## Problem 1: Basic Medical Diagnosis

A medical clinic uses a basic rule-based system to support preliminary diagnosis decisions.

A patient arrives with confirmed fever and rash, but without cough. The goal is to determine which diagnosis and medical actions can be inferred from the available evidence.

The system must reason forward from the patient's symptoms to possible diagnoses, prescriptions, and public health actions.

### Medical Rules

- If there is fever and cough, then possible flu.
- If there is fever and rash, then possible measles.
- If there is flu, then prescribe antiviral medication.
- If there is measles, then prescribe isolation.
- If there is fever but no cough and no rash, then order a blood test.
- If isolation is prescribed, then notify public health authorities.

### Task

Model the medical rules as logical propositions, evaluate the known facts, and derive the conclusions that follow from the patient's symptoms.

### Facts

- The patient has fever.
- The patient has rash.
- The patient does not have cough.

### Questions

- What diagnosis can be derived?
- What medical action should be prescribed?
- Should public health authorities be notified?

### Event to Corroborate

If the patient is later confirmed not to have a rash, does the derived diagnosis or medical action change?

## Problem 2: Exclusive Choice

Some systems require exactly one option to be active. In these cases, a regular OR is not enough because both options cannot be true at the same time.

The goal is to model situations where one condition or another condition may be true, but not both. Use the XOR operation to represent this type of exclusive choice.

### System Rules

- A student can enter the lab using either a student ID or a temporary pass, but not both at the same time.
- A light is on if exactly one of two switches is activated.
- A user can recover an account using either email verification or phone verification, but not both methods together.

### Task

1. Model each situation as logical propositions using the XOR operation.

2. Propose five examples from your daily life where the XOR operation applies, and model each one as logical propositions.

### Facts

- XOR is true when exactly one proposition is true.
- XOR is false when both propositions are true.
- XOR is false when both propositions are false.

### Questions

- How would you model the lab access rule using XOR?
- How would you model the light switch rule using XOR?
- How would you model the account recovery rule using XOR?
