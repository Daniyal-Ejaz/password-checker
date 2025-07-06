# password_logic.py
import re
import random
import string

def check_password_strength(password):
    score = 0
    remarks = []
    tips = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        remarks.append("❌ Too short: Use at least 8 characters.")
        tips.append("📌 Use 12+ characters to resist brute-force attacks.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("❌ Missing uppercase letter.")
        tips.append("📌 Add uppercase letters (A–Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("❌ Missing lowercase letter.")
        tips.append("📌 Use lowercase letters (a–z).")

    if re.search(r"\d", password):
        score += 1
    else:
        remarks.append("❌ Missing number.")
        tips.append("📌 Include digits (0–9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        remarks.append("❌ No special characters.")
        tips.append("📌 Use @, #, $, %, etc. to add complexity.")

    if re.search(r"(.)\1\1", password):
        remarks.append("❌ Repeating characters.")
        tips.append("📌 Avoid repeating same letters or digits.")

    common = ['password', '123456', 'qwerty', 'admin', 'letmein']
    if password.lower() in common:
        remarks.append("❌ Very common password.")
        tips.append("📌 Avoid commonly used passwords from leaked lists.")

    tips.append("🔐 Do not reuse this password across multiple websites.")

    if score >= 7:
        return "✅ Very Strong Password", remarks, tips
    elif score >= 5:
        return "⚠️ Good, but can be improved", remarks, tips
    else:
        return "❌ Weak Password", remarks, tips

def generate_password(length=14):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))
