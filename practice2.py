from logic import And, Not, Implication, Or, Symbol, model_check, Biconditional, XOR

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

print(f"Diagnosis: \n The patient has flu: {model_check(knowledge, flu)}")
print(f" The patient has measless: {model_check(knowledge, measless)}\n")

print(f"Medical action:\n Prescribed an antiviral medication: {model_check(knowledge, antiviral_medication)}")
print(f" Prescibed an isolation: {model_check(knowledge, isolation)}")
print(f" Order a blood test: {model_check(knowledge, blood_test)}\n")

print(f"Notify the authorities:{model_check(knowledge, public_health_authorities)}")

"""

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
"""
student_id = Symbol("student_id")
temporary_pass = Symbol("temporary_pass")
lab_access = Symbol("lab_access")
switch1 = Symbol("switch1")
switch2 = Symbol("switch2")
light_on = Symbol("light_on")
email_verification = Symbol("email_verification")
phone_verification = Symbol("phone_verification")
account_recovery = Symbol("account_recovery")
indoor_training = Symbol("indoor_training")
beach_training = Symbol("beach_training")
train_volleyball = Symbol("train_volleyball")
pizza = Symbol("pizza")
hamburger = Symbol("hamburger")
eat_fast_food = Symbol("eat_fast_food")
android = Symbol("android")
iphone = Symbol("iphone")
play_sudoku = Symbol("play_sudoku")
bus = Symbol("bus")
car = Symbol("car")
go_to_university = Symbol("go_to_university")
online_class = Symbol("online_class")
face_to_face_class = Symbol("face_to_face_class")
study_completed = Symbol("study_completed")

knowledge2 = And(
    Biconditional(lab_access,XOR(student_id, temporary_pass)),
    Biconditional(light_on,XOR(switch1, switch2)),
    Biconditional(account_recovery,XOR(email_verification, phone_verification)),
    Biconditional(train_volleyball,XOR(indoor_training, beach_training)),
    Biconditional(eat_fast_food,XOR(pizza, hamburger)),
    Biconditional(play_sudoku,XOR(android, iphone)),
    Biconditional(go_to_university,XOR(bus, car)),
    Biconditional(study_completed,XOR(online_class, face_to_face_class))
)
knowledge2.add(student_id)
knowledge2.add(Not(temporary_pass))

knowledge2.add(switch1)
knowledge2.add(Not(switch2))

knowledge2.add(email_verification)
knowledge2.add(Not(phone_verification))

knowledge2.add(indoor_training)
knowledge2.add(Not(beach_training))

knowledge2.add(pizza)
knowledge2.add(Not(hamburger))

knowledge2.add(android)
knowledge2.add(Not(iphone))

knowledge2.add(bus)
knowledge2.add(Not(car))

knowledge2.add(online_class)
knowledge2.add(Not(face_to_face_class))

print("Lab access:")
print(f" Access granted: {model_check(knowledge2, lab_access)}\n")

print("Light system:")
print(f" Light is on: {model_check(knowledge2, light_on)}\n")

print("Account recovery:")
print(f" Account recovered: {model_check(knowledge2, account_recovery)}\n")

print("Daily life examples:")
print(f" Train volleyball: {model_check(knowledge2, train_volleyball)}")
print(f" Eat fast food: {model_check(knowledge2, eat_fast_food)}")
print(f" Play sudoku: {model_check(knowledge2, play_sudoku)}")
print(f" Go to university: {model_check(knowledge2, go_to_university)}")
print(f" Study completed: {model_check(knowledge2, study_completed)}")