import sqlite3
import streamlit as st

# Connect to database
conn = sqlite3.connect('cars_and_drivers.db')

# Create cursor
c = conn.cursor()

# Create table cars
c.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        registration TEXT NOT NULL
    )
''')

# Create table drivers
c.execute('''
    CREATE TABLE IF NOT EXISTS drivers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        address TEXT NOT NULL
    )
''')

# Define CRUD operations

# Create
def add_car(model, year, registration):
    options = ["Volkswagen", "Toyota", "Ford"]
    selected_option = st.selectbox("Select an option", options)
    st.write("You selected:", selected_option)
    cursor.execute('INSERT INTO CARS (MODEL) VALUES (?)', (selected_option,))
    conn.commit()

def add_car(model, year, registration):
    c.execute('''
        INSERT INTO cars (model, year, registration)
        VALUES (?, ?, ?)
    ''', (model, year, registration))
    conn.commit()
# Read
def view_cars():
    c.execute('SELECT * FROM cars')
    cars = c.fetchall()
    return cars

def view_drivers():
    c.execute('SELECT * FROM drivers')
    drivers = c.fetchall()
    return drivers

# Update
def update_car(id, model=None, year=None, registration=None):
    c.execute('''
        UPDATE cars
        SET model=?, year=?, registration=?
        WHERE id=?
    ''', (model, year, registration, id))
    conn.commit()

def update_driver(id, name=None, phone_number=None, address=None):
    c.execute('''
        UPDATE drivers
        SET name=?, phone_number=?, address=?
        WHERE id=?
    ''', (name, phone_number, address, id))
    conn.commit()

# Delete
def delete_car(id):
    c.execute('DELETE FROM cars WHERE id=?', (id,))
    conn.commit()

def delete_driver(id):
    c.execute('DELETE FROM drivers WHERE id=?', (id,))
    conn.commit()

# Streamlit app

# Sidebar
menu = ['Home', 'View Cars', 'View Drivers', 'Add Car', 'Add Driver']
choice = st.sidebar.selectbox('Select option', menu)

if choice == 'Home':
    st.title('Welcome to Cars and Drivers App')
    st.write('Please select an option from the sidebar')

elif choice == 'View Cars':
    st.title('View Cars')
    cars = view_cars()
    for car in cars:
        st.write(f'ID: {car[0]}')
        st.write(f'Model: {car[1]}')
        st.write(f'Year: {car[2]}')
        st.write(f'Registration: {car[3]}')


elif choice == 'View Drivers':
    st.title('View Drivers')
    drivers = view_drivers()
    for driver in drivers:
        st.write(f'ID: {driver[0]}')
        st.write(f'Name: {driver[1]}')
        st.write(f'Phone number: {driver[2]}')
        st.write(f'Address: {driver[3]}')

elif choice == 'Add Car':
    st.title('Add Car')
    models = ['toyota', 'golf', 'mercedes',]
    model = st.selectbox('Model', options=models)
    year = st.number_input('Year', min_value=1900, max_value=2023)
    registration = st.text_input('Registration')
    if st.button('Add'):
        add_car(model, year, registration)
        st.success('Car added successfully')

elif choice == 'Add Driver':
    st.title('Add Driver')
    name = st.text_input('Name')
    phone_number = st.text_input('Phone number')
    address = st.text_input('Address')
    if st.button('Add'):
        add_driver(name, phone_number, address)
        st.success('Driver added successfully')

elif choice == 'Update Car':
    st.title('Update Car')
    car_id = st.number_input('Enter car ID', min_value=1)
    car = view_cars_by_id(car_id)
    if car:
        model = st.text_input('Model', value=car[1])
        year = st.number_input('Year', value=car[2], min_value=1900, max_value=2023)
        registration = st.text_input('Registration', value=car[3])
        if st.button('Update'):
            update_car(car_id, model, year, registration)
            st.success('Car updated successfully')
    else:
        st.warning('Car ID not found')

elif choice == 'Update Driver':
    st.title('Update Driver')
    driver_id = st.number_input('Enter driver ID', min_value=1)
    driver = view_drivers_by_id(driver_id)
    if driver:
        name = st.text_input('Name', value=driver[1])
        phone_number = st.text_input('Phone number', value=driver[2])
        address = st.text_input('Address', value=driver[3])
        if st.button('Update'):
            update_driver(driver_id, name, phone_number, address)
            st.success('Driver updated successfully')
    else:
        st.warning('Driver ID not found')

elif choice == 'Delete Car':
    st.title('Delete Car')
    car_id = st.number_input('Enter car ID', min_value=1)
    car = view_cars_by_id(car_id)
    if car:
        if st.button('Delete'):
            delete_car(car_id)
            st.success('Car deleted successfully')
    else:
        st.warning('Car ID not found')

elif choice == 'Delete Driver':
    st.title('Delete Driver')
    driver_id = st.number_input('Enter driver ID', min_value=1)
    driver = view_drivers_by_id(driver_id)
    if driver:
        if st.button('Delete'):
            delete_driver(driver_id)
            st.success('Driver deleted successfully')
    else:
        st.warning('Driver ID not found')

# Close database connection
conn.close()
