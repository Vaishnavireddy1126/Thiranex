import re

COMMON_PASSWORDS = {"password","123456","qwerty","admin","welcome"}

def analyze_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 20

    if re.search(r"[a-z]", password):
        score += 10
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 10
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 10
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        suggestions.append("Add special characters.")

    if password.lower() not in COMMON_PASSWORDS:
        score += 20
    else:
        suggestions.append("Avoid common passwords.")

    if not re.search(r"(.)\1{2,}", password):
        score += 10
    else:
        suggestions.append("Avoid repeated characters.")

    strength = (
        "Weak" if score < 40 else
        "Moderate" if score < 60 else
        "Strong" if score < 80 else
        "Very Strong"
    )

    return score, strength, suggestions

if __name__ == "__main__":
    pwd = input("Enter password: ")
    score, strength, suggestions = analyze_password(pwd)

    print(f"Score: {score}/100")
    print(f"Strength: {strength}")
    if suggestions:
        print("\\nSuggestions:")
        for s in suggestions:
            print("-", s)
