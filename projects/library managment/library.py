import json
from pathlib import Path

class Library:
    database = "data.json"
    memberDb = "member.json"

    def __init__(self):
        self.data = self._load_json(self.database)
        self.members = self._load_json(self.memberDb)

    def _load_json(self, file):
       if Path(file).exists():
        try:
            with open(file) as fs:
                return json.load(fs)
        except json.JSONDecodeError:   # agar file empty ya invalid ho
            return []
        else:
          return []


    def _update(self):
        with open(self.database, "w") as fs:
            json.dump(self.data, fs, indent=4)

    def _updateMembers(self):
        with open(self.memberDb, "w") as fs:
            json.dump(self.members, fs, indent=4)

    def register_member(self, name, email):
        info = {
            "name": name,
            "email": email,
            "issuedBooks": []
        }
        self.members.append(info)
        self._updateMembers()

    def add_book(self, book_info):
        self.data.append(book_info)
        self._update()

    def search_book(self, title, isbn):
        return [b for b in self.data if b["Title"] == title and b["ISBN"] == isbn]

    def issue_book(self, name, email, bookTitle, ISBN):
        member = [m for m in self.members if m["name"] == name and m["email"] == email]
        book = [b for b in self.data if b["Title"] == bookTitle and b["ISBN"] == ISBN]

        if not member or not book:
            return "Member ya Book exist nahi karti"

        book = book[0]
        member = member[0]

        if book["Available copies"] <= 0:
            return "Book available nahi hai"

        book["Available copies"] -= 1
        member["issuedBooks"].append(book)

        self._update()
        self._updateMembers()
        return "Book issue ho gayi 😎📚"

    def return_book(self, name, email, title, ISBN):
        member = [m for m in self.members if m["name"] == name and m["email"] == email]
        book = [b for b in self.data if b["Title"] == title and b["ISBN"] == ISBN]

        if not member or not book:
            return "Member ya Book exist nahi karti"

        book = book[0]
        member = member[0]

        if book not in member["issuedBooks"]:
            return "Iss member ne ye book li hi nahi"

        member["issuedBooks"].remove(book)
        book["Available copies"] += 1

        self._update()
        self._updateMembers()
        return "Book return ho gayi ✔📚"
