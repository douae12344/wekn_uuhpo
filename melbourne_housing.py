
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

df=pd.read_csv('MELBOURNE_HOUSE_PRICES_LESS.csv')


st.title('MELBOURNE_HOUSING')

st.header('Melbourne House')

st.image('my_house.jpg')



st.write('#### min_price')
min_price=df['Price'].min()
st.write(min_price)


st.write('#### max_price')
max_price=df['Price'].max()
st.write(max_price)



st.write('#### min_distance')
min_distance=df['Distance'].min()
st.write(min_distance)



st.write('#### max_distance')
max_distance=df['Distance'].max()
st.write(max_distance)


st.write('#### mean_rooms')
mean_rooms=df['Rooms'].mean()
st.write(mean_rooms)
 
st.write('#### large_distance_price')
large_distance_price=df.groupby('Distance').mean()['Price'].nlargest(5)
st.write(large_distance_price)


st.write('#### small_regionname_price')
small_regionname_price=df.groupby('Regionname').mean()['Price'].nsmallest(5)
st.write(small_regionname_price)
 

st.write('##### large_regionname_propertycount')
large_regionname_propertycount=df.groupby('Regionname').mean()['Propertycount'].nlargest(5)
st.write(large_regionname_propertycount)
 



tab1, tab2, tab3 = st.tabs(['Numerical Features', 'Categorical Features', 'Multivariate Analysis'])


tab1.write('## My_Price')
tab1.plotly_chart(px.histogram(df, 'Price'))   
tab1.write('We observe from the graphical representation that the number of rooms in houses located in Melbourne consists mainly of 3 rooms, with a count of 28k.')
tab1.write('  And the average apartments contain 2 or 4 rooms in each area,')
tab1.write (' And the lowest percentage is one-bedroom apartments, with a count of 2111 apartments.')


tab1.write('## My_Rooms')
tab1.plotly_chart(px.histogram(df, 'Rooms'))
tab1.write('We observe and deduce from the graphical representation that whenever the distance is close to the city center, the house prices in Melbourne, Australia, are high.')


tab1.write('## My_Propertycount')
tab1.plotly_chart(px.histogram(df, 'Propertycount'))
tab1.write('We observe that the highest property rate reaches 1241, and the lowest reaches 45.')


tab1.write('## My_Distance')
tab1.plotly_chart(px.histogram(df, 'Distance'))
tab1.write('The graphical representation illustrates the distributed distances across all regions.')



tab2.write('## My_Regionname')
tab2.plotly_chart(px.histogram(df, 'Regionname'))
tab2.write('From the statement, we deduce that the highest average rate reaches 17.559k in Southern Metropolitan.')
tab2.write('And the average rate reaches 11.717 k in the Western Victoria region,')
tab2.write('As for the lowest average, it could go down to 238 in the Western Metropolitan region.')

tab2.write('## My_Councilarea')
tab2.plotly_chart(px.histogram(df, 'CouncilArea'))
tab2.write('Through the graphical representation, we observe that each region has a council.')

tab2.write('## My_Sellerg')
tab2.plotly_chart(px.histogram(df, 'SellerG'))
tab2.write('The statement includes the names of all the employees responsible for home sales.')
tab2.write('We observe that the highest number of sales were conducted by the employees:')
tab2.write('"_Jellis / _Ray / _Biggin"')

tab2.write('And the fewest sales were by the employees:')
tab2.write('"_Gravey/ _Del/ _Caine/ _Collins/ _Greg/ _Alexkarbon/ _Reliance/ _Metro/ _Only/ _HAR".')

 
tab2.write('the remaining ones except for those mentioned in the highest and average sales categories.')
        


 

col1, col2 = tab3.columns(2)
col1.write('### How distance from Downtown affects price ?')
col2.plotly_chart(px.scatter(df, 'Distance', 'Price'))
tab3.write('Through the graphical representation, we observe that as the distance increases, the price decreases. For instance, when the distance was 105, its price was 11.2 million. And when the distance was 45.9, its price was 2.225 million.')


col1, col2 = tab3.columns(2)
col1.write('### How does the location of the area affect the price of homes ?')
col2.plotly_chart(px.scatter(df, 'Regionname', 'Price'))
tab3.write('From the graphical representation, we notice that there are regions with high prices and some with low prices.')
tab3.write('_ As for the top three areas, their prices are high:')
tab3.write("'Souhen Metropolian','Northen Metropolitan','Eastern Metropolitan'") 
tab3.write('_ as for the bottom three areas, their prices are low: "Western Victoria","Eastern Victoria","Northern Victoria"')


col1, col2 = tab3.columns(2)
col1.write('### What areas contain the most and least propety ?')
col2.plotly_chart(px.scatter(df, 'Propertycount', 'Regionname'))
tab3.write('_Most properties are located in those areas: Norhen Metropolitan')
tab3.write('_ the fewest properties are found in: Western Victoria ')


col1, col2 = tab3.columns(2)
col1.write('### The council that resides in each region ?')
col2.plotly_chart(px.scatter(df, 'Regionname', 'CouncilArea'))
tab3.write('From the statement, we observe that each area includes a specific council. We also note that there are councils that appear in multiple area')
tab3.write('For example, Council:')
tab3.write('- "Hume City Council", who resides in : "Western Metropolitan" and "Norhen Metropolitan"')
