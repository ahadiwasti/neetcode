class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        owner = {}

        def find(email):
            if email not in parent:
                parent[email] = email

            res = email

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]

            return res 



        def union(e1,e2):
            p1,p2 = find(e1),find(e2)

            if p1 != p2:
                parent[p1] = p2

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                owner[email] = name
                union(emails[0],email)
                
        emailGroup = defaultdict(list)
        for email in parent:
            root = find(email)
            emailGroup[root].append(email)

        res = []
        for root, emails in emailGroup.items():
            res.append([owner[root]]+sorted(emails))

        return res




