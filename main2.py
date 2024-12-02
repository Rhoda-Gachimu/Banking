import streamlit as st

# Initialize balance
if "balance" not in st.session_state:
    st.session_state.balance = 20.0

# Functions
def show_balance():
    st.success(f"Your balance is ${st.session_state.balance:.2f}")

def deposit(amount):
    if amount <= 0:
        st.error("Deposit amount must be greater than 0.")
    else:
        st.session_state.balance += amount
        st.success(f"${amount:.2f} deposited successfully!")

def withdraw(amount):
    if amount <= 0:
        st.error("Withdrawal amount must be greater than 0.")
    elif amount > st.session_state.balance:
        st.error("Insufficient funds!")
    else:
        st.session_state.balance -= amount
        st.success(f"${amount:.2f} withdrawn successfully!")


st.title("Nairobi Banking System")


option = st.radio("Select an action:", ("Show Balance", "Deposit", "Withdraw"))


if option == "Show Balance":
    if st.button("Check Balance"):
        show_balance()

elif option == "Deposit":
    deposit_amount = st.number_input("Enter amount to deposit:", min_value=0.0, step=0.01)
    if st.button("Deposit"):
        deposit(deposit_amount)


elif option == "Withdraw":
    withdraw_amount = st.number_input("Enter amount to withdraw:", min_value=0.0, step=0.01)
    if st.button("Withdraw"):
        withdraw(withdraw_amount)

st.write("---")
st.info("Thank you for banking with us!")
