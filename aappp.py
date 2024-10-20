import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load(r'car_name_model.pkl')

# User interface
st.title("Car Name Prediction")
st.write("Please enter the features of the car to get a prediction.")

# Input features
gender = st.selectbox("Gender", options=['Male', 'Female'])

# Annual income input using slider
annual_income = st.slider("Annual Income", min_value=10080, max_value=11200000, value=50000)

model_input = st.selectbox("Model", options=[
    'Expedition', 'Durango', 'Eldorado', 'Celica', 'TL', 'Diamante', 'Corolla',
    'Galant', 'Malibu', 'Escort', 'RL', 'Pathfinder', 'Grand Marquis', '323i',
    'Sebring Coupe', 'Forester', 'Accent', 'Land Cruiser', 'Accord', '4Runner',
    'I30', 'A4', 'Carrera Cabrio', 'Jetta', 'Viper', 'Regal', 'LHS', 'LW', '3000GT',
    'SLK230', 'Civic', 'S-Type', 'S40', 'Mountaineer', 'Park Avenue',
    'Montero Sport', 'Sentra', 'S80', 'Lumina', 'Bonneville', 'C-Class', 'Altima',
    'DeVille', 'Stratus', 'Cougar', 'SW', 'C70', 'SLK', 'Tacoma', 'M-Class', 'A6',
    'Intrepid', 'Sienna', 'Eclipse', 'Contour', 'Town car', 'Focus', 'Mustang',
    'Cutlass', 'Corvette', 'Impala', 'Cabrio', 'Dakota', '300M', '328i', 'Bravada',
    'Maxima', 'Ram Pickup', 'Concorde', 'V70', 'Quest', 'ES300', 'SL-Class',
    'Explorer', 'Prizm', 'Camaro', 'Outback', 'Taurus', 'Cavalier', 'GS400',
    'Monte Carlo', 'Sonata', 'Sable', 'Metro', 'Voyager', 'Cirrus', 'Avenger',
    'Odyssey', 'Intrigue', 'Silhouette', '5-Sep', '528i', 'LS400', 'Aurora',
    'Breeze', 'Beetle', 'Elantra', 'Continental', 'RAV4', 'Villager', 'S70', 'LS',
    'Ram Van', 'S-Class', 'E-Class', 'Grand Am', 'SC', 'Passat', 'Xterra',
    'Frontier', 'Crown Victoria', 'Camry', 'Navigator', 'CL500', 'Escalade', 'Golf',
    'Ranger', 'Prowler', 'Windstar', 'GTI', 'Passport', 'Boxter', 'LX470', 'CR-V',
    'Sunfire', 'Caravan', 'Ram Wagon', 'Neon', 'Wrangler', 'Integra', 'Grand Prix',
    'Grand Cherokee', 'F-Series', 'A8', 'Mystique', '3-Sep', 'Cherokee',
    'Carrera Coupe', 'Catera', 'Seville', 'CLK Coupe', 'LeSabre', 'Sebring Conv.',
    'GS300', 'Firebird', 'V40', 'Montero', 'Town & Country', 'SL', 'Alero', 'Mirage',
    'Century', 'RX300', 'Avalon'
])
engine = st.selectbox("Engine Type", options=['Double Overhead Camshaft', 'Overhead Camshaft'])
transmission = st.selectbox("Transmission", options=['Auto', 'Manual'])

# Adding Body Style option
body_style = st.selectbox("Body Style", options=['SUV', 'Passenger', 'Hatchback', 'Hardtop', 'Sedan'])

