import os

basepath = os.path.abspath(".")
print(basepath)

allQueries = "q1 q2 q3 q4 q5 q6 q7 q8 q9 q10 q11 q12 q13 q14 q15 q16 q17 q18 q19 q20 q21 q22 q23 q24 q25 q26 q27 q28 q29 q30"
f = open(basepath + "/scripts/env.txt", "w")
f.write("export EX_TAG=\"experiment_tag_sample\" \nexport TEST_QUERIES=\"" + allQueries + "\"")
f.close()
print("All queries selected")
