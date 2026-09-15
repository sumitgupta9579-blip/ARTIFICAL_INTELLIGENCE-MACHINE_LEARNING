student={
    "Math":80,
    "Science":90,
    "English":85
}

sub=[]

for subject in student :
    if student[subject]>=85:
        # print(subject)
        sub.append(subject)

print(sub)
