import streamlit as st
from library import Library

lib = Library()

st.set_page_config(page_title="Library Management", page_icon="📚", layout="centered")

st.title("📚 Library Management System")
st.write("Hamza ki OP Library App 🤝🔥")

menu = st.sidebar.radio("Menu", [
    "Register Member",
    "Add Book",
    "Search Book",
    "Issue Book",
    "Return Book"
])

# REGISTER MEMBER
if menu == "Register Member":
    st.subheader("👤 Register New Member")
    name = st.text_input("Name")
    email = st.text_input("Email")

    if st.button("Register"):
        lib.register_member(name, email)
        st.success("Member registered successfully 🎉")

# ADD BOOK
elif menu == "Add Book":
    st.subheader("➕ Add New Book")

    title = st.text_input("Book Title")
    author = st.text_input("Author")
    category = st.text_input("Category")
    year = st.number_input("Publication Year", step=1)
    isbn = st.number_input("ISBN", step=1)
    total = st.number_input("Total Copies", step=1)
    available = st.number_input("Available Copies", step=1)
    desc = st.text_area("Description")

    if st.button("Add Book"):
        book = {
            "Title": title,
            "Author": author,
            "Category": category,
            "Publication year": year,
            "ISBN": isbn,
            "Total copies": total,
            "Available copies": available,
            "Description": desc
        }
        lib.add_book(book)
        st.success("Book added successfully 📘✨")

# SEARCH BOOK
elif menu == "Search Book":
    st.subheader("🔍 Search Book")
    title = st.text_input("Book Title")
    isbn = st.number_input("ISBN", step=1)

    if st.button("Search"):
        result = lib.search_book(title, isbn)
        if result:
            st.json(result[0])
        else:
            st.error("Book not found 😔")

# ISSUE BOOK
elif menu == "Issue Book":
    st.subheader("📖 Issue Book")

    name = st.text_input("Member Name")
    email = st.text_input("Member Email")
    title = st.text_input("Book Title")
    isbn = st.number_input("ISBN", step=1)

    if st.button("Issue"):
        msg = lib.issue_book(name, email, title, isbn)
        st.info(msg)

# RETURN BOOK
elif menu == "Return Book":
    st.subheader("↩ Return Book")

    name = st.text_input("Name")
    email = st.text_input("Email")
    title = st.text_input("Book Title")
    isbn = st.number_input("ISBN", step=1)

    if st.button("Return"):
        msg = lib.return_book(name, email, title, isbn)
        st.success(msg)
