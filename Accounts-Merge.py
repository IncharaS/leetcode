from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        # Step 1: Set each email as its own parent and map to name
        for i in accounts:
            name = i[0]
            email = i[1:]
            for e in email:
                if e not in parent:
                    parent[e] = e
                    email_to_name[e] = name

        # Step 2: Define find function for Union-Find
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        # Step 3: Union emails in the same account
        for i in accounts:
            name = i[0]
            email = i[1:]
            root_email = email[0]  # ✅ fix: not e[0]
            r_1 = find(root_email)
            for e in email[1:]:
                r_2 = find(e)
                if r_1 != r_2:
                    parent[r_2] = r_1

        # Step 4: Group emails by their root
        group_of_email = defaultdict(list)
        for email in parent:
            root_email = find(email)
            group_of_email[root_email].append(email)

        # Step 5: Prepare output
        output = []
        for root_email, list_of_emails in group_of_email.items():
            name = email_to_name[root_email]
            output.append([name] + sorted(list_of_emails))  

        return output
