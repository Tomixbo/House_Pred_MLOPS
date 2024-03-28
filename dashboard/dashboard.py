import pandas as pd
from explainerdashboard import ExplainerDashboard, RegressionExplainer
from pycaret.regression import load_model
from dash_bootstrap_components.themes import PULSE

df = pd.read_csv("test_data.csv")
X = df[["lat", "long", "sqft_living", "sqft_above", "sqft_living15", "sqft_lot15", "yr_built", "zipcode", "sqft_basement", "grade"]]
y = df['price']

model = load_model("House-sales-10pred-tuned")

explainer = RegressionExplainer(model, X, y)

# run
ExplainerDashboard(explainer, 
                        title="House sales price prediction", 
                        whatif=False,
                        shap_dependence=False,
                        shap_interaction=False,
                        no_permutations=True,
                        decision_trees=False,
                        bootstrap=PULSE
                        ).run(host='0.0.0.0', port=1235, use_waitress=True)