# Adding dealer region option
dealer_region = st.selectbox("Dealer Region", options=[
    'Middletown', 'Aurora', 'Greenville', 'Pasco', 'Janesville', 'Scottsdale', 'Austin'
])
# Define price options
price_options = [
    26000, 19000, 31500, 14000, 24500, 12000, 42000, 82000, 15000, 31000,
    46000, 9000, 17000, 18000, 33000, 21000, 25000, 22000, 31250, 41000,
    13000, 20000, 43000, 16000, 61000, 39000, 42500, 45001, 36001, 21001,
    29000, 27000, 25600, 36000, 31100, 22600, 45000, 62000, 22700, 49000,
    28000, 22001, 25001, 12800, 22500, 46500, 54000, 16001, 38000, 21200,
    71000, 57001, 62001, 69001, 20001, 26750, 24000, 28501, 15500, 12500,
    27250, 11000, 26500, 69000, 14150, 60500, 44000, 11650, 11800, 27500,
    16900, 14200, 51000, 32000, 39500, 13500, 9250, 29500, 18501, 17001,
    23500, 53000, 60750, 24001, 35000, 18500, 21500, 41100, 20200, 59000,
    57000, 25500, 19100, 10000, 23000, 11501, 24250, 37000, 54500, 25100,
    34000, 21900, 29200, 85000, 43500, 14500, 16500, 85600, 75000, 71500,
    61500, 19500, 29001, 60000, 28001, 60001, 22100, 21100, 31001, 36600,
    53500, 49300, 17500, 26001, 23501, 9200, 22650, 57500, 39600, 28100,
    9500, 16700, 69500, 18001, 45500, 15601, 16800, 22200, 39501, 19001,
    20500, 14100, 12001, 34300, 51200, 32500, 49500, 20600, 33500, 49001,
    39001, 85001, 26501, 18100, 62500, 15510, 14001, 27501, 16251, 26251,
    10500, 29300, 22250, 19020, 15001, 18250, 12300, 41500, 42200, 51850,
    82500, 15100, 45200, 44001, 20700, 28500, 51500, 28800, 53001, 75500,
    17250, 12700, 27200, 22150, 15400, 19750, 19200, 13050, 36200, 69100,
    38500, 16100, 29600, 24100, 18180, 31800, 42700, 14600, 26700, 41001,
    27001, 24200, 36500, 23001, 11100, 71200, 28200, 19300, 9600, 26100,
    22300, 42100, 46801, 10100, 21501, 33800, 12600, 9001, 33001, 31600,
    49750, 27300, 42001, 34500, 14900, 43200, 22601, 33200, 11500, 18200,
    31700, 38001, 15600, 31900, 43001, 35001, 51001, 16501, 51501, 34001,
    71501, 17201, 25800, 62600, 22101, 27201, 75001, 54001, 36700, 15880,
    20100, 22800, 25200, 20250, 42801, 71001, 21701, 19700, 13001, 24501,
    46600, 14800, 71700, 9800, 19250, 12250, 61001, 41501, 24101, 41251,
    75501, 10001, 46001, 19400, 21700, 29080, 44500, 32001, 41400, 75600,
    46100, 45800, 14501, 10700, 13501, 85301, 17350, 13750, 43300, 24751,
    12200, 18101, 18800, 26200, 45100, 69800, 20150, 22501, 11001, 36501,
    43800, 69980, 82001, 19800, 62200, 19501, 29100, 9700, 36350, 41200,
    23700, 17801, 13801, 29400, 20300, 19600, 17800, 17700, 31201, 21600,
    29800, 12501, 31501, 19050, 21801, 38281, 18601, 33501, 57600, 49101,
    71950, 25400, 31301, 51100, 17501, 71210, 42800, 82101, 16250, 23250,
    41250, 26600, 17600, 44750, 24900, 25251, 69600, 17100, 45101, 75350,
    39050, 22401, 17450, 41900, 29250, 45350, 32600, 61100, 21881, 10701,
    12750, 61501, 15251, 39200, 53101, 35500, 22400, 34501, 18550, 28600,
    43501, 69300, 38200, 46080, 54900, 31801, 44700, 17200, 24701, 45601,
    31400, 69101, 31750, 39100, 82600, 15800, 20501, 21400, 38100, 23200,
    43100, 61050, 26250, 39400, 13100, 13400, 22350, 45501, 26881, 57201,
    22201, 18600, 28700, 45600, 27100, 26601, 12801, 51150, 43540, 12100,
    69200, 71900, 33600, 23100, 33100, 18400, 46700, 61101, 41450, 21050,
    10600, 25250, 71901, 14750, 21300, 27801, 44501, 49010, 38201, 82300,
    60501, 37001, 17301, 23801, 9380, 12701, 16101, 16200, 22801, 34200,
    85250, 45450, 23050, 45180, 53300, 11900, 9100, 19801, 71800, 13780,
    45880, 29801, 35222, 16151, 24800, 17101, 60600, 54750, 42600, 18081,
    22251, 14400, 17220, 27750, 85800, 25501, 49501, 42501, 18201, 27251,
    16901, 39550, 33601, 26801, 17701, 20601, 21250, 71580, 18900, 26690,
    25300, 57990, 25900, 33700, 26550, 29880, 13550, 71990, 53900, 18350,
    53501, 17750, 21201, 18801, 31200, 22750, 27800, 37500, 46501, 35100,
    25951, 26101, 17050, 18150, 14901, 44751, 26800, 20140, 16600, 14201,
    51800, 13601, 46601, 28250, 31110, 25650, 18301, 21101, 17751, 29501,
    15501, 24601, 14101, 82250, 19101, 14700, 26880, 37700, 17601, 20751,
    62501, 24600, 25700, 9251, 69501, 25201, 71101, 14251, 10050, 24300,
    85200, 19581, 37501, 27101, 85500, 69700, 57750, 45250, 34201, 38501,
    75700, 19701, 28201, 20800, 15200, 82750, 25081, 36100, 41800, 49701,
    53250, 11101, 20401, 13850, 49601, 20101, 13350, 42900, 39800, 25701,
    49801, 43201, 32501, 25601, 24700, 22900, 9501, 19401, 51300, 11200,
    19900, 34801, 16750, 20400, 42250, 19601, 39401, 60850, 16450, 15401,
    23800, 46400, 26150, 19090, 32300, 22751, 25101, 12511, 15551, 46651,
    26850, 57250, 85300, 54501, 43650, 36300, 29601, 57501, 13701, 14300,
    24301, 31701, 62100, 29101, 13300, 13700, 21750, 11300, 18050, 35800,
    21301, 19150, 60100, 23600, 36601, 24201, 9201, 37281, 23701, 45050,
    45251, 17900, 12050, 36800, 14151, 18251, 13200, 43600, 61300, 14851,
    39250, 14401, 23551, 21601, 10501, 36401, 61800, 43950, 49600, 15250,
    15071, 43880, 82100, 10751, 10201, 12350, 31300, 11456, 36301, 49700,
    26301, 42201, 24233, 43101, 27301, 69301, 1200, 4200, 42101, 27601,
    1450, 12101, 23051, 1700, 2200, 51600, 20251, 4300, 23950, 19751,
    13900, 16701, 19201, 14971, 20201, 39900, 21880, 53100, 35400, 15701,
    18401, 46101, 15101, 75200, 11901, 25751, 60851, 22870, 62601, 20351,
    39750, 25050, 38330, 34701, 10301, 49100, 26051, 49800, 16801, 29901,
    39601, 45750, 54300, 14601, 9901, 13600, 21401, 9601, 9750, 41301,
    41401, 13250, 31770, 32200, 12151, 17551, 34600, 26900, 62800, 20750,
    38720, 31601, 62801, 69150, 60101, 39801, 28750, 15201, 20701, 60250,
    34751, 85601, 16401, 20900, 27900, 14050, 20881, 43601, 71801, 15151,
    85400, 18300, 28901, 26300, 29751, 12601, 75100, 29700, 44100, 54601,
    21130, 38101, 28101, 39101, 53301, 27880, 41201, 62201, 57200, 12201,
    27701, 46401, 39651, 69180, 42850, 16400, 41050, 45401, 15900, 37600,
    22010, 46200, 45201, 24750, 15700, 20791, 34550, 10200, 17580, 17300,
    39340, 25301, 51601, 36250, 12301, 19880, 26751, 17650, 82351, 28301,
    12470, 33170, 19451, 29301, 19011, 37100, 82800, 45490, 23550, 22701,
    69801, 51900, 43080, 53200, 71100, 16651, 29701, 57300, 19301, 54100,
    18701, 41700, 11350, 61200, 36400, 27700, 33301, 49200, 23881, 20340,
    9400, 34800, 27600, 31101, 41801, 15300, 16601, 29201, 26331, 34100,
    45550, 10601, 61401, 42401, 41101, 60700, 75400, 25350, 18110, 49250,
    19901, 44331, 16150, 62300, 57100, 13800, 53600, 16300, 23400, 38300,
    46690, 10400, 9910, 51401, 32250, 23180, 31991, 61250, 82450, 11060]

# Price input using slider
selected_price = st.slider("Select Price", min_value=1200, max_value=85800, value=30000)

# Finding the closest price from available options
closest_price = min(price_options, key=lambda x: abs(x - selected_price))

st.write(f"Selected Price: {closest_price}")

# On button click for prediction
if st.button("Predict"):
    # Preparing data for prediction
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Annual Income': [annual_income],
        'Model': [model_input],
        'Engine': [engine],
        'Transmission': [transmission],
        'Price ($)': [closest_price],
        'Body Style': [body_style],
        'Dealer_Region': [dealer_region]

    })

    # Convert categorical features to dummy variables
    input_data_encoded = pd.get_dummies(input_data, drop_first=True)

    # Reindex to match the model's input features
    input_data_encoded = input_data_encoded.reindex(columns=model.feature_names_in_, fill_value=0)

    # Making prediction
    prediction = model.predict(input_data_encoded)
    st.write(f"Predicted Car Name: {prediction[0]}")




