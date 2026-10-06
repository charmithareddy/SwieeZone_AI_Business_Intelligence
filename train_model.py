import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# -----------------------------------------
# 1. Load SwieeZone sales data
# -----------------------------------------

df = pd.read_csv("data/swieeZone_sales.csv")

print("Dataset loaded successfully!")
print(f"Total rows: {len(df)}")


# -----------------------------------------
# 2. Select features and target
# -----------------------------------------

features = [
    "Product",
    "Category",
    "Quantity",
    "Price",
    "Discount",
    "Region",
    "Payment_Method"
]

target = "Revenue"

X = df[features]
y = df[target]


# -----------------------------------------
# 3. Identify column types
# -----------------------------------------

categorical_features = [
    "Product",
    "Category",
    "Region",
    "Payment_Method"
]

numerical_features = [
    "Quantity",
    "Price",
    "Discount"
]


# -----------------------------------------
# 4. Convert categorical data
# -----------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# -----------------------------------------
# 5. Create Machine Learning model
# -----------------------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# -----------------------------------------
# 6. Create complete ML pipeline
# -----------------------------------------

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# -----------------------------------------
# 7. Split the data
# -----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# -----------------------------------------
# 8. Train the model
# -----------------------------------------

print("Training model...")

pipeline.fit(X_train, y_train)

print("Model training completed!")


# -----------------------------------------
# 9. Test the model
# -----------------------------------------

predictions = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Performance")
print("-----------------")
print(f"Mean Absolute Error: ₹{mae:,.2f}")
print(f"R² Score: {r2:.4f}")


# -----------------------------------------
# 10. Save the trained model
# -----------------------------------------

joblib.dump(
    pipeline,
    "models/swieeZone_revenue_model.pkl"
)

print("\nModel saved successfully!")
print("Location: models/swieeZone_revenue_model.pkl")