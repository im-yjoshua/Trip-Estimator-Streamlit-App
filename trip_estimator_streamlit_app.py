import streamlit as st

def Expenses_Calculator(total_distance, petrol_Price, avg_mileage, No_Guests, Food_Price_per_person, How_Many_Days, fun_Activities, Driver_Expenses, rent_for_hotel_per_day):
    # Total Expense for Petrol
    Total_expense_of_petrol = int((total_distance / avg_mileage) * petrol_Price) * 2
    # Total Expense for Guest's food
    Total_expense_of_food = No_Guests * Food_Price_per_person
    # Total Expense for Hotel
    TotalPriceforHotel = (rent_for_hotel_per_day * How_Many_Days) * No_Guests
    # Total Expense for Driver Expenses
    TotalPriceforDriver = Driver_Expenses
    # Total Expense for Fun Activities
    TotalPriceforFunActivities = fun_Activities * No_Guests
    # Final Total 
    finalTotal = int(Total_expense_of_petrol + Total_expense_of_food + TotalPriceforHotel + TotalPriceforDriver + TotalPriceforFunActivities )
    # Total cost divided among all the guests
    dividedAmount = finalTotal / No_Guests

    return {
        "Total expense for petrol": Total_expense_of_petrol,
        "Total expense for food": Total_expense_of_food,
        "Total expense for hotel": TotalPriceforHotel,
        "Total expense for driver": TotalPriceforDriver,
        "Total expense for fun activities": TotalPriceforFunActivities,
        "Overall expense": finalTotal,
        "Total expense per person": dividedAmount
    }

# Streamlit app setup
st.title("Expenses Calculator")

# Collecting inputs
total_distance = st.number_input("Enter the total distance of your trip (in km):", min_value=0)
petrolPrice = st.number_input("Enter current petrol price (per liter):", min_value=0)
totalMileage = st.number_input("Enter the mileage of your car (km per liter):", min_value=0)
totalGuests = st.number_input("Enter the total number of guests:", min_value=1)
foodPrice = st.number_input("Enter the food price per person (per day):", min_value=0)
howManyDays = st.number_input("Enter the number of days the trip will last:", min_value=1)
funActivities = st.number_input("Enter the cost of fun activities per person:", min_value=0)
driverCost = st.number_input("Enter the total driver cost:", min_value=0)
rentForHotelPerDay = st.number_input("Enter the rent for hotel per day (per person):", min_value=0)

if st.button("Calculate Expenses"):
    expenses = Expenses_Calculator(total_distance, petrolPrice, totalMileage, totalGuests, foodPrice, howManyDays, funActivities, driverCost, rentForHotelPerDay)
    
    st.subheader("Calculation Results:")
    st.write(f"Total expense for petrol will be: {expenses['Total expense for petrol']} Rs.")
    st.write(f"Total expense for food will be: {expenses['Total expense for food']} Rs.")
    st.write(f"Total expense for hotel will be: {expenses['Total expense for hotel']} Rs.")
    st.write(f"Total expense for driver: {expenses['Total expense for driver']} Rs.")
    st.write(f"Total expense for fun activities will be: {expenses['Total expense for fun activities']} Rs.")
    st.write(f"Your overall expense would be: {expenses['Overall expense']} Rs.")
    st.write(f"Total expense per person would be estimatedly: {expenses['Total expense per person']} Rs.")
    