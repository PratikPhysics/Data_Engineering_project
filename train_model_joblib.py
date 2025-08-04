import pandas as pd
import pymysql
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
import joblib
import sklearn
import warnings

warnings.filterwarnings("ignore")

# === 1. Connect to MySQL and Load Data ===
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='pratik',
    database='BigMart'
)

df_item = pd.read_sql("SELECT * FROM item_info", connection)
df_outlet = pd.read_sql("SELECT * FROM outlet_info", connection)
df_sales = pd.read_sql("SELECT * FROM sales_info", connection)
connection.close()

# === 2. Merge DataFrames ===
df = df_item.merge(df_outlet, on='ID').merge(df_sales, on='ID')
df.drop('ID', axis=1, inplace=True)

# === 3. Feature Engineering ===
df['Outlet_Age'] = 2025 - df['Outlet_Establishment_Year']
df.drop('Outlet_Establishment_Year', axis=1, inplace=True)

df['Item_Fat_Content'] = df['Item_Fat_Content'].replace({
    'low fat': 'Low Fat',
    'LF': 'Low Fat',
    'reg': 'Regular'
})

df['Item_Visibility'] = np.where(df['Item_Visibility'] > 0.3, 0.3, df['Item_Visibility'])

# === 4. Prepare X, y ===
X = df.drop('Item_Outlet_Sales', axis=1)
y = df['Item_Outlet_Sales']

# === 5. Categorical vs Numerical Columns ===
categorical_cols = X.select_dtypes(include='object').columns.tolist()

# === 6. Preprocessing Pipeline ===
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'
)

# === 7. Full Pipeline with Model ===
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, random_state=42))
])

# === 8. Train/Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === 9. Train Model ===
model.fit(X_train, y_train)

# === 10. Evaluate ===
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)

print("\n✅ Model Trained Successfully")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.2f}")

# === 11. Save model with version info ===
joblib.dump((model, sklearn.__version__), "bigmart_model.joblib")
print(f"✅ Model saved with scikit-learn version {sklearn.__version__}")
