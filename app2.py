import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# Sidebar Title
st.sidebar.title("STARTUP FUNDING ANALYSIS")

# Load and clean the dataset
df = pd.read_csv("streamlit_website/st_clean.csv")

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Extract year and month from date
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# Unique startup names for selection
startup_name_list = df['startup'].dropna().unique().tolist()

# Helper Function: Investor-wise Details
def investors_details(investor):
    st.title(investor)

    # Display 5 most recent investments
    last5_df = df[df['investors'].str.contains(investor, na=False)].head()[
        ['date', 'startup', 'vertical', 'city', 'round', 'amount']
    ]
    st.subheader("Most Recent Investment")
    st.dataframe(last5_df)

    # Display biggest investments by amount
    st.subheader(f"Biggest Investments by {investor}")
    big_df = df[df['investors'].str.contains(investor, na=False)]\
        .groupby('startup')['amount'].sum().sort_values(ascending=False).head()
    st.dataframe(big_df)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Biggest Investment")
        fig, ax = plt.subplots()
        ax.bar(big_df.index, big_df.values)
        st.pyplot(fig)

    with col2:
        st.subheader("Sectors Invested In")
        investment_chart = df[df['investors'].str.contains(investor, na=False)]\
            .groupby('vertical')['amount'].sum()
        fig1, ax1 = plt.subplots()
        ax1.pie(investment_chart, labels=investment_chart.index, autopct='%1.1f%%')
        st.pyplot(fig1)

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Stages Invested In")
        stage_chart = df[df['investors'].str.contains(investor, na=False)]\
            .groupby('round')['amount'].sum()
        fig2, ax2 = plt.subplots()
        ax2.pie(stage_chart, labels=stage_chart.index, autopct='%1.1f%%')
        st.pyplot(fig2)

    with col4:
        st.subheader("Cities Invested In")
        city_chart = df[df['investors'].str.contains(investor, na=False)]\
            .groupby('city')['amount'].sum()
        fig3, ax3 = plt.subplots()
        ax3.pie(city_chart, labels=city_chart.index, autopct='%1.1f%%')
        st.pyplot(fig3)

    # Year-on-Year investment trend
    year_series = df[df['investors'].str.contains(investor, na=False)]\
        .groupby('year')['amount'].sum()
    st.subheader('YoY Investment')
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index, year_series.values)
    st.pyplot(fig4)


# Helper Function: Overall Analysis
def load_overall_analyis():
    st.title("OVERALL ANALYSIS")

    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        total = round(df['amount'].sum(), 2)
        st.metric("Total", str(total), "CR")
    with col2:
        max_amount = df.groupby('startup')['amount'].sum().max()
        st.metric("Max", str(max_amount), "CR")
    with col3:
        mean = df.groupby('startup')['amount'].sum().mean()
        st.metric("Avg", str(round(mean, 2)), "CR")
    with col4:
        num_startup = df['startup'].nunique()
        st.metric("Funded Startups", str(num_startup))

    # Month-over-Month investment graph
    st.header("MoM Investment Graph")
    temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    temp_df['x_axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)

    fig5, ax5 = plt.subplots()
    ax5.plot(temp_df['x_axis'], temp_df['amount'])
    plt.xticks(rotation=90)
    st.pyplot(fig5)


# Sidebar Options
option = st.sidebar.selectbox('Select the Option', ["Overall analysis", "STARTUP", "Investors"])

if option == "Overall analysis":
    if st.sidebar.button("Show Overall Analysis"):
        load_overall_analyis()

elif option == "STARTUP":
    selected_startup = st.sidebar.selectbox("Select Startup", startup_name_list)
    st.title("STARTUP ANALYSIS")
    # You can implement detailed startup-specific view here

else:
    # Flatten all investors into a sorted unique list
    all_investors = sorted(set(df['investors'].dropna().str.split(',').sum()))
    selected_investor = st.sidebar.selectbox("Select Investor", all_investors)
    if st.sidebar.button("Show Investor Details"):
        investors_details(selected_investor)
