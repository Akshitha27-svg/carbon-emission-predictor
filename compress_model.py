import gzip
import shutil

with open("forecasting_co2_emmision.pkl", "rb") as f_in:
    with gzip.open("forecasting_co2_emmision.pkl.gz", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

print("✅ Compression complete: forecasting_co2_emmision.pkl.gz created")
