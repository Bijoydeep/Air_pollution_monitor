import requests
import pandas as pd

def load_openaq_data(location, pollutant):
    try:
        url = f"https://api.openaq.org/v2/measurements"
        params = {
            "city": location,
            "parameter": pollutant,
            "limit": 100,
            "sort": "desc",
            "order_by": "date"
        }
        response = requests.get(url, params=params).json()
        results = response["results"]
        df = pd.DataFrame(results)
        df["date_utc"] = pd.to_datetime(df["date"]["utc"])
        df = df[["date_utc", "value"]].set_index("date_utc").resample("D").mean()
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
