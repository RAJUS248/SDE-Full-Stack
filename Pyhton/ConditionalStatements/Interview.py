
# constant 
CGPA_REQUIRED = 8.0
PS_LEVEL_REQUIRED = 4
CODING_SKILL_LEVEL = 4

coding_skill = 4
problem_solving = 5
cs_fundamentals = 4
cgpa = 8.2         # Out of 10
communication = 2

i = 4
j = 5 
k = 4 
x = 8.2 
y = 2 

if (i >= 3 and x >= 6):
    print("Eligible for interview")

if (coding_skill >= CODING_SKILL_LEVEL and not communication < 3) or cgpa > 9:
    print("Eligible for fast-track")

# (True and not (True)) or False
# (True and False) or False
# (False) or False 
# False

if coding_skill >= 4 and problem_solving >= 4 and cs_fundamentals >= 4:
    if (cgpa >= CGPA_REQUIRED and communication >=3):
        print("Candidate meets the technical level, decision is hired!")
    else:
        print("Not hiring because of weak communication and adademics")
else:
    print("decision is NO-HIRE")

if (
    coding_skill >= 4 and
    problem_solving >= 4 and
    cs_fundamentals >= 4 and
    cgpa >= 7.0 and
    communication >= 3
):
    print("🎉 Hiring Decision: SELECTED")
else:
    print("📋 Hiring Decision: REJECTED")