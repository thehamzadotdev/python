import streamlit as st
import json
import random
import string
from pathlib import Path


# ----------------- CLASS DEFINITION -----------------
class Bank:
    database = "data.json"
    data = []

    # Load data when class loads
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            with open(database, 'w') as fs:
                json.dump([], fs)
    except Exception as err:
        st.error(f"An exception occurred: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __generateRandom(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spclchr = random.choices("!@#$%^&*()", k=3)
        id_ = alpha + num + spclchr
        random.shuffle(id_)
        return "".join(id_)

    @classmethod
    def createAccount(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            st.warning("🚫 You are not eligible to open an account (must be 18+ and 4-digit pin).")
            return None
        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNumber": cls.__generateRandom(),
            "balance": 0
        }
        cls.data.append(account)
        cls.__update()
        st.success("✅ Account created successfully!")
        st.json(account)
        return account

    @classmethod
    def depositMoney(cls, accountNumber, pin, amount):
        user = next((i for i in cls.data if i["accountNumber"] == accountNumber and i["pin"] == pin), None)
        if not user:
            st.error("❌ Invalid account or pin!")
            return
        if amount <= 0:
            st.warning("⚠️ Enter a valid positive amount.")
            return
        user["balance"] += amount
        cls.__update()
        st.success(f"💰 {amount} deposited successfully!")

    @classmethod
    def withdrawMoney(cls, accountNumber, pin, amount):
        user = next((i for i in cls.data if i["accountNumber"] == accountNumber and i["pin"] == pin), None)
        if not user:
            st.error("❌ Invalid account or pin!")
            return
        if amount <= 0 or amount > user["balance"]:
            st.warning("⚠️ Invalid amount or insufficient balance.")
            return
        user["balance"] -= amount
        cls.__update()
        st.success(f"💸 {amount} withdrawn successfully!")

    @classmethod
    def showDetails(cls, accountNumber, pin):
        user = next((i for i in cls.data if i["accountNumber"] == accountNumber and i["pin"] == pin), None)
        if not user:
            st.error("❌ Invalid account or pin!")
            return
        st.subheader("👤 Account Details")
        st.json(user)

    @classmethod
    def updateDetails(cls, accountNumber, pin, name=None, email=None, new_pin=None):
        user = next((i for i in cls.data if i["accountNumber"] == accountNumber and i["pin"] == pin), None)
        if not user:
            st.error("❌ Invalid account or pin!")
            return
        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if new_pin:
            user["pin"] = new_pin
        cls.__update()
        st.success("📝 Account details updated successfully!")

    @classmethod
    def deleteAccount(cls, accountNumber, pin):
        user = next((i for i in cls.data if i["accountNumber"] == accountNumber and i["pin"] == pin), None)
        if not user:
            st.error("❌ Invalid account or pin!")
            return
        cls.data.remove(user)
        cls.__update()
        st.success("🗑️ Account deleted successfully!")


# ----------------- STREAMLIT UI -----------------
st.set_page_config(page_title="Bank App", page_icon="🏦", layout="centered")

st.title("🏦 Streamlit Bank Management System")
st.write("Manage your accounts interactively with ease 💳")

menu = st.sidebar.radio(
    "Select an Action",
    ["Create Account", "Deposit Money", "Withdraw Money", "Show Details", "Update Details", "Delete Account"]
)

# -------------- MENU OPTIONS ----------------
if menu == "Create Account":
    st.subheader("🧾 Create a New Account")
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=1, max_value=120)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")
    if st.button("Create Account"):
        if name and email and pin:
            Bank.createAccount(name, int(age), email, int(pin))
        else:
            st.warning("Please fill all fields.")

elif menu == "Deposit Money":
    st.subheader("💰 Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Deposit"):
        Bank.depositMoney(acc, int(pin), int(amount))

elif menu == "Withdraw Money":
    st.subheader("💸 Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Withdraw"):
        Bank.withdrawMoney(acc, int(pin), int(amount))

elif menu == "Show Details":
    st.subheader("🔍 View Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Show"):
        Bank.showDetails(acc, int(pin))

elif menu == "Update Details":
    st.subheader("📝 Update Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New 4-digit PIN (optional)", type="password")
    if st.button("Update"):
        Bank.updateDetails(acc, int(pin), name, email, int(new_pin) if new_pin else None)

elif menu == "Delete Account":
    st.subheader("⚠️ Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Delete"):
        Bank.deleteAccount(acc, int(pin))
