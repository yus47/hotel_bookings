<a name="readme-top"></a>

> [!NOTE]
> <b>AlphaGroup_JC_DS_FT_JKT_24_FinalProject</b>

<h1 align="center">
  <span style="color: #627254; font-size: 44px; font-weight: bold;">
    Maintaining Vila Galé Hotel Revenue: Predictive Analytics for Reservation Cancellations and No-Shows in The Hospitality Sector
  </span>
</h1>

---

<div style="text-align: left;">
  <h2 style="background-color: #2C3E3D; color: white; padding: 10px 20px; margin-bottom: 20px; border-radius: 8px; font-weight: bold; font-style: italic; display: inline-block;">Final Project: Data-Driven Analysis and Supervised Learning Classification</h2>
</div>

> [!IMPORTANT]
> `Disclaimer: 
This final project serves as a final crucial component of the educational and assessment sequence in Job Connector Data Science and Machine Learning Program at Purwadhika Digital Technology School. The notebook might be too heavy to be rendered in Github reader, please kindly download the notebook to your local environment to read the Jupyter Notebook.`

**Author:** [Arief Luqman Hakiem](https://www.linkedin.com/in/ariefluqman/), [Samuel Semaya](https://www.linkedin.com/in/samuelsemaya/), and [Yusuf Sidharta](https://www.linkedin.com/in/yusuf-sidharta-257203127/) <br>
**Batch:** JCDS 2404 <br>
**Date Submitted and Last Updated:** `2024-09-05` <br>
**Data Source:** [Kaggle Hotel Bookings Demand Dataset](https://www.kaggle.com/jessemostipak/hotel-booking-demand/data) <br>

<div style="text-align: left;">
  <h2 style="background-color: #2C3E3D; color: white; padding: 10px 20px; margin-bottom: 20px; border-radius: 8px; font-weight: bold; display: inline-block;">Supporting Resources</h2>
</div>

---

 **Github:** [Repository](https://github.com/PurwadhikaDev/AlphaGroup_JC_DS_FT_JKT_24_FinalProject) <br>
 **Tableau:** [Dashboard](https://public.tableau.com/app/profile/samuelsemaya/viz/hotel_bookings_17248493669470/DashboardSummary) <br>
 **Streamlit:** [Deployment](https://hotel-cancellation-alpha-group.streamlit.app/)

<div style="text-align: left;">
  <h2 style="background-color: #2C3E3D; color: white; padding: 10px 20px; margin-bottom: 20px; border-radius: 8px; font-weight: bold; display: inline-block; font-size: 30px">Context</h2>
</div>

---

<div style='text-align: justify'>

<strong>Vila Galé</strong>, founded in 1986, is one of the largest hotel groups in <strong>Portugal</strong>. Boasting top location, comfort, and decoration of its 31 hotels, Vila Galé gets a rank in the top 120 hotel companies in the world. This company also prioritizes availability and friendliness of each unit team, making sure that their slogan of “Always Close to You” is always true in serving their guests [[1]](https://www.linkedin.com/company/vila-gale-s-a-/about/). Two of their hotels are located in <strong>Albufeira and Lisbon</strong>. Albufeira municipality is one of the largest, liveliest, and most exciting resort towns among other Portugal coastline areas [[2]](https://www.algarve-tourist.com/albufeira-algarve-portugal-guide.html). With glorious beaches and wonderful climate, there are many activities and accommodation, including its legendary nightlife, to be experienced, making it Algarve’s most popular holiday destination. Lisbon also offers many things to tourists and business people. Whether history, culture, food, or simply relaxing by water, the capital city of Portugal has many things to be enjoyed whether you’re on a business trip or just simply on a vacation.
<br><br>
The two hotels are <strong>Vila Galé Opera</strong> and <strong>Vila Galé Atlântico</strong>. There are similarities and differences between the two hotels. Both are <strong>4-star hotels</strong> under Vila Galé management, but their target markets are a bit different. With their facilities, Vila Galé Opera, located in Lisbon, is assumed to also target business-minded guests as well as tourists [[3]](https://www.vilagale.com/en/hotels/lisbon-coast/vila-gale-opera), making it fall in the <strong>city hotel category</strong>. On the contrary, Vila Galé Atlântico, located right besides Galé beach in Albufeira, is focusing more on guests who want to enjoy their vacation, both for couples and for families with children [[4]](https://www.vilagale.com/en/hotels/algarve/vila-gale-atlantico). This condition of Vila Galé Atlântico makes it fall in the <strong>resort hotel category</strong> for this research purpose.
<br><br>
However, <strong>high cancellation rates remain a challenge for hotels, influenced by customer behavior and economic uncertainties</strong>. These studies highlight that stricter cancellation policies can lead to reduced bookings as customers seek better deals, contributing to the high cancellation rates experienced by hotels [[5]](https://doi.org/10.1016/j.ijhm.2010.03.010). For instance, there is a problem in both hotels: there are <strong>lost potential revenues due to no shows and cancellations</strong> from the guests who have not finished their payment. To counter this problem, the management of Vila Galé need to <strong>revise their policy regarding cancellations and no shows</strong>. This also leads to developing a cancellation prediction machine learning model that can identify potentially canceling guests, so that the room can be accommodated to other guests. On that note, the machine learning model also need to take into account the accuracy of guests whom is predicted canceling their reservation, <strong>as failing to take that factor into account would lead to double booking</strong>, potentially <strong>receiving negative reviews and word-of-mouth</strong> for Vila Galé Opera, Vila Galé Atlântico, or even Vila Galé hotels as a whole.

</div>




<div style="text-align: left;">
  <h2 style="background-color: #2C3E3D; color: white; padding: 10px 20px; margin-bottom: 20px; border-radius: 8px; font-weight: bold; display: inline-block; font-size: 30px">Problem Hypothesis</h2>
</div>

---

<div style='text-align: justify'>

Vila Galé Hotels in Portugal are facing a significant challenge with <b>high rates of reservation cancellations and no-shows</b>. This phenomenon results in a <strong>substantial number of rooms remaining unoccupied that could have otherwise been sold</strong>, directly impacting the hotels' revenue streams. The situation creates uncertainty in room inventory management and potentially disrupts overall hotel operational efficiency. The unpredictability in occupancy rates complicates accurate forecasting, affecting decisions related to pricing, staffing, and resource allocation. This issue is particularly pressing for both <strong>Vila Galé Opera (the city hotel) and Vila Galé Atlântico (the resort hotel)</strong>, despite their differing target markets and amenities. The hotels need to understand the underlying factors contributing to these cancellations and develop strategies to mitigate their impact on business performance.
<br><br>
In detail, the problem hypothesis for a machine learning approach focus on <strong>accurately predicting and classifying the likelihood of reservation cancellations and no-shows</strong>. By developing predictive models, the hotels can <strong>minimize uncertainty in room occupancy, allowing for more effective room inventory management, dynamic pricing strategies, and optimized staffing levels</strong>. This approach would help reduce the financial impact of cancellations and no-shows, improving overall operational efficiency.<br>
The problem hypothesis for analytics might center on identifying actionable insights to increase Vila Galé Hotels revenue, even in the face of high cancellation rates. Include planning strategies to minimize reservation cancellation rates by expanding market segmentation and attracting new tourist demographics.
<br><br>
<strong>By combining machine learning models and analytics with targeted marketing, Vila Galé Hotels can better position themselves to maximize revenue and occupancy rates, even in a competitive and uncertain market environment.</strong>

</div>




<div style="text-align: left;">
  <h2 style="background-color: #2C3E3D; color: white; padding: 10px 20px; margin-bottom: 20px; border-radius: 8px; font-weight: bold; display: inline-block; font-size: 30px">Problem Goals</h2>
</div>

---

<div style='text-align: justify'>

The goals of this analysis is to assist the <b>Hotel Revenue Manager</b> in optimizing hotel revenue and improving overall operational efficiency. The analysis will focus on identifying booking patterns, occupancy trends, customer segmentation, and factors influencing reservation cancellations. The insights gained will be used to develop <b>dynamic pricing strategies, increase occupancy rates, reduce cancellations, and optimize resource allocation</b>. Ultimately, these findings will support data-driven decision-making to enhance hotel profitability during both high and low demand periods [[6]](https://www.mews.com/en/blog/hotel-revenue-manager).

</div>
<div style="text-align: left;">
  <h2 style="background-color: #2C3E3D; color: white; padding: 10px 20px; margin-bottom: 20px; border-radius: 8px; font-weight: bold; display: inline-block; font-size: 30px">Evaluation Metric</h2>
</div>

---

<div style='text-align: justify'>

<strong>Conditions:</strong>

1. **True Positive**: Guest canceled occurs, meaning the guest canceled really happening for sure.
2. **False Positive (Type I Error)**: The guest is predicted to canceled but actually doesn't.  
Consequence: Hotels may overbook or give rooms to other guests, which can cause operational problems and potential reputational damage if genuine guests still show up.
3. **True Negative**: The guest doesn't canceled, meaning they continue to booking hotel.
4. **False Negative (Type II Error)**: The guest is predicted not to canceled but actually does.  
Consequence: There's risk empty room unexpected, which is losing some potential revenue and resource usage not efficient.
<br><br>
<div style='text-align: justify'>
The <strong>F2 score</strong> is chosen as the primary evaluation metric for this guest cancellation prediction model because it emphasizes recall over precision. In the case of cancellation prediction, the main focus is to identify as many potential cancellation guest (True Positives) as possible, while minimizing type II error.
<br><br>
<strong>The reasons are:</strong>

1. Revenue Protection: F2 prioritizes recall, helping identify more potential cancellations and protect hotel revenue.

2. Cost Imbalance: False negatives (missed cancellations) are typically more costly than false positives in the hotel industry.

3. Operational Flexibility: Hotels can usually manage false positives more easily than unexpected cancellations.

4. Inventory Optimization: Higher recall enables better room allocation and occupancy maximization.

5. Proactive Management: Identifying likely cancellations allows for targeted retention efforts and improved customer engagement.

**These reasons align well with the Hotel Revenue Manager's goals of maximizing revenue, optimizing resource allocation, and improving overall operational efficiency in the hotel industry.**

</div>



<div style="text-align: left;">
  <h2 style="background-color: #2C3E3D; color: white; padding: 10px 20px; margin-bottom: 20px; border-radius: 8px; font-weight: bold; display: inline-block; font-size: 30px">Dataset Dictionary</h2>
</div>

---

|Column|Data Type|Description|
|---|---|---|
|`hotel`|categorical|Type of hotel, whether it's resort hotel or city hotel|
|`is_canceled`|categorical|Value indicating if the booking was canceled (1) or not (0)|
|`lead_time`|numerical|Number of days that elapsed between the entering date of the booking into the PMS and the arrival date|
|`arrival_date_year`|date-year|Year of arrival date|
|`arrival_date_month`|date-month|Month of arrival date|
|`arrival_date_week_number`|date-week-year|Week number of year for arrival date|
|`arrival_date_day_of_month`|date-day-month|Day of arrival date|
|`stays_in_weekend_nights`|numerical|Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel|
|`stays_in_week_nights`|numerical|Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel|
|`adults`|numerical|Number of adults in the booking|
|`children`|numerical|Number of children in the booking|
|`babies`|numerical|Number of babies in the booking|
|`meal`|categorical|Type of meal booked. Categories are presented in standard hospitality meal packages: Undefined/SC – no meal package; BB – Bed & Breakfast; HB – Half board (breakfast and one other meal – usually dinner); FB – Full board (breakfast, lunch and dinner)|
|`country`|categorical|Country of origin of the guest, represented in ISO 3155-3:2013 format|
|`market_segment`|categorical|Market segment designation. In categories, the term “TA” means “Travel Agents” and “TO” means “Tour Operators”|
|`distribution_channel`|categorical|Booking distribution channel. The term “TA” means “Travel Agents” and “TO” means “Tour Operators”|
|`is_repeated_guest`|categorical|Value indicating if the guest has stayed at the hotel before, with 1 representing a repeated guest and 0 for new guest|
|`previous_cancellations`|numerical|Number of previous bookings that were cancelled by the customer prior to the current booking|
|`previous_bookings_not_canceled`|numerical|Number of previous bookings that were not cancelled by the customer prior to the current booking|
|`reserved_room_type`|categorical|Code of room type reserved. Code is presented instead of designation for anonymity reasons|
|`assigned_room_type`|categorical|Code for the type of room assigned to the booking. Sometimes the assigned room type differs from the reserved room type due to hotel operation reasons (e.g. overbooking) or by customer request. Code is presented instead of designation for anonymity reasons|
|`booking_changes`|numerical|Number of changes/amendments made to the booking from the moment the booking was entered on the PMS until the moment of check-in or cancellation|
|`deposit_type`|categorical|Indication on if the customer made a deposit to guarantee the booking. This variable can assume three categories: No Deposit – no deposit was made; Non Refund – a deposit was made in the value of the total stay cost; Refundable – a deposit was made with a value under the total cost of stay|
|`agent`|categorical|ID of the travel agency that made the booking|
|`company`|categorical|ID of the company/entity that made the booking or responsible for paying the booking. ID is presented instead of designation for anonymity reasons|
|`days_in_waiting_list`|numerical|Number of days the booking was on the waiting list before it was confirmed to the customer|
|`customer_type`|categorical|Type of booking, assuming one of four categories: Contract - when the booking has an allotment or other type of contract associated to it; Group – when the booking is associated to a group; Transient – when the booking is not part of a group or contract, and is not associated to other transient booking; Transient-party – when the booking is transient, but is associated to at least other transient booking|
|`adr`|numerical|Average Daily Rate as defined by dividing the sum of all lodging transactions by the total number of staying nights|
|`required_car_parking_spaces`|numerical|Number of car parking spaces required by the guest|
|`total_of_special_requests`|numerical|Number of special requests made by the guest (e.g. twin bed or high floor)|
|`reservation_status`|categorical|Reservation last status, assuming one of three categories: Canceled – booking was canceled by the customer; Check-Out – customer has checked in but already departed; No-Show – customer did not check-in and did inform the hotel of the reason why|
|`reservation_status_date`|date|Date at which the last status was set. This variable can be used in conjunction with the ReservationStatus to understand when was the booking canceled or when did the customer checked-out of the hotel|

For analysis purpose, several columns also need to be added into the dataframe. The columns are:
* `arrival_date`: exact arrival date of the guest(s), from columns containing `arrival_date` in their names.
* `gap_of_arrival_and_reservation_status`: to know in which day guests canceled their reservations. Since check-out guests reservation status change occurs when they check-out, for this category, the lower point of this columns will be set to 0.
* `duration_of_stay`: adding duration of stay of weeknights and weekends.
* `matched_rooms_assigned_reserved`: to know whether guests get their reserved room or had to switch to other rooms available; 1 means the room reserved and assigned matched, while 0 means otherwise.
* `booking_date`: exact date of when reservations made.
* `live_time`: number of days between `booking_date` and `reservation_status_date`, if the reservation was not cancelled, the `live_time` is the same with ADR.
* `previous_cancellation_ratio`: ratios of how many cancelled reservations before the current reservation per total reservations made before.
* `was_in_waiting_list`: grouping of whether the reservations were immediately put into the PMS or needed to wait before being inputted.
* `is_local`: grouping of whether the reservations made by guests from Portugal or not, if yes, the value is 1.
* `adr_third_quartile_deviation`: normalization of `adr` columns using `arrival_date_year`, `arrival_date_week_number`, `distribution_channel`, and `reserved_room_type` to avoid multicollinearity and reduce effects of said columns to `adr`.



<div style="text-align: left;">
  <h2 style="background-color: #2C3E3D; color: white; padding: 10px 20px; margin-bottom: 20px; border-radius: 8px; font-weight: bold; display: inline-block; font-size: 30px">Conclusion of Data Cleaning</h2>
</div>

---

To summarize what was done in the data cleaning process, the changed of the current dataframe with the original dataframe are listed below:
* Missing Value:
    - Dropping missing values in columns `children` and `country`
    - Filling missing values in columns `agent` and `company` with string value 'undefined'
* Duplicate Entries:
    - Remove any data that had more than 7 duplicates
* Data Anomalies:
    - `country`:
        - Replace 'CN' with 'CHN'
        - Replace 'TMP' with 'TLS'
    - `meals`:
        - combine 'Undefined' with 'SC' (or Self-Catering)
    - `market_segment`:
        - remove 'Undefined' (treated as missing values)
    - `distribution_channel`:
        - remove 'Undefined' (trated as missing values)
    - `duration_of_stay`:
        - remove any data with zero days stays
    - `adr`:
        - remove outliers and negative values
    - `children`:
        - remove outliers
    - `babies`:
        - remove outliers
    - `required_car_parking_spaces`:
        - remove outliers


The cleaned data is enclosed in this repository with the name `hotel_bookings_cleaned.csv`.



<div style="text-align: left;">
  <h2 style="background-color: #2C3E3D; color: white; padding: 10px 20px; margin-bottom: 20px; border-radius: 8px; font-weight: bold; display: inline-block; font-size: 30px">Modeling</h2>
</div>

---

<div style='text-align: justify'>
For this guest prediction cancellation project, we will separate the dataset into features (independent variables) and target (dependent variable). Features include columns excluding 'is_canceled', such as 'agent', 'company', and others. <strong>Our target is the 'is_canceled' column</strong>, which indicates whether a guest canceled or not. This separation is crucial for training the model to predict canceled based on guest characteristics.

To be precise, there are 19 columns used as features, listed below:
* Categorical features: `hotel`, `agent`, `company`, `customer_type`, `deposit_type`, `distribution_channel`, `market_segment`, `meal`, `is_local`, `was_in_waiting_list`, `is_repeated_guest`;
* Numerical features: `adr_third_quartile_deviation`, `adults`, `booking_changes`, `lead_time`, `previous_cancellation_ratio`, `total_of_special_requests`, `duration_of_stay`, `arrival_date_week_number`.
</div>


<div style='text-align: justify'>
The dataset <strong>will be split into training and testing data with an 80:20 ratio</strong>. The training data will be used to train the model, while the testing data will be used to evaluate the model's performance. This split is important for assessing the model's ability to generalize to new, unseen data.
</div>

Based on the cross-validating and model evaluation, the model chosen for this case is **the hyperparameter tuned model of XGBoost Classifier using Random Oversampling** as the resample method. Using F2-score as the main metric, its F2-score was as high as 81%. This model also **has a very high recall of 95%**. Other than precision, the other metrics also seem okay from this team rule of thumb, with accuracy of 74%, precision of 52%, and F1-score of 0.67%. The model has been saved as an pickle object, and ready to be deployed.


<div style="text-align: left;">
  <h2 style="background-color: #2C3E3D; color: white; padding: 10px 20px; margin-bottom: 20px; border-radius: 8px; font-weight: bold; display: inline-block; font-size: 30px">Model Limitations</h2>
</div>

---

This model was trained using Xtreme Gradient Booster model for classification, with the train data were resampled using Random Oversampling method. While the model may perform well, there are several limitations while inputting data to be used as features, listed below:
* `lead_time` must be inbetween 0 and 709;
* `duration_of_stay` must be inbetween 1 and 57;
* `previous_cancellation_ratio` must be in between 0 and 1;
* `booking_changes` must be in between 0 and 21;
* `total_of_special_requests` must be in between 0 and 5.

<br><hr>
[🔼 Back to top](#readme-top)
