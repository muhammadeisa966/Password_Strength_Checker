import re
from checker.patterns import common_patterns
from checker.suggestions import get_suggestions
from utils.dictionary import is_common_word

def check_password_strength(password: str) -> dict:
    score = 0
    suggestions = []

    if len(password) > 12:
        score += 1
    else:
        suggestions.append("Make the password at least 12 characters.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Use a mix of uppercase and lowercase letters.")
    
    if re.search(r'[!@£$%^&*()_+{|[|]:;"|<>,.?/~`\\|-]', password):
        score += 1
    else:
        suggestions.append("Include special characters.")

    if any(p in password.lower() for p in common_patterns) or is_common_word(password):
        suggestions.append("Avoid common words or patters.")
    else:
        score += 1

    verdict = ["Very Weak", "Weak", "Moderate", "Strong", 'Very Strong', "Excellent"]
    return {
        "score": score,
        "verdict": verdict[score],
        "suggestions": suggestions
    }