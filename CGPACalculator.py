

# T  = 0.1*GAA + max(0.6*F + 0.2*max(QZ1,QZ2) , 0.4*F + 0.2*QZ1 + 0.3*QZ2)

while True:
    gaa = float(input("Enter Avg marks of best 10 GAA: "))
    if 0 <= gaa <= 100:
        break
    else:
        print("Enter Valid marks between 0-100")

while True:
    quiz1 = float(input("Enter Quiz 1 Marks: "))
    if 0 <= quiz1 <= 100:
        break
    else:
        print("Enter Valid marks between 0-100")

while True:
    quiz2 = float(input("Enter Quiz 2: "))
    if 0 <= quiz2 <= 100:
        break
    else:
        print("Enter Valid marks between 0-100")

while True:
    end_term = float(input("Enter End Term marks: "))
    if 0 <= end_term <= 100:
        break
    else:
        print("Enter Valid marks between 0-100")

print("\n" + "="*50)
print("📊 SCORE SUMMARY")
print("="*50)
print(f"You Average Mark of Best 10 week graded Assignment: {gaa}")
print(f"Your Quiz Score: {quiz1}")
print(f"Your quiz 2 score: {quiz2}")
print(f"Your End Term Score: {end_term}")

best_score = max(quiz2,quiz1)

Method1 = 0.1*gaa + 0.6*end_term + 0.2*best_score
Method2 = 0.1*gaa + 0.4*end_term + 0.2*quiz1 + 0.3*quiz2

final_score = max(Method1,Method2)
print("\n🧮 CALCULATING YOUR GRADE...")
print("="*50)

print(f"Your Score According to method 1: {Method1}")
print(f"Your Score According to method 2: {Method2}")
print(f"\n🏆 FINAL CALCULATION:")
print("\n" + "="*60)
print("🎉 FINAL RESULTS")
print("="*60)
print(f"Your Final Score: {final_score/10}")

def get_letter(score):
    if score >= 90:
        return "S"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return  "B"
    elif score >= 60:
        return "C"
    elif score >=50:
        return "D"
    else:
        return "F"
letter = get_letter(final_score)
print(f"Your Grade is: {letter}")

print(f"\n📈 GRADE ANALYSIS:")
if final_score >= 80:
    print("🌟 Excellent performance! You're in the top tier!")
elif final_score >= 70:
    print("👍 Good job! Solid understanding demonstrated.")
elif final_score >= 60:
    print("📚 Average performance. Consider reviewing weak areas.")
elif final_score >= 50:
    print("⚠️ Below average. Focus on fundamentals next time.")
else:
    print("🚨 Needs significant improvement. Seek help from instructors")