import json


class RestAPI:
    def __init__(self, database=None):
        self.db = database or {"users": []}
        self.db["users"].sort(key=lambda u: u["name"])

    def get(self, url, payload=None):
        if url == "/users":
            return json.dumps({
                "users": [
                    u for u in self.db["users"]
                    if u["name"] in json.loads(payload)["users"]
                ]
            } if payload else self.db)

    def post(self, url, payload=None):
        payload = json.loads(payload) if payload else None

        if url == "/add":
            new_user = {
                "name": payload["user"],
                "owes": {},
                "owed_by": {},
                "balance": 0.0,
            }
            self.db["users"].append(new_user)
            self.db["users"].sort(key=lambda u: u["name"])
            return json.dumps(new_user)

        elif url == "/iou":
            lender = payload["lender"]
            borrower = payload["borrower"]
            amount = payload["amount"]

            for from_, to, amt in [(lender, borrower, amount), (borrower, lender, -amount)]:
                user = next(
                    u for u in self.db["users"]
                    if u["name"] == from_
                )
                user["balance"] += amt
                owed = user["owed_by"].pop(to, 0.0) - user["owes"].pop(to, 0.0) + amt
                if owed > 0.0:
                    user["owed_by"][to] = owed
                elif owed < 0.0:
                    user["owes"][to] = -owed

            return json.dumps({
                "users": [ u for u in self.db["users"] if u["name"] in (lender, borrower) ]
            })