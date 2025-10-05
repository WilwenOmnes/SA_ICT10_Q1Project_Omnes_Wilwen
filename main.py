from pyscript import display
import pandas as pd

services = {
    "Service": [
        "30-min Relaxation Massage",
        "60-min Deep Tissue Massage",
        "90-min Full Body Massage",
        "Foot Massage",
        "Head & Shoulder Massage"
    ],
    "Price (₱)": [300.00, 600.00, 900.00, 250.00, 200.00]
}

df = pd.DataFrame(services)
display(df, target="service-table")