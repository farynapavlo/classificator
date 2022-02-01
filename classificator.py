from __future__ import division
from collections import defaultdict
from math import log

def read_sample(file_name):
    sample = []
    f = open(f"{file_name}")
    
    for line in f:
        sample.append(line.strip().split(" "))
    
    f.close()
    return sample

def add_to_sample(file_name):
    f = open(f"{file_name}", "a")
    
    name, gender = input("Enter a name: ").capitalize(), input("Enter a gender (woman/man): ").lower()
    print()
    if gender in ["woman", "man"]:
        f.write(f"{name} {gender}\n")
    
    f.close()
    
def train(samples):
    classes, freq = defaultdict(lambda:0), defaultdict(lambda:0)
    
    for feats, label in samples:
        classes[label] += 1                 
        for feat in feats:
            freq[label, feat] += 1          

    for label, feat in freq:                
        freq[label, feat] /= classes[label]
    
    for c in classes:                       
        classes[c] /= len(samples)

    return classes, freq                    

def classify(classifier, feats):
    classes, prob = classifier
    return min(classes.keys(),              
        key = lambda cl: -log(classes[cl]) + \
            sum(-log(prob.get((cl,feat), 10**(-7))) for feat in feats))

def get_features(sample): return (
        'll: %s' % sample[-1],          # get last letter
        'fl: %s' % sample[0],           # get first letter
        'sl: %s' % sample[1],           # get second letter
        )

def get_gender(file_name, name):
    samples = read_sample(file_name)
    features = [(get_features(feat), label) for feat, label in samples]
    classifier = train(features)
    return classify(classifier, get_features(u'{}'.format(name.lower())))

def show_info(name, gender):
    print(f"""
    Name  : {name.capitalize()}
    Gender: {gender.capitalize()}
""")
    
if __name__ == "__main__":
    
    
    while True:
        choice = input("""1 - teach
2 - check
Enter your choice: """)
        print()
        if choice == "2":
            name = input("Enter a name: ")
            gender = get_gender(r'C:\Users\faryn\OneDrive\Рабочий стол\Лаби політех\Курсова\names.txt', name)
            show_info(name, gender)
        elif choice == "1":
            add_to_sample(r'C:\Users\faryn\OneDrive\Рабочий стол\Лаби політех\Курсова\names.txt')
        else:
            break

