class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            i = email.index("@")
            local = email[:i]
            domain = email[i:]

            # Deal with local part
            if "." in local:
                local = local.replace(".", "")
            if "+" in local:
                pls_sign = local.index("+")
                local = local[:pls_sign]
            
            email = local + domain
            email_set.add(email)
        
        return len(email_set)
            
