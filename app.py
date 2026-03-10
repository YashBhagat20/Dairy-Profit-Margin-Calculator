from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Farmer Milk Profit Predictor API")


class MilkInput(BaseModel):
    cow_milk: float
    buffalo_milk: float
    healthcare_cost: float
    transport_cost: float
    helper_cost: float
    machinery_cost: float


class MilkProfitPredictor:

    def __init__(self, data: MilkInput):

        self.cow_milk = data.cow_milk
        self.buffalo_milk = data.buffalo_milk
        self.total_milk = self.cow_milk + self.buffalo_milk

        # Prices per litre
        self.price_customer = 72
        self.price_supplier = 144
        self.price_vendor = 102

        # Costs
        self.healthcare_cost = data.healthcare_cost
        self.transport_cost = data.transport_cost
        self.helper_cost = data.helper_cost
        self.machinery_cost = data.machinery_cost

    def distribute_milk(self):

        share = self.total_milk / 3

        return {
            "customers_litres": share,
            "suppliers_litres": share,
            "vendors_litres": share
        }

    def calculate_revenue(self):

        distribution = self.distribute_milk()

        customer_revenue = distribution["customers_litres"] * self.price_customer
        supplier_revenue = distribution["suppliers_litres"] * self.price_supplier
        vendor_revenue = distribution["vendors_litres"] * self.price_vendor

        total_revenue = customer_revenue + supplier_revenue + vendor_revenue

        return {
            "customer_revenue": customer_revenue,
            "supplier_revenue": supplier_revenue,
            "vendor_revenue": vendor_revenue,
            "total_revenue": total_revenue
        }

    def calculate_costs(self):

        return (
            self.healthcare_cost
            + self.transport_cost
            + self.helper_cost
            + self.machinery_cost
        )

    def calculate_profit(self):

        revenue = self.calculate_revenue()["total_revenue"]
        cost = self.calculate_costs()

        return revenue - cost

    def monthly_prediction(self):

        return self.calculate_profit() * 30


@app.get("/")
def root():
    return {"message": "Farmer Milk Profit Predictor API is running"}


@app.post("/predict-profit")
def predict_profit(data: MilkInput):

    predictor = MilkProfitPredictor(data)

    distribution = predictor.distribute_milk()
    revenue = predictor.calculate_revenue()
    daily_profit = predictor.calculate_profit()
    monthly_profit = predictor.monthly_prediction()

    return {
        "milk_distribution": distribution,
        "revenue": revenue,
        "daily_profit": daily_profit,
        "monthly_prediction": monthly_profit
    }