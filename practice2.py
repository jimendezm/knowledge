from logic import And, Not, Implication, Or, Symbol, model_check, Biconditional

"""
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
"""
fever=Symbol("fever")
cough=Symbol("cough")
rash=Symbol("rash")
flu=Symbol("flu")
measless=Symbol("measless")
antiviral_medication=Symbol("antiviral_medication")
isolation=Symbol("isolation")
blood_test=Symbol("blood_test")
public_health_authorities=Symbol("public_health_authorities")

knowledge=And(
    Implication(And(fever,cough),flu),
    Implication(And(fever,rash), measless),
    Implication(flu,antiviral_medication),
    Implication(measless,isolation),
    Implication(And(fever,Not(cough),Not(rash)),blood_test),
    Implication(isolation,public_health_authorities)
)

knowledge.add(fever)
knowledge.add(rash)
knowledge.add(Not(cough))

print(f"Diagnosis:\n The patient has flu: {model_check(knowledge, flu)}")
print(f"\nThe patient has measless: {model_check(knowledge, measless)}")

print(f"Medical action:\n Prescribed an antiviral medication: {model_check(knowledge, antiviral_medication)}")
print(f"\n Prescibed an isolation: {model_check(knowledge, isolation)}")
print(f"\n Order a blood test: {model_check(knowledge, blood_test)}")

print(f"\n Notify the authorities:{model_check(knowledge, public_health_authorities)}")

