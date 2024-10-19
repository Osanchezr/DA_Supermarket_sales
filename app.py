import streamlit as st
from backend import load_data, get_summary, plot_sales_over_time


def main():
    st.title('Supermarket Sales Dashboard')

    # Load data 
    data = load_data()
    
    # Interactive widgets
    st.sidebar.header('Controls')
# Filtro de género
    gender_options = ['Todos', 'Male', 'Female']
    selected_gender = st.sidebar.selectbox('Seleccionar género', gender_options)

# Filtro de calificación mínima (rating)
    min_rating = st.sidebar.slider('Calificación mínima', min_value=0, max_value=10, value=5, step=1)

# Filtrar los datos por rating y género
    filtered_data = data[data['Rating'] >= min_rating]

# Aplicar el filtro de género si no es 'Todos'
    if selected_gender != 'Todos':
        filtered_data = filtered_data[filtered_data['Gender'] == selected_gender]

    # Summary statistics
    updated_summary = get_summary(filtered_data)
    st.write("### Summary Statistics")
    st.table(updated_summary)

    # Display raw data
    st.write("### Raw Data")
    st.dataframe(filtered_data)

    # Plotting
    st.write("### Sales Over Time")
    plt = plot_sales_over_time(filtered_data)
    st.pyplot(plt)
    


if __name__ == '__main__':
    main()
