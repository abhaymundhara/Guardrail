import re
from typing import Dict, List

class PolicyEngine:
    def __init__(self):
        self.policies = [
            PIIPolicy(),
            ProfanityPolicy(),
            UnauthorizedRefundPolicy()
        ]
    
    def evaluate(self, output: str, context: Dict) -> Dict:
        violations = []
        for policy in self.policies:
            if policy.violates(output, context):
                violations.append(policy.name)
        allowed = len(violations) == 0
        return {
            "allowed": allowed,
            "violations": violations,
            "confidence": 1.0 if allowed else 0.0
        }

class PIIPolicy:
    name = "PII_LEAKAGE"
    patterns = [
        r'\b\d{3}-\d{2}-\d{4}\b',
        r'\b\d{16}\b',
        r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',
        r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    ]
    
    def violates(self, output: str, context: Dict) -> bool:
        for pattern in self.patterns:
            if re.search(pattern, output, re.IGNORECASE):
                return True
        return False

class ProfanityPolicy:
    name = "PROFANITY"
    banned_words = ['fuck', 'shit', 'damn', 'bitch']
    
    def violates(self, output: str, context: Dict) -> bool:
        output_lower = output.lower()
        return any(word in output_lower for word in self.banned_words)

class UnauthorizedRefundPolicy:
    name = "UNAUTHORIZED_REFUND"
    max_refund = 100
    
    def violates(self, output: str, context: Dict) -> bool:
        if 'refund' not in output.lower():
            return False
        amounts = re.findall(r'\$(\d+)', output)
        for amount in amounts:
            if int(amount) > self.max_refund:
                return True
        return False
