import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Esta es mi primera app")

np.random.seed(1234)

X = np.random.normal(0, 10, 1000)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

ax.hist(X, bins=50)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

st.pyplot(fig)